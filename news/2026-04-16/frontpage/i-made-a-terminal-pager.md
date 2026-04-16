# I made a terminal pager

- **Link**: https://theleo.zone/posts/pager/
- **HN**: https://news.ycombinator.com/item?id=47786164
- **Score**: 149 points
- **By**: speckx
- **Date**: 2026-04-15 22:27 UTC
- **Comments**: 35

---

## Comments

### asibahi

Slightly related: I am an Arab who speaks Arabic and reads Arabic and the only place I ever see the unicode character ﷽ is by programmers giving an example of "unicode is too hard".

Perhaps as a graphical element at the beginning of books, too.

It is a part of the Arabic Presentation Forms block which explicitly is for supporting legacy encodings and should not be used.

---

### CGamesPlay

I am definitely waiting for a "modern less replacement" in the same vein as fd, sd, fzf, and the rest of the under-20yo cli crew. I get that "less" is reasonably maintained still.

I think the killer feature for me would be refresh. I get that this can't work for piped input, but I want `git diff` to show in a pager with a refresh button that holds my place. fzf supports both refresh and piped input, so perhaps there's some ideas there that could be leveraged.

> **busfahrer**: I've noticed that subconsciously, I've started to use `bat` for interactive paging, even though that's not its main use case

> > **CGamesPlay**: Bat just uses less internally. And it deliberately breaks less’ handling of ^C, annoyingly.

> **zeech**: I went looking for a 'new' pager a couple years back and settled on this [0].  I've since gone back to `less` since it got annoying jumping between systems and having different pagers, but when I used it it was quite nice.
> 
> [0] [https://github.com/walles/moor](https://github.com/walles/moor)

> **anthk**: That should be under a less(1) flag, but optional as it can mess piping.

---

### da_rob

Well-written article!

I wish there was some kind of standard to tell CLI apps what features to expect from the system pager, so they can act accordingly …

Right now, apps can talk to the terminal to check for feature support, but all of that falls apart when the output is piped to a pager. (Do we support inline links? ANSI colors? Sixel support??)

Shameless plug, specifically regarding Sixel support: I needed a pager with better image support than just less -r and made [https://github.com/roblillack/lessi](https://github.com/roblillack/lessi)

> **Cthulhu_**: To be pedantic, you mean a standard like IEEE 1003 aka POSIX? ([https://pubs.opengroup.org/onlinepubs/9799919799/utilities/m...](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/more.html))

---

### ancientcatz

If I remember correctly, `gum` also provides a pager feature: [https://github.com/charmbracelet/gum](https://github.com/charmbracelet/gum)

> **netghost**: TIL about `gum`.  I love this and endeavor to integrate it into something sometime.  Thank you for mentioning it!

> > **project2501a**: Oh, you will love all of charmbracelet
> > 
> > [https://github.com/charmbracelet](https://github.com/charmbracelet)

---

### efaref

I wrote streampager a few years ago to scratch a similar itch. It works well enough for my own uses (and is/was used in library form as the built-in pager for sapling and jj).

I think it still needs some work for more general use which I unfortunately don't have time for at the moment.

---

### thegdsks

How does this compare to less with syntax highlighting? I've been using bat as a pager (bat --paging=always) and it covers most of what I need. Curious what the advantage is for larger files.

---

### vomayank

Interesting project.

What was the main limitation in existing pagers like less that pushed you to build a new one?

> **lrobinovitch**: Author here!
> 
> If I were to give this post a longer title, it would be "I made a terminal pager because I needed a really good viewport component for my Go TUIs, then realized that a TUI viewport is just a mini terminal pager and I want the same text navigation and manipulation experience everywhere that I encounter long text blocks in my terminal".
> 
> I take no issue at all with `less`, it's super powerful and configurable as I call out in the post. I took the functionality I needed, made it a reusable component for Go TUIs, then made a terminal pager in the form of a Go TUI with it.

> > **ErroneousBosh**: "Because I felt like it" is also a perfectly acceptable answer ;-)

> > **ghthor**: Still use Wander everyday <3

---

### broken-kebab

I suggest writing an intro which would answer 'why' you made it.

> **ErroneousBosh**: Why wouldn't you?

---

### pimlottc

The TL;DR doesn’t really say what this new pager offers compared to less; it seems to mostly be a learning project:

> lore supports only a subset of what less does, but in a more intuitive and useful manner for my daily activity. I also find value in understanding it from the ground up, bytes to terminal views, and continuing to refine it as I learn more about what I actually want and need in a terminal pager.

---

### gandreani

I really like this post! I think it's the clearest explanation I've seen of the different characteristics of utf-8 strings

---

### mnkyprskbd

bat is the king of pagers. [https://github.com/sharkdp/bat](https://github.com/sharkdp/bat)

> **asibahi**: Doesn’t it just call `less`?

> > **joombaga**: Yes. It calls the default pager (or whatever you specify).

> **teki_one**: bat does not look like a pager: [https://github.com/sharkdp/bat?tab=readme-ov-file#automatic-...](https://github.com/sharkdp/bat?tab=readme-ov-file#automatic-paging)

> > **teo_zero**: In fact it's not. The name itself mimicks cat, not less. It's a filter that adds annotations to its input, such as syntax highlighting, git diffs and special-char coloring.
> > 
> > Personally I can't find any use for bat: I'm a devote user of vim for editing, and it already does all of this, so why not using it to view files as well? It's satisfying to have the same interface, colors and shortcuts whether you're editing or viewing!

> **saghm**: I like it a lot more than `less`, but unfortunately it's always a lot slower when first opening really large files. I'm not sure if it's eagerly loading the whole thing (maybe because that's needed for AST parsing in the case of syntax highlighting, although it happens even on files without highlighting), but there are times I have to swap to `less` still.

---

### jzer0cool

Was curious but the git link there doesn't load?

---

### dostick

From the title I thought it’s about a dead man’s switch.

> **nkoren**: I thought it was about replicating a mossad supply chain attack.

---

### jauntywundrkind

It's not great but I made a typescript library to wrap pickers recently, such as skim, fuzzel, fzf, dmenu, rofi, etc. Some very similar problems.

Would love if anyone has thoughts or suggestions. It was quick and dirty, and works fine for my use, but I'm not sure where else I could take this, how else I might splice apart the problem, what else would suit it. [https://tangled.org/jauntywk.bsky.social/picker-power](https://tangled.org/jauntywk.bsky.social/picker-power)

---

### fragmede

A Splunk, a Splunk! My kingdom for a Splunk!

(too bad Cisco bought them and made it too expensive).

Also, no "less does more than more and most does more than less" joke?

---
