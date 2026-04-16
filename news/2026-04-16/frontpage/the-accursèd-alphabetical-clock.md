# The Accursèd Alphabetical Clock

- **Link**: https://boat.horse/clock/index.html
- **HN**: https://news.ycombinator.com/item?id=47774039
- **Score**: 44 points
- **By**: ohjeez
- **Date**: 2026-04-15 02:39 UTC
- **Comments**: 11

---

## Comments

### cbdevidal

Could someone please explain the minute hand? It says it’s Nine : Twenty-nine but the minute hand is pointing at the word Twelve.

> **nDRDY**: I think the labels are pointlessly confusing.

---

### unholiness

I love the fractal nature of this, where the big shape of one two three four... is then roughly repeated both on a slower scale (twenty thirty forty...) and on a narrower scale (twenty-one twenty-two twenty-three twenty-four...).

I'm now wondering the hausdorf dimension of the graph of alphabetical numbers <n, and how other languages might compare.

---

### gorgoiler

What a ridiculous idea.   As hard to read as it is dumb!

For a senior engineer like myself with decades of experience it is trivial to see how to fix this to make it much more readable.

1/ pick a sunny day

2/ at each hour, measure the bearing to the sun

3/ encode as a dict[str, float] e.g.

```
    {“twelve”:180.00}

```
4/ sort the hours by dict.get

Voila.

As an added bonus, for some reason this ends up sorting the minutes *and* seconds too.  (“# wtf?!”)

For now, I was only able to fix the hours when I could see the sun (eleven, twelve, and two to eight — I don’t get up very early and I like lunch).  Patches form the arctic circle welcome :P

I also need to tilt my head a bit as eleven is at the top instead of twelve.  Other than that I would say it’s a considerable improvement on the OP’s rather *naïve* implementation!  Scoff!

> **rich_sasha**: You could make either method more secure by hashing the encoded time and displaying that.
> 
> Make sure to use a cryprographically-secure hash function and a strong salt.

> **eru**: Here in Singapore on many sunny days, the bearing is largely the same hour after hour.  The sun just changes apparent altitude.

> > **fellerts**: Jam a stick in the ground aligned with the earth's axis and take your bearing from the shadow's direction. Then follow GP's instructions. Never mind that we've reinvented the sundial...

> > > **eru**: > Jam a stick in the ground aligned with the earth's axis [...]
> > > 
> > > You mean place a stick flat on the ground?  (Singapore is pretty much on the equator.)

---

### gnabgib

As a Show HN (40 points, 15 days ago, 27 comments) [https://news.ycombinator.com/item?id=47571401](https://news.ycombinator.com/item?id=47571401)

---

### alfanick

Imagine the mechanical gears behind this if it was an analogue watch. So many funky curved gears in there.

---

### throwway262515

Syntax is wildly continuous with semantics, what’s the problem?

---
