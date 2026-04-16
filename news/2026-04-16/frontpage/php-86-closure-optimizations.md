# PHP 8.6 Closure Optimizations

- **Link**: https://wiki.php.net/rfc/closure-optimizations
- **HN**: https://news.ycombinator.com/item?id=47763959
- **Score**: 26 points
- **By**: moebrowne
- **Date**: 2026-04-14 10:59 UTC
- **Comments**: 4

---

## Comments

### kevincox

It is an interesting comparison that JavaScript always ensures that different evaluations of a closure expression results in unique instances. So in general the closures will require allocations for each (unless the allocation is otherwise prevented such as via escape analysis). Of course much of the underlying data may be shared, but the identity itself will be unique.

I don't know how strict JavaScript garbage collection rules are. This was non-observable for the longest time but FinalizationRegistry now exists which makes cleanup observable. It sounds like basically no guarantees are provided when an object will be cleaned up, so presumably an implementation would be allowed to make optimizations such are proposed where for PHP.

---

### moebrowne

> Non-static closures are turned into static ones if they are guaranteed not to make use of $this.

> Stateless closures, i.e. those that are static, don't capture any variables and don't declare any static variables, are cached between uses.

---

### hyperionultra

~3% performance gains. I didn’t understood part about $this.

> **rererereferred**: If the closure doesn't use $this (an instance of the current class) then it doesn't need to store a reference to it, which also skips the bookkeeping from the garbage collector.

---
