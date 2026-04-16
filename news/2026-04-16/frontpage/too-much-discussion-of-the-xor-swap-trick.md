# Too much discussion of the XOR swap trick

- **Link**: https://heather.cafe/posts/too_much_xor_swap_trick/
- **HN**: https://news.ycombinator.com/item?id=47750486
- **Score**: 111 points
- **By**: CJefferson
- **Date**: 2026-04-13 11:22 UTC
- **Comments**: 68

---

## Comments

### pjc50

The fun bit is right at the start when the author notices that the compiler spots this and optimizes it away.

We didn't get into the deeper question of benchmarking it vs. a three-register swap, because I suspect the latter would be handled entirely by register renaming and end up being faster due to not requiring allocation of an ALU unit. Difficult to benchmark that because in order for it to make a difference, you'd need to surround it with other arithmetic instructions.

A meta question is why this persists. It has the right qualities for a "party trick": slightly esoteric piece of knowledge, not actually that hard to understand when you do know about it, but unintuitive enough that most people don't spontaneously reinvent it.

See also: [https://en.wikipedia.org/wiki/Fast_inverse_square_root](https://en.wikipedia.org/wiki/Fast_inverse_square_root) , which requires a bit more maths.

The other classic use of XOR - cursor overdrawing - has also long since gone away. It used to be possible to easily draw a cursor on a monochrome display by XORing it in, then to move it you simply XOR it again, restoring the original image.

> **jcalvinowens**: The "party trick" is more general than just xor, for example:
> 
> ```
>     void swap(unsigned* a, unsigned* b)
>     {
>         *a = *a + *b;
>         *b = *a - *b;
>         *a = *a - *b;
>     }
> 
> ```
> GCC still sees through it with restrict: [https://godbolt.org/z/8n3bGha3e](https://godbolt.org/z/8n3bGha3e)

> **jimjag**: You can even do it with complex images in a multi-color bitmap. I do it with my 6502 SBC setup: [https://github.com/jimjag/JJ65c02/blob/main/Software/pico-co...](https://github.com/jimjag/JJ65c02/blob/main/Software/pico-code/pico_core/vga_graphics.c)

> **vidarh**: The cursor overdrawing trick in part started going away before it's time thanks to patent enforcement (one of the lawsuits infamously exacerbated Commodores financial woes towards the end)... By the time the patent expired there was really no longer much value in going back to it.

---

### danhau

> Are there other XOR tricks?

Yes, error correction.

You have some packets of data a, b, c. Add one additional packet z that is computed as z = a ^ b ^ c. Now whenever one of a, b or c gets corrupted or lost, it can be reconstructed by computing the XOR of all the others.

So if b is lost: b = a ^ c ^ z. This works for any packet, but only one. If multiple are lost, this will fail.

There are way better error correction algorithms, but I like the simplicity of this one.

> **throwaway2027**: [https://en.wikipedia.org/wiki/XOR_linked_list](https://en.wikipedia.org/wiki/XOR_linked_list)

> **amelius**: XOR is also great for storing copyrighted works without liability.
> 
> a = the bits of some song or movie
> 
> b = pure noise
> 
> Store c = a^b.
> 
> Give b to a friend. Throw away a.
> 
> Now both you and your friend have a bit vector of pure noise. Together you can produce the copyrighted work. But nobody is liable.

> > **aleph_minus_one**: This is the "What Colour are your bits?" argument:
> > 
> > > [https://ansuz.sooke.bc.ca/entry/23](https://ansuz.sooke.bc.ca/entry/23)
> > 
> > > [https://ansuz.sooke.bc.ca/entry/24](https://ansuz.sooke.bc.ca/entry/24)
> > 
> > As these article outline, the legal situation is much more complicated (and unintuitive to people who are used to "computer science thinking").

> > > **amelius**: This is because legal people want something to exist that does not physically exist.
> > > 
> > > There is no trace back from pure noise to the original work.
> > > 
> > > Colour of bits is just magical thinking.

> > **nkrisc**: Crimes aren’t legal just because you hide it. Intent matters.
> > 
> > Law is more akin to philosophy than computer science.

> > **pjc50**: Whether people are liable is a question for the courts, and I suspect they simply look through the tech and ask "do you end up with a copy of the work?"
> > 
> > (unless you're an AI company, in which case you can copy the whole internet just fine)

> > > **amelius**: But that's an unsolvable question. Just like when A is caught on camera stealing a diamond, but A turns out to have an identical twin B. So the prosecutor can't do anything.

> > **lelanthran**: That's called encryption using a one time pad.

> > > **amelius**: That's one way of looking at it. Note that you can easily extend it to multiple people holding multiple keys, so that a=b^c^d^e, etc.

> > **meindnoch**: Pretty sure the law doesn't care about this XOR trick.

> **direwolf20**: Important note: Only if you already know which one was corrupted.

> **nsteel**: Also to cheaply (area) create multi-port RAMs.

> > **pjc50**: How does that work?

> > > **nsteel**: It's similar to RAID schemes but instead of drive failure it's port unavailability. There's a reference at [1] or an FPGA-centric one at [2], but it applies to anywhere where dual/single-port rams are readily available but anything more exotic isn't.
> > > 
> > > ```
> > >   [1] Achieving Multi-Port Memory Performance on Single-Port Memory with Coding Techniques - https://arxiv.org/abs/2001.09599
> > >   [2] https://people.csail.mit.edu/ml/pubs/fpga12_xor.pdf
> > > ```

> **Terr_**: See also: RAID levels that use one disk for parity. Three disks is simplest, but technically you can do more if you trust that only one will go bad at a time.
> 
> A few months ago, I had a rare occasion of trying to explain them to a relative who had just bought a fancy NAS and wanted help setting it up.

---

### pcherna

On the Amiga, accessing the pulldown menus caused the display to be temporarily frozen, so that the menu panel could be rendered off screen and then swapped in using the blitter and the XOR trick. It wasn’t as fast as a straight copy, but it saved on precious memory, and it rendered very cleanly.

When you released to the menu button on the mouse, it did a similar swap to restore the screen contents. In version 2.0 I optimized it to do a simple copy of the offscreen rectangle back onto the screen because before it was wasting time in order to preserve the menu pixels that we’re going to be thrown away immediately.

---

### gobdovan

The XOR trick is only cool in its undefined-behavior form:

a^=b^=a^=b;

Which allegedly saves you 0.5 seconds of typing in competitive programming competitions from 20 years ago and is known to work reliably (on MinGW under Windows XP).

Bonus authenticity: use `a^=a` to zero a register in a single x86 instruction (and makes a real difference for compiler toolchains 30+ years old).

For real now, a very useful application of XOR is its relation to the Nim game [0], which comes in very handy if you need to save your village from an ancient disgruntled Chinese emperor.

[0] [https://en.wikipedia.org/wiki/Nim](https://en.wikipedia.org/wiki/Nim)

> **MathMonkeyMan**: `xor eax, eax` is less code when assembled. That's why compilers generate it.

> > **gobdovan**: ..and reliably generate it for decades, but you can still manually do it in C for bonus stylistic points!

> **leni536**: > The XOR trick is only cool in its undefined-behavior form:
> 
> > a^=b^=a^=b;
> 
> I believe this is defined in C++ since C++17, but still undefined in C.

> **ginko**: >Bonus authenticity: use `a^=a` to zero a register in a single x86 instruction (and makes a real difference for compiler toolchains 30+ years old).
> 
> Modern compilers will still use xor for zeroing registers on their own.
> 
> For instance: [https://godbolt.org/z/n5n35xjqx](https://godbolt.org/z/n5n35xjqx)
> 
> Variable a(register esi) is first initialized to 42 with mov and then cleared to zero using xor.

> > **gobdovan**: Yes, the whole comment is tongue in cheek for pointless manual optimizations.

---

### JKCalhoun

My assumption has been that the XOR trick was closer to a *thought experiment* or *hypothetical*. That is to say, no one would ever use it in practice, but by asking an interviewee to walk through it shows they have a low-level understanding of how binary numbers work, bit-masking.

For me it falls in the *obfuscated-C* quadrant for code. Performance implications aside, it's just not the kind of "self-documenting" code I like lying around in my sources. (And I'll take clarity of purpose over performance every day.)

---

### mmozeiko

xor swap trick was useful in older simd (sse1/sse2) when based on some condition you want to swap values or not:

```
  tmp = (a ^ b) & mask
  a ^= tmp
  b ^= tmp

```
If mask = 0xfff...fff then a/b will be swapped, otherwise if mask = 0 then they'll remain the same.

> **CJefferson**: Oh, that is cool, I’ve never seen that. I might add that to an extended version of the post sometime, I’ll be sure to credit you.

> **jagged-chisel**: So mask is marking the bits you want swapped and leaving the others in place.

> **koolala**: Could this still be the ideal way for vectors of Ints in WebGL2?

> **jesse__**: That's hella cute

---

### HarHarVeryFunny

> Are there other XOR tricks?

I'm not sure I'd call it a "trick", but since A ^ 0 = A, and B ^ B = 0, then ((A ^ B) ^ B) = A. i.e. XOR-ing any number by the same number twice gets you back the original number.

This used to be used back in the day for cheap and nasty computer graphics, since it means that if you draw to the screen by XOR-ing with the pixels already on the screen then you can undo it, restoring the background, by doing it a second time. The "nasty" part is that XORing with what's already on the screen isn't going to look great, but for something like a rotating wire-frame figure it might be OK.

---

### fuglede_

The XOR swap trick also features in the compilation/synthesis of quantum algorithms, where the XOR instruction (in the form of a CNOT gate) is fundamental in many architectures, and where native swapping need not be available.

One extension that I ran into, and which I think forms a nice problem is the following:

Just like the XOR swap trick can be used to swap to variables (and let's just say that they're bools), it can be extended to implement any permutation of the variables: suppose that the permutation is written as a composition of  n transpositions (i.e., swaps of pairs), and that  is the minimal number of transpositions that let's you do that. Each transposition can be implemented by 3 XORs, by the XOR swap trick for pairs, and so the full permutation can be implemented by 3n XORs. Now here's the question: Is it possible to come up with a way of doing it with less than 3n, or can we find a permutation that has a shortcut through XOR-land (not allowing any other kinds of instructions)? In other words, is XOR-swapping XOR-optimal?

I'm not going to spoil it, but only last year a paper was published in the quantum information literature that contains an answer [0]. I ended up making a little game where you get to play around with XOR-optimizing not only permutations, but general linear reversible circuits. [1]

[0] [https://link.springer.com/article/10.1007/s11128-025-04831-5](https://link.springer.com/article/10.1007/s11128-025-04831-5)

[1] [https://swapple.fuglede.dk](https://swapple.fuglede.dk)

---

### praptak

Xor swap trick has perfect profile for underhanded C contests. It generally works until a specific condition triggers its failure. The condition is "the arguments are aliases", so for example XOR_SWAP(a[i], a[j]) when i=j.

> **imploded_sub**: TFA mentions this as an issue for the trick, whereas you rightly point out it's an evil feature instead.

---

### Panzerschrek

Such tricks were maybe useful 40 years ago while writing assembly code manually or while using a dumb compiler with no optimizations. But nowadays such tricks are near to useless. All useful ones (like optimizing division by 2 via bitshift ) are already implemented as compiler optimizations. Others shouldn't be used in order to avoid making optimizer's job harder.

> **Tade0**: Back when I was in college in the late 00s we were advised to not attempt to optimise using assembly unless we really found a bottleneck the compiler missed.

> > **pjc50**: Correct. There are still some situations that benefit from it, but only using the extended instruction sets that compilers can't/won't generate. Even then you should at least try writing the C code and seeing if it will auto-vectorize. Even C# can auto-vectorize some cases now.
> > 
> > Things like "add with saturation" and the special AES instructions.

> > > **jesse__**: In my experience, relying on the compiler to auto vectorize your code is a path fraught with peril.
> > > 
> > > It'll break eventually.  If it matters, write the simd yourself.  It'll probably be 2-50x better than the compiler anyways.

---

### fch42

xor'ing the elements of lists together also allows a test of "unordered equality" because 1^2^3^4^5 == (xor of any permutation of [1,2,3,4,5]).

Yes there are false positives, and the false negative of all-zero/all-equal, but the test can be useful in a "bloom filter" type case.

Have used it in dynamic firewalling rules ... one can do something pretty close to a JA3/JA4 TLS fingerprint in eBPF with that (to match the cipher lists).

---

### robinsonb5

This brings back memories of Chunky-to-Planar conversion on the Amiga, where the Xor trick was combined with bitshifts and masking to rearrange the bits in 8 32-bit words in reasonable time.

---

### torginus

I would remark that modern CPUs don't use physical registers, so swapping should be just a register rename op, and this kind of bithacking only applies to old machines.

The article makes the same point as well at the end:

It is the kind of technique which might have been occasionally useful in the 1980s, but now is only useful for cute interview questions and as a curiosity.

---

### YasuoTanaka

Used to do this in assembly back when registers actually mattered. Today it mostly hurts readability more than anything.

---

### pjmlp

Another trick when SIMD is not available, is pseudo SIMD via SWAR, one example,

[https://lemire.me/blog/2022/01/21/swar-explained-parsing-eig...](https://lemire.me/blog/2022/01/21/swar-explained-parsing-eight-digits/)

---
