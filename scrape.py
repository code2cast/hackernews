#!/usr/bin/env python3
"""Scrape Hacker News stories and comments to markdown files."""

import asyncio
import html
import re
from datetime import datetime, timezone
from pathlib import Path

import click
import httpx

HN_API = "https://hacker-news.firebaseio.com/v0"
ALGOLIA_API = "https://hn.algolia.com/api/v1"
MAX_CONCURRENT = 20
MAX_RETRIES = 3


async def fetch_item(
    client: httpx.AsyncClient, sem: asyncio.Semaphore, item_id: int
) -> dict | None:
    """Fetch a single HN item by ID with retries."""
    for attempt in range(MAX_RETRIES):
        try:
            async with sem:
                resp = await client.get(f"{HN_API}/item/{item_id}.json")
            if resp.status_code == 200 and resp.json() is not None:
                return resp.json()
            return None
        except httpx.HTTPError:
            if attempt == MAX_RETRIES - 1:
                return None
            await asyncio.sleep(0.5 * (attempt + 1))
    return None


async def fetch_comment_tree(
    client: httpx.AsyncClient,
    sem: asyncio.Semaphore,
    comment_id: int,
    max_replies: int = 30,
    depth: int = 0,
    max_depth: int = 3,
) -> dict | None:
    """Fetch a comment and its reply tree recursively."""
    comment = await fetch_item(client, sem, comment_id)
    if not comment or comment.get("deleted") or comment.get("dead"):
        return None

    replies = []
    kid_ids = comment.get("kids", [])[:max_replies]
    if kid_ids and depth < max_depth:
        tasks = [
            fetch_comment_tree(client, sem, kid, max_replies, depth + 1, max_depth)
            for kid in kid_ids
        ]
        results = await asyncio.gather(*tasks)
        replies = [r for r in results if r]

    return {
        "by": comment.get("by", "[deleted]"),
        "text": comment.get("text", ""),
        "time": comment.get("time", 0),
        "replies": replies,
    }


async def fetch_story_comments(
    client: httpx.AsyncClient,
    sem: asyncio.Semaphore,
    story: dict,
    max_root: int = 15,
    max_replies: int = 30,
) -> list[dict]:
    """Fetch top comments for a story."""
    kid_ids = story.get("kids", [])[:max_root]
    if not kid_ids:
        return []

    tasks = [fetch_comment_tree(client, sem, kid, max_replies) for kid in kid_ids]
    results = await asyncio.gather(*tasks)
    return [r for r in results if r]


def html_to_markdown(h: str) -> str:
    """Convert HN HTML comments to markdown text."""
    if not h:
        return ""
    text = h.replace("<p>", "\n\n")
    text = re.sub(r'<a\s+href="([^"]*)"[^>]*>([^<]*)</a>', r"[\2](\1)", text)
    text = text.replace("<i>", "*").replace("</i>", "*")
    text = text.replace("<b>", "**").replace("</b>", "**")
    text = re.sub(
        r"<pre><code>(.*?)</code></pre>", r"```\n\1\n```", text, flags=re.DOTALL
    )
    text = re.sub(r"<code>(.*?)</code>", r"`\1`", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    return text.strip()


def format_comment(comment: dict, depth: int = 0) -> str:
    """Format a comment and its replies as markdown."""
    author = comment["by"]
    text = html_to_markdown(comment["text"])
    lines = []

    if depth == 0:
        lines.append(f"### {author}")
        lines.append("")
        lines.append(text)
    else:
        blockquote = "> " * depth
        for line in f"**{author}**: {text}".split("\n"):
            lines.append(f"{blockquote}{line}")

    lines.append("")

    for reply in comment.get("replies", []):
        lines.append(format_comment(reply, depth + 1))

    return "\n".join(lines)


def slugify(title: str) -> str:
    """Convert a title to a filesystem-safe slug."""
    slug = re.sub(r"[^\w\s-]", "", title.lower())
    slug = re.sub(r"[\s_]+", "-", slug)
    return slug[:80].strip("-")


def story_to_markdown(story: dict, comments: list[dict]) -> str:
    """Convert a story + comments to a markdown document."""
    title = story.get("title", "Untitled")
    url = story.get("url", "")
    hn_url = f"https://news.ycombinator.com/item?id={story['id']}"
    score = story.get("score", 0)
    author = story.get("by", "unknown")
    time_str = datetime.fromtimestamp(story.get("time", 0), tz=timezone.utc).strftime(
        "%Y-%m-%d %H:%M UTC"
    )
    num_comments = story.get("descendants", 0)

    lines = [
        f"# {title}",
        "",
    ]

    if url:
        lines.append(f"- **Link**: {url}")
    lines.extend(
        [
            f"- **HN**: {hn_url}",
            f"- **Score**: {score} points",
            f"- **By**: {author}",
            f"- **Date**: {time_str}",
            f"- **Comments**: {num_comments}",
            "",
        ]
    )

    if story.get("text"):
        lines.extend(["---", "", html_to_markdown(story["text"]), ""])

    lines.extend(["---", "", "## Comments", ""])

    for comment in comments:
        lines.append(format_comment(comment))
        lines.append("---\n")

    if not comments:
        lines.append("*No comments yet.*\n")

    return "\n".join(lines)


async def get_front_page_stories(
    client: httpx.AsyncClient, sem: asyncio.Semaphore, limit: int
) -> list[dict]:
    """Fetch top stories from the HN front page."""
    resp = await client.get(f"{HN_API}/topstories.json")
    resp.raise_for_status()
    ids = resp.json()[:limit]

    tasks = [fetch_item(client, sem, sid) for sid in ids]
    stories = await asyncio.gather(*tasks)
    return [s for s in stories if s]


async def search_stories(
    client: httpx.AsyncClient, sem: asyncio.Semaphore, query: str, limit: int
) -> list[dict]:
    """Search HN stories via Algolia, then hydrate from Firebase."""
    resp = await client.get(
        f"{ALGOLIA_API}/search",
        params={"query": query, "tags": "story", "hitsPerPage": limit},
    )
    resp.raise_for_status()
    hits = resp.json().get("hits", [])

    hn_ids = [int(h["objectID"]) for h in hits]
    tasks = [fetch_item(client, sem, sid) for sid in hn_ids]
    stories = await asyncio.gather(*tasks)
    return [s for s in stories if s]


async def run(search: str | None, limit: int, output_dir: Path):
    today = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")

    if search:
        subdir = "search-" + slugify(search)
    else:
        subdir = "frontpage"

    dest = output_dir / "news" / today / subdir
    dest.mkdir(parents=True, exist_ok=True)

    sem = asyncio.Semaphore(MAX_CONCURRENT)

    async with httpx.AsyncClient(timeout=30) as client:
        if search:
            click.echo(f"Searching HN for '{search}' (limit {limit})...")
            stories = await search_stories(client, sem, search, limit)
        else:
            click.echo(f"Fetching HN front page (limit {limit})...")
            stories = await get_front_page_stories(client, sem, limit)

        click.echo(f"Found {len(stories)} stories. Fetching comments...")

        for i, story in enumerate(stories, 1):
            title = story.get("title", "Untitled")
            click.echo(f"  [{i}/{len(stories)}] {title}")

            comments = await fetch_story_comments(
                client, sem, story, max_root=15, max_replies=30
            )
            md = story_to_markdown(story, comments)

            filename = f"{slugify(title)}.md"
            (dest / filename).write_text(md, encoding="utf-8")

    click.echo(f"\nDone! {len(stories)} files saved to {dest}")


@click.command()
@click.argument("search", required=False, default=None)
@click.option("--limit", "-n", default=30, help="Number of stories to fetch")
@click.option(
    "--output",
    "-o",
    default=".",
    help="Output base directory",
    type=click.Path(path_type=Path),
)
def main(search, limit, output):
    """Scrape Hacker News stories and comments to markdown.

    Omit SEARCH to scrape the front page. Provide a term to search HN.

    \b
    Examples:
        python scrape.py                  # Front page, 10 stories
        python scrape.py -n 5             # Front page, 5 stories
        python scrape.py "rust lang" -n 3 # Search for "rust lang", 3 results
    """
    asyncio.run(run(search, limit, output))


if __name__ == "__main__":
    main()
