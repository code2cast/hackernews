# FIXAPL

- **Link**: https://fixapl.netlify.app/
- **HN**: https://news.ycombinator.com/item?id=47736738
- **Score**: 49 points
- **By**: tosh
- **Date**: 2026-04-12 06:36 UTC
- **Comments**: 4

---

## Comments

### electroly

I like it. Genuinely, I think APL only reuses glyphs for dramatically different monadic vs. dyadic behavior because there were limited positions available on a Selectric type ball. Many glyphs are reused as-is for multiple meanings, and they had to build some glyphs by overstriking a second glyph on top of an existing one. None of this is a concern these days.

That said, some of the reuses do make sense. ⍴ as monadic shape and dyadic reshape makes perfect sense. In FIXAPL, shape is △ and reshape is ⍴; the symbols have nothing to do with each other. I think that particular separation is a loss rather than a gain.

---

### tosh

FIXAPL is an interesting spin on APL without overloading on arity.

Many array languages overload glyphs on arity so they basically behave depending on if you call them with 1 argument (in "monadic form") vs 2 arguments ("dyadic form")

monadic: G A1

dyadic: A1 G A2

where G is the glyph and AN are arguments

The overloading can lead to confusion (but is also interesting in its own way because you can reduce the number of glyphs in the language surface).

That overloading is I would say also one of the reasons array languages might not be as approachable and one aspect of the 'difficult to read' argument.

Maybe even more important: avoiding overloading on arity helps with composition (I still have to dig into this deeper).

---

### mlajtos

This is a good idea.

Monadic/dyadic case for single glyph works nice only when you have a default value associated with it. For example `√16` is actually `2√16`. Or `log 100` is `10 log 100`. And `-3` is `0-3`.

---

### vegabook

How does typescript perform on arrays compared with BQN for example whose reference CBQN implementation extensively uses AVX / Neon?

---
