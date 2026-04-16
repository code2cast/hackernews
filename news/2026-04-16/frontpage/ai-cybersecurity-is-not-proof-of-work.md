# AI cybersecurity is not proof of work

- **Link**: https://antirez.com/news/163
- **HN**: https://news.ycombinator.com/item?id=47791236
- **Score**: 66 points
- **By**: surprisetalk
- **Date**: 2026-04-16 10:48 UTC
- **Comments**: 19

---

## Comments

### rakejake

>> Test it yourself, GPT 120B OSS is cheap and available. BTW, this is why with this bug, the stronger the model you pick (but not enough to discover the true bug), the less likely it is it will claim there is a bug.

I guess this is the crux of the debate. All the claims are comparing models that are available freely with a model that is available only to limited customers (Mythos). The problem here is with the phrase "better model". Better how? Is it trained specifically on cybersecurity? Is it simply a large model with a higher token/thinking budget? Is it a better harness/scaffold? Is it simply a better prompt?

I don't doubt that some models are stronger that other models (a Gemini Pro or a Claude Opus has more parameters, higher context sizes and probably trained for longer and on more data than their smaller counterparts (Flash and Sonnet respectively).

Unless we know the exact experimental setup (which in this case is impossible because Mythos is completely closed off and not even accessible via API), all of this is hand wavy. Anthropic is definitely not going to reveal their setup because whether or not there is any secret sauce, there is more value to letting people's imaginations fly and the marketing machine work. Anthropic must be jumping with joy at all the free publicity they are getting.

---

### dwa3592

Fighting over analogies is kind of pointless imo, but if you want me to indulge, here is what I will ask: Do you consider breadth first search better or depth first search better? - the good answer is it depends on the search surface. The same way bugs, vulnerabilities are hiding somewhere on the surface or inside(exploiting dependencies) the surface  of the software.

In conclusion - Having a lot of tokens help! Having a better model also helps. Having both helps a lot. Having very intelligent humans + a lot of tokens + the best frontier models will help the most (emphasis on intelligent human).

---

### alex_young

The whole framing is kind of uninteresting imo.  If you spend more time researching code you can find more bugs to exploit / patch is not an earthshaking observation.

Adding the words “by Claude” to it doesn’t materially change it.  One could also pay a few humans to do the same thing.  People have done that for decades.

---

### qsort

A couple of alternative scenarios, although I'm not sure how much stock we should put in them:

- what if at a certain level of capability you're essentially bug-free? I'm somewhat skeptical that this could be the case in a strong sense, because even if you formally prove certain properties, security often crucially depends on the threat model (e.g. side channel attacks, constant-time etc,) but maybe it becomes less of a problem in practice?

- what if past a certain capability threshold weaker models can substitute for stronger ones if you're willing to burn tokens? To make an example with coding, GPT-3 couldn't code at all, so I'd rather have X tokens with say, GPT 5.4, than 100X tokens with GPT-3. But would I rather have X tokens with GPT 5.4 or 100X tokens with GPT 5.2? That's a bit murkier and I could see that you could have some kind of indifference curve.

> **Leomuck**: Honestly, if every software project ran an AI-based security check over their code, the software world would probably be more secure. Of course, there are lots of projects who don't need that, having skilled people behind it, but we've seen many popular software projects (even by big companies) who didn't care at all. So even a basic model would find issues.
> 
> Also, I find myself thinking more and more that the ability to pay for tokens is becoming crucial. And it's unfair. If you don't have money, you don't have access. Somehow, a worsening of class conflicts. If you know what I mean.

> > **serial_dev**: Not only that, even if you would like to pay, the best model providers could decide any day that they want to save on cost, so they nerf the responses. Then you shipping on time is at the mercy of these companies.
> > 
> > If you spend months shipping slop, because “models will get better and tomorrow’s models can fix me today’s slop”, what happens when they not only do not get better, but actually get worse, and you are left with a bunch of slop you don’t understand and your problem solving muscles gotten weak?

---

### neutered_knot

It is also not proof of work because of asymmetries between attacker and defender. An attacker only needs to find one exploitable issue before the defender finds it and patches it, while the defender eventually needs to find all issues - and even then can't really be sure they remediated everything.

The defender also not only has to discover issues but get them deployed. Installing patches takes time, and once the patch is available, the attacker can use it to reverse engineer the exploit and use it attack unpatched systems. This is happening in a matter of hours these days, and AI can accelerate this.

It is also entirely possible that the defender will never create patches or users will never deploy patches to systems because it is not economically viable. Things like cheap IoT sensors can have vulnerabilities that don't get addressed because there is no profit in spending the tokens to find and fix flaws. Even if they were fixed, users might not know about patches or care to take the time to deploy them because they don't see it worth their time.

Yes, there are many major systems that do have the resources to do reviews and fix problems and deploy patches. But there is an enormous installed base of code that is going to be vulnerable for a long time.

---

### egormakarov

> Different LLMs executions take different branches, but eventually the possible branches based on the code possible states are saturated

With LLMs even the halting problem is just the question of paying for pro subscription!

> **dtech**: The proof of halting being unsolvable usually uses a specific "adverserial" machine. In practice it's incredibly likely for the halt question to be answerable for any specific real life program.

---

### baxtr

Interestingly enough: earlier today this discussion was trending: [https://news.ycombinator.com/item?id=47769089](https://news.ycombinator.com/item?id=47769089) (Cybersecurity looks like proof of work now)

> **RugnirViking**: the article here is pretty clearly a response to the one you posted

> > **onionisafruit**: It’s only clear if you know it exists, and now I know it exists thanks to gp.

---

### nottorp

Seriously. We need a BuSab for IT.

This continous rush is not healthy. npm updates, replies to articles that barely made HN 12 hours ago, anything like that. It's not healthy.

Slow down.

> **WesolyKubeczek**: Amtrak is slow and expensive, but the hype train is free!

---

### andersmurphy

> What happens is that weak models hallucinate (sometimes causally hitting a real problem)

So the bigger models hallucinate better causally hitting more real problems?

---

### 4qwUz

While I fully agree with the headline I find it surprising that so many people implicitly claim familiarity with the aptly named "Mythos". Mythos is closed and currently has the status of an overhyped Anduril drone that failed contact with reality in Ukraine.

If anyone has access to the mythical Mythos we'll see the contact with reality.

> **RugnirViking**: my understanding is that employees of several of the largest companies in the world get access to it atm. Those employees are overrepresented in places like HN

> > **WesolyKubeczek**: These employees may be as well under NDA, or their access may be predicated on them not sharing actual data (like Oracle and benchmarks). Anyway, you can’t verify any claims yourself, thus it might as well not exist.

---

### redwood

What seems to be getting lost in the noise on this topic is that security has always been about security in depth and mitigating controls, in other words applied paranoia. There are always threat vectors and we're seeing a change in the shape of those vectors with more rapidity than ever before which is certainly exhausting for everyone. But don't forget the fundamentals here

---
