# Cybersecurity looks like proof of work now

- **Link**: https://www.dbreunig.com/2026/04/14/cybersecurity-is-proof-of-work-now.html
- **HN**: https://news.ycombinator.com/item?id=47769089
- **Score**: 488 points
- **By**: dbreunig
- **Date**: 2026-04-14 18:08 UTC
- **Comments**: 181

---

## Comments

### j2kun

The article heavily quotes the "AI Security Institute" as a third-party analysis. It was the first I heard of them, so I looked up their about page, and it appears to be primarily people from the AI industry (former Deepmind/OpenAI staff, etc.), with no folks from the security industry mentioned. So while the security landscape is clearly evolving (cf. also Big Sleep and Project Zero), the conclusion of "to harden a system we need to spend more tokens" sounds like yet more AI boosting from a different angle. It raises the question of why no other alternatives (like formal verification) are mentioned in the article or the AISI report.

I wouldn't be surprised if NVIDIA picked up this talking point to sell more GPUs.

> **tptacek**: I would be interested in which notable security researchers you can find to take the other side of this argument. I don't know anything about the "AI Security Institute", but they're saying something broadly mirrored by security researchers. From what I can see, the "debate" in the actual practitioner community is whether frontier models are merely as big a deal as fuzzing was, or something signficantly bigger. Fuzzing was a *profound* shift in vulnerability research.
> 
> (Fan of your writing, btw.)

> > **j2kun**: It's less that I think they would take the other side of the argument, than that they would lend some credence to the content of the analysis. For example, I would not particularly trust a bunch of AI researchers to come up with a representative set of CTF tasks, which seems to be the basis of this analysis.

> > > **tptacek**: Yeah, you might be right about this particular analysis! The sense I have from talking to people at the labs is that they're really just picking deliberately diverse and high-profile targets to see what the models are capable of.

> > **VorpalWay**: > but they're saying something broadly mirrored by security researchers.
> > 
> > You might well be right, it is not an area I know much of or work in. But I'm a fan of reliable sources for claims. It is far to easy to make general statements on the internet that appear authorative.

> **croemer**: They are a UK government unit: "The AI Security Institute is a research organisation within the Department of Science, Innovation and Technology."
> 
> Unfortunately, they fit straight lines to graphs with y axis from 0 to 100% and x axis being time - which is not great. Should do logistic instead.

> **wg0**: If true, that's naked, shameless and brutal capitalism.
> 
> Seems much like those secretly tobacco industry funded reports about tobacco being safe and such.

---

### somesortofthing

There's still the question of access to the codebase. By all accounts, the best LLM cyber scanning approaches are *really* primitive - it's just a bash script that goes through every single file in the codebase and, for each one and runs a "find the vulns here" prompt. The attacker usually has even less access than this - in the beginning, they have network tools, an undocumented API, and maybe some binaries.

You can do a lot better efficiency-wise if you control the source end-to-end though - you already group logically related changes into PRs, so you can save on scanning by asking the LLM to only look over the files you've changed. If you're touching security-relevant code, you can ask it for more per-file effort than the attacker might put into their own scanning. You can even do the big bulk scans an attacker might on a fixed schedule - each attacker has to run their own scan while you only need to run your one scan to find everything they would have. There's a *massive* cost asymmetry between the "hardening" phase for the defender and the "discovering exploits" phase for the attacker.

Exploitability also isn't binary: even if the attacker is better-resourced than you, they need to find a whole chain of exploits in your system, while you only need to break the weakest link in that chain.

If you boil security down to just a contest of who can burn more tokens, defenders get efficiency advantages only the best-resourced attackers can overcome. On net, public access to mythos-tier models will make software more secure.

> **anitil**: On that latest episode of 'Security Cryptography Whatever' [0] they mention that the time spent on improving the harness (at the moment) end up being outperformed by the strategy of "wait for the next model". I doubt that will continue, but it broke my intuition about how to improve them
> 
> [0] [https://securitycryptographywhatever.com/2026/03/25/ai-bug-f...](https://securitycryptographywhatever.com/2026/03/25/ai-bug-finding/)

> > **conception**: This is basically how you should treat all AI dev. Working around AI model limits for something that will take 3-6 months of work has very little ROI compared to building what works today and just waiting and building what works tomorrow tomorrow.

> > > **thephyber**: This assumes AI model improvements will be predictable, which they won’t.
> > > 
> > > There are several simultaneous moving targets: the different models available at any point in time, the model complexity/ capability, the model price per token, the number of tokens used by the model for that query, the context size capabilities and prices, and even the evolution of the codebase. You can’t calculate comparative ROIs of model A today or model B next year unless these are far more predictable than they currently are.

> > > **sally_glance**: This is the hard part - especially with larger initiatives, it takes quite a bit of work to evaluate what the current combination of harness + LLM is good at. Running experiments yourself is cumbersome and expensive, public benchmarks are flawed. I wish providers would release at least a set of blessed example trajectories alongside new models.
> > > 
> > > As it is, we're stuck with "yeah it seems this works well for bootstrapping a Next.js UI"...

> > **jorvi**: That seems very unlikely.
> > 
> > Chinese AI vendors specifically pointed out that even a few gens ago there was maybe 5-15% more capability to squeeze out via training, but that the cost for this is extremely prohibitive and only US vendors have the capex to have enough compute for both inference and that level of training.
> > 
> > I'd take their word over someone that has a vested interested in pushing Anthropic's latest and greatest.
> > 
> > The real improvements are going to be in tooling and harnessing.

> > **theptip**: It’s a good thing to keep in mind, but LLM + scaffolding is clearly superior. So if you just use vanilla LLMs you will always be behind.
> > 
> > I think the important thing is to avoid over-optimizing. Your scaffold, not avoid building one altogether.

> > > **fragmede**: It's wild to me that a paragraph or 7 of plain English that amounts to "be good at things" is enough to make a material difference in the LLM's performance.

> > **Kinrany**: That only applies to workarounds for current limitations, no? Some things a harness can do will apply in the same way to future models.

> > **yorwba**: I think you took away the wrong lesson from that podcast:
> > 
> > *I think there is work to be done on scaffolding the models better. This exponential right now reminds me of the exponential from CPU speeds going up until let’s say 2000 or something where you had these game developers who would develop really impressive games on the current thing of hardware and they do it by writing like really detailed intricate x86 instruction sequences for like just exactly whatever this, like, you know, whatever 486 can do, knowing full well that in 2 years, you know, the pen team is gonna be able to do this much faster and they didn’t need to do it. But like you need to do it now because you wanna sell your game today and like, yeah, you can’t just like wait and like have everyone be able to do this. And so I do think that there definitely is value in squeezing out all of the last little juice that you can from the current model.*
> > 
> > Everything you can do today will *eventually* be obsoleted by some future technology, but if you need better results *today*, you actually have to do the work. If you just drop everything and wait for the singularity, you're just going to unnecessarily cap your potential in the meantime.

> > **argee**: >  it broke my intuition about how to improve them
> > 
> > Here we go again.
> > 
> > [http://www.incompleteideas.net/IncIdeas/BitterLesson.html](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)

> > **bitexploder**: And if you have the better harness and the next model?

> > > **anitil**: I would _hope_ that the double combo would be better, but honestly I have no idea

> **btown**: The problem, though, is that this turns "one of our developers was hit by a supply chain attack that never hit prod, we wiped their computer and rotated keys, and it's not like we're a big target for the attacker to make much use of anything they exfiltrated..." into "now our entire source code has been exfiltrated and, even with rudimentary line-by-line scanning, will be automatically audited for privilege escalation opportunities within hours."
> 
> Taken to an extreme, the end result is a dark forest. I don't like what that means for entrepreneurship generally.

> > **linkregister**: This is a great example of vulnerability chains that can be broken by vulnerability scanning by even cheaper open source models. The outcome of a developer getting pwned doesn't have to lead to total catastrophe. Having trivial privilege escalations closed off means an attacker will need to be noisy and set off commodity alerting. The will of the company to implement fixes for the 100 Github dependabot alerts on their code base is all that blocks these entrepreneurs.
> > 
> > It does mean that the hoped-for 10x productivity increase from engineers using LLMs is eroded by the increased need for extra time for security.
> > 
> > This take is not theoretical. I am working on this effort currently.

> > > **pixl97**: I disagree that it's extra time for security,  it's the time we should have been spending in the first place.

> > > **fragmede**: It's great news for developers. Extra spend on a development/test env so dev have no prod access, prod has no ssh access; and SREs get two laptops, with the second one being a Chromebook that only pulls credentials when it's absolutely necessary.

> > **eru**: > Taken to an extreme, the end result is a dark forest.
> > 
> > Sorry, how does that work?

> > > **bryanrasmussen**: since the suggestion is that the new security bug finding LLMs will increase protection because it will have access to the full source code then, the dark forest fear would be, if it is possible for an attacker to get all the source the attacker will be in a better position.
> > > 
> > > This seems wrong however, as it ignores the arrow of time. The full source code has been scanned and fixed for things that LLMs can find before hitting production, anyone exfiltrating your codebase can only find holes in stuff with their models that is available via production for them to attack and that your models for some reason did not find.
> > > 
> > > I don't think there is any reason to suppose non-nation state actors will have better models available to them and thus it is not a dark forest, as nation states will probably limit their attacks to specific things, thus most companies if they secure their codebase using LLMs built for it will probably be at a significantly more secure position than nowadays and, I would think, the golden age of criminal hacking is drawing to a close. This assume companies smart enough to do this however.
> > > 
> > > Furthermore, the worry about nation state attackers still assumes that they will have better models and not sure if that is likely either.

> **xeyownt**: One defender, many attackers, I don't see how the economy of scale can be positive for the defender.
> 
> Assuming your code is inaccessible isn't good for security. All security reviews are done assuming code source is available. If you don't provide the source, you'll never score high in the review.

> **tossandthrow**: > it's just a bash script that goes through every single file in the codebase and, for each one and runs a "find the vulns here" prompt.
> 
> This really is not the case.
> 
> You have freedom of methodology.
> 
> You can also ask it to enumerate various risks and find proof of existence for each of them.
> 
> Certainly our LLM audits are not just a prompt per file - so I have a hard time believing that best in class tools would do this.

> > **pseudohadamard**: I've actually had pretty good results from doing exactly that.  There was one FP when it tried to be Coverity and failed miserably, but the others were "you need to look at this bit more closely", and in most cases there was something there.  Not necessarily a vuln but places where the code could have been written more clearly.  It was like having your fourth grade English teacher looking over your shoulder and saying "you need to look at the grammar in this sentence more closely".
> > 
> > And using an LLM to audit your code isn't necessarily a case of turning it into perfect code, it's to keep ahead of the other side also using an LLM.  You don't need to outrun the bear, just the other hikers.

> **eru**: > There's a massive cost asymmetry between the "hardening" phase for the defender and the "discovering exploits" phase for the attacker.
> 
> Well, you need to harden everything, the attacker only needs to find one or at most a handful of exploits.

> > **lelanthran**: > Well, you need to harden everything, the attacker only needs to find one or at most a handful of exploits.
> > 
> > Yeah, but it's not like the attacker *knows* where to look without checking everything, it it?
> > 
> > If you harden and fix 90% of vulns, the attacker may give up when their attempts reach 80% of vulns.
> > 
> > It's the same as it has ever been; you don't need to outrun the bear, you only need to outrun the other runners.

> > > **eru**: Compare and contrast [https://en.wikipedia.org/wiki/Kerckhoffs%27s_principle](https://en.wikipedia.org/wiki/Kerckhoffs%27s_principle)

> **lmeyerov**: Most companies and their vendor ecosystems run on OSS
> 
> Worse, "attackers no longer break in, they log in", so the supply chain attacks harvesting credentials have been frightening

> **nl**: > By all accounts, the best LLM cyber scanning approaches are really primitive - it's just a bash script that goes through every single file in the codebase
> 
> What accounts are these?
> 
> I've seen some people use this but I cannot imaging that anyone thinks this is the best.
> 
> For example I've had success telling LLMs to scan from application entry points and trace execution, and that seems an extremely obvious thing to do. I can't imagine others in the field don't have much better approaches.

> **ozim**: Still it makes cost of making software higher.
> 
> You cannot get away with „well no one is going to spend time writing custom exploit to get us” or „just be faster than slowest running away from the bear”.

> **chrisjj**: > By all accounts, the best LLM cyber scanning approaches are really primitive - it's just a bash script that goes through every single file in the codebase and, for each one and runs a "find the vulns here" prompt
> 
> Primitive? I'd say simple and thorough.

> **Retr0id**: Tokens can also be burnt on decompilation.

> > **tptacek**: Yes, and it apparently burns *lots* of tokens. But what I've heard is that the outcomes are drastically less expensive than hand-reversing was, when you account for labor costs.

> > > **jeffmcjunkin**: Can confirm. Matching decompilation in particular (where you match the compiler along with your guess at source, compile, then compare assembly, repeating if it doesn't match) is very token-intensive, but it's now very viable: [https://news.ycombinator.com/item?id=46080498](https://news.ycombinator.com/item?id=46080498)
> > > 
> > > Of course LLMs see a lot more source-assembly pairs than even skilled reverse engineers, so this makes sense. Any area where you can get unlimited training data is one we expect to see top-tier performance from LLMs.
> > > 
> > > (also, hi Thomas!)

> > > **gfosco**: Yeah, it's token intensive but worth it.  I built a very dumb example harness which used IDA via MCP and analyzed/renamed/commented all ~67k functions in a binary, using Claude Haiku for about $150.  A local model could've accomplished it for much less/free.  The knowledge base it outputs and the marked up IDA db are super valuable.

> > **somesortofthing**: Another asymmetric advantage for defenders - attackers need to burn tokens to form incomplete, outdated, and partially wrong pictures of the codebase while the defender gets the whole latest version plus git history plus documentation plus organizational memory plus original authors' cooperation for free.

> > > **high_na_euv**: >original authors' cooperation
> > > 
> > > Ha
> > > 
> > > >for free.
> > > 
> > > Haha, it is more complicated in reality

> > **echelon**: > Tokens can also be burnt on decompilation.
> > 
> > Prediction 1. We're going to have cheap "write Photoshop and AutoCad in Rust as a new program / FOSS" soon. No desktop software will be safe. Everything will be cloned.
> > 
> > Prediction 2. We'll have a million Linux and Chrome and other FOSS variants with completely new codebases.
> > 
> > Prediction 3. People will trivially clone games, change their assets. Modding will have a renaissance like never before.
> > 
> > Prediction 4. To push back, everything will move to thin clients.

> > > **jgraham**: I think if prediction 1 is true (that it becomes cheap to clone existing software in a way that doesn't violate copyright law), the response will not be purely technical (moving to thin clients, or otherwise trying to technically restrict the access surface to make reverse engineering harder). Instead I'd predict that companies look to the law to replace the protections that they previously got from copyright.
> > > 
> > > Obvious possibilities include:
> > > 
> > > * More use of software patents, since these apply to underlying ideas, rather than specific implementations.
> > > 
> > > * Stronger DMCA-like laws which prohibit breaking technical provisions designed to prevent reverse engineering.
> > > 
> > > Similarly, if the people predicting that humans are going to be required to take ultimate responsibility for the behaviour of software are correct, then it clearly won't be possible for that to be any random human. Instead you'll need legally recognised credentials to be allowed to ship software, similar to the way that doctors or engineers work today.
> > > 
> > > Of course these specific predictions might be wrong. I think it's fair to say that nobody really knows what might have changed in a year, or where the technical capabilities will end up. But I see a lot of discussions and opinions that assume zero feedback from the broader social context in which the tech exists, which seems like they're likely missing a big part of the picture.

> **bryanrasmussen**: >By all accounts, the best LLM cyber scanning approaches are really primitive
> 
> It seems like that is perhaps not the case anymore with the Mythos model?

> **kelvinjps10**: what about open source software?

---

### antirez

Why this is the wrong analogy: finding hash collisions, while exponentially harder with N, is *guaranteed* to find, with enough work, some S so that H(S) satisfies N, so an asymmetry of resources used will have the side with more work eventually winning. But bugs are different: 1. different LLMs executions take different branches, but eventually the branches possible based on the code possible states are saturated. 2. if we imagine sampling the model for a bug in a given code M times, with M large, eventually the cap becomes not M (because of saturated state so of the code and the LLM sampler) but I, the model intelligence level. The OpenBSD SACK bug easily shows that: you can run an inferior model for an infinite number of times, it will never realize that the lack of validation of the start window *if* put together with the integer overflow *then* put together with the fact the branch where the node should never be NULL is entered produce the bug. So cyber security of tomorrow will not be like proof of work "more GPU wins", but better models and faster access to such models win.

> **fhd2**: Agreed, it is different in terms of there being no guarantee that a specific piece of software even has an exploit. If you don't want to break into a specific piece of software, or even a specific system, I would argue that the law of averages applies: If you just invest enough, you'll likely find _something_ worth exploiting.
> 
> In other terms, I feel the argument from TFA generally checks out, just on a different level than "more GPU wins". It's one up: "More money wins". That's based on the premise that more capable models will be more expensive, and using more of it will increase the likelihood of finding an exploit, as well as the total cost. What these model providers pay for GPUs vs R&D, or what their profit margin is, I'd consider less central.
> 
> But then again, AI didn't change this, if you have more money you can find more exploits: Whether a model looks for them or a human.

---

### nostrademons

Relevant Tony Hoare quote: “There are two approaches to software design: make it so simple there are obviously no deficiencies, or make it so complex there are no obvious deficiencies”.

> **tekacs**: I think this is so relevant, and thank you for posting this.
> 
> Of course it's *trivially* NOT true that you can defend against all exploits by making your system sufficiently compact and clean, but you can certainly have a big impact on the exploitable surface area.
> 
> I think it's a bit bizarre that it's implicitly assumed that all codebases are broken enough, that if you were to attack them sufficiently, you'll eventually find endlessly more issues.
> 
> Another analogy here is to fuzzing. A fuzzer can walk through all sorts of states of a program, but when it hits a password, it can't really push past that because it needs to search a space that is impossibly huge.
> 
> It's all well and good to try to exploit a program, but (as an example) if that program _robustly and very simply_ (the hard part!) says... that it only accepts messages from the network that are signed before it does ANYTHING else, you're going to have a hard time getting it to accept unsigned messages.
> 
> Admittedly, a lot of today's surfaces and software were built in a world where you could get away with a lot more laziness compared to this. But I could imagine, for example, a state of the world in which we're much more intentional about what we accept and even bring _into_ our threat environment. Similarly to the shift from network to endpoint security. There are for sure, uh, million systems right now with a threat model wildly larger than it needs to be.

> > **slow_typist**: Problem is, the way economic activity is organised in general, there is no transition path from complex bloated systems to well designed completely human auditable systems. For example given the inherent (and proven) security risks of the Wordpress ecosystem, nobody should run WP anymore.

> > > **PunchyHamster**: I'd hazard a guess 90% of WP instances could be replaced by static site generator + some tiny app to handle forms, and the 9/10th of remaining ones with static gen + form + some external commenting system, whether in cloud or something like commento.

> **self_awareness**: The question is what "complex" means. Complex for us doesn't mean it's complex for LLM. And vice-versa. So I wouldn't value this approach at all.

> > **misja111**: I disagree. Much of what makes software complex for us, makes it complex for LLM just as well. E.g:
> > 
> > - a very large codebase
> > 
> > - a codebase which is not modularized into cohesive parts
> > 
> > - niche languages or frameworks
> > 
> > - overly 'clever' code

> > > **xeyownt**: Yeah, the main problem is that most companies / people don't give a f*ck about security because it is not a key feature. It's only a marketing stamp. You want it good enough to sell the products, but you don't want to spent too much on it. So instead you go vibe coding. The baby is dead born.

---

### jzelinskie

Security has always been a game of just how much money your adversary is willing to commit. The conclusions drawn in lots of these articles are just already well understood systems design concepts, but for some reason people are acting like they are novel or that LLMs have changed anything besides the price.

For example from this article:

> Karpathy: Classical software engineering would have you believe that dependencies are good (we’re building pyramids from bricks), but imo this has to be re-evaluated, and it’s why I’ve been so growingly averse to them, preferring to use LLMs to “yoink” functionality when it’s simple enough and possible.

Anyone who's heard of "leftpad" or is a Go programmer ("A little copying is better than a little dependency" is literally a "Go Proverb") knows this.

Another recent set of posts to HN had a company close-sourcing their code for security, but "security through obscurity" has been a well understand fallacy in open source circles for decades.

> **lelanthran**: > Another recent set of posts to HN had a company close-sourcing their code for security, but "security through obscurity" has been a well understand fallacy in open source circles for decades.
> 
> I dunno about that quoted bit; "Defense in depth" (Or defense via depth) is a *good* thing, and obscurity is just one of those layers.
> 
> "Security through obscurity" is indeed wrong if the obscurity is a large component of the security, but it *helps* if it is just another layer of defense in the stack.
> 
> IOW, harden your system as if it were completely transparent, and only *then* make it opaque.

> **alexwebb2**: > "security through obscurity" has been a well understand fallacy in open source circles for decades
> 
> The times, as they say, are a-changin’.
> 
> Open software is not inherently more secure than closed software, and never has been.
> 
> Its relative security value was always derived from circumstantial factors, one of the most important of which was the combination of incentive and ability and willingness of others in the community to spend their time and attention finding and fixing bugs and potential exploits.
> 
> Now, that’s been the case for so long that we all implicitly take it for granted, and conclude that open software is generally more secure than closed, and that security through obscurity falls short in comparison.
> 
> But this may very well fundamentally change when the cost of navigating the search space of potential exploits, for both the attacker and the defender, is dramatically reduced along the axes of time and attention, and increased along the axis of monetary investment.
> 
> It then becomes a game of which side is more willing to pool monetary resources into OSS security analysis – the attackers or the defenders – and I wouldn’t feel comfortable betting on the defenders in that case.

> **pmontra**: Yes, there is nothing novel in "to harden a system we need to spend more tokens discovering exploits than attackers spend exploiting them." That's what security always looked like, physical security included (burglars, snipers, etc.) So when AI is available you have to throw more AI at securing your system than your adversaries do. What a surprise.
> 
> Maybe we could start with the prompts for the code generation models used by developers.

---

### creatonez

I mostly agree with the article.

> You don’t get points for being clever

Not sure about this framing, this can easily lead to the wrong conclusions. There is an arms race, yes, and defenders are going to need to spend a lot of GPU hours as a result. But it seems self-evident that the fundamentals of cybersecurity still matter a lot, and you still win by being clever. For the foreseeable future, security posture is still going to be a reflection of human systems. Human systems that are under enormous stress, but are still fundamentally human. You win by getting your security culture in order to produce (and continually reproduce) the most resilient defense that masters both the craft and the human element, not just by abandoning human systems in favor of brute forcing security problems away as your only strategy.

Indeed, domains that are truly security critical will acquire this organizational discipline (what's required is the same type of discipline that the nuclear industry acquires after a meltdown, or that the aviation industry acquires after plane crashes), but it will be a bumpy ride.

This article from exactly 1 year ago is almost prophetic to exactly what's going on right now *and* the subtle ways in which people are most likely to misunderstand the situation: [https://knightcolumbia.org/content/ai-as-normal-technology](https://knightcolumbia.org/content/ai-as-normal-technology)

---

### dataviz1000

> to harden a system you need to spend more tokens discovering exploits than attackers will spend exploiting them.

I, for the NFL front offices, created a script that exposed an API to fully automate Ticketmaster through the front end so that the NFL could post tickets on all secondary markets and dynamic price the tickets so if rain on a Sunday was expected they could charge less. Ticketmaster was slow to develop an API. Ticketmaster couldn't provide us permission without first developing the API first for legal reasons but told me they would do their best to stop me.

They switched over to PerimeterX which took me 3 days to get past.

Last week someone posted an article here about ChatGPT using Cloudflare Turnstile. [0] First, the article made some mistakes how it works. Second, I used the [AI company product] and the Chrome DevTools Protocol (CDP) to completely rewrite all the scripts intercepting them before they were evaluated -- the same way I was able to figure out PerimeterX in 3 days -- and then recursively solve controlling all the finger printing so that it controls the profile. Then it created an API proxy to expose ChatGPT for free. It required some coaching about the technique but it did most of the work in 3 hours.

These companies are spending 10s of millions of dollars on these products and considering what OpenAI is boasting about security, they are worthless.

[0] [https://news.ycombinator.com/item?id=47566865](https://news.ycombinator.com/item?id=47566865)

---

### snowwrestler

It looks like proof of work because:

> Worryingly, none of the models given a 100M budget showed signs of diminishing returns. “Models continue making progress with increased token budgets across the token budgets tested,” AISI notes.

So, the author infers a durable direct correlation between token spend and attack success. Thus you will need to spend more tokens than your attackers to find your vulnerabilities first.

However it is worth noting that this study was of a 32-step network intrusion, which only one model (Mythos) even was able to complete at all. That’s an incredibly complex task. Is the same true for pointing Mythos at a relatively simple single code library? My intuition is that there is probably a point of diminishing returns, which is closer for simpler tasks.

In this world, popular open source projects will probably see higher aggregate token spend by both defenders and attackers. And thus they might approach the point of diminishing returns faster. If there is one.

> **SyneRyder**: Worth pointing out that as impressive as the 32-step network takeover is, Mythos wasn't able to achieve it on *every* attempt, and the network itself did not have the usual defence systems.
> 
> I wouldn't use those as excuses to dismiss AI though. Even if this model doesn't break your defences, give it 3 months and see where the next model lands.

> **janalsncm**: Knowing nothing about cybersecurity, maybe the question is whether it costs more tokens to go from 32 steps to 33, or to complete the 33rd step? If it’s cheaper to add steps, or if defense is uncorrelated but offense becomes correlated, it’s not as bad as the article makes it seem.
> 
> For instance, if failing any step locks you out, your probability of success is p^N, which means it’s functionally impossible with enough layers.

> > **necovek**: This is not like adding one bit of randomness to improve security: this was a model system which required 32 steps to break in if I understood correctly.
> > 
> > It is not that one would design a system in this manner because you'd never design a loophole in no matter the steps it takes to get there: it is just a benchmark.

---

### mikewarot

Long ago, during the Viet Nam conflict, the US government learned that computers needed to be able to securely process data from multiple levels of classification simultaneously.  Research in the 1970s found solutions that were adopted in the Mainframe world, like KeyKOS and EROS. Then the PC revolution swept all that away, and we're here 40+ years later, with operating systems that trust every bit of code the user runs with that user's full authority.

It's nuts. If the timing were slightly different, none of this "Cybersecurity" would even be a thing. We'd just have capabilities based, secure general purpose computation.

> **necovek**: While I agree we are re-learning lessons from ages ago and reinventing the same tech, I believe the problem comes from the desire to manage the same data with different software. On desktops, imagine your photo library that you might view with one set of programs, modify with another, try out a completely new one to make videos out of photos...
> 
> As soon as there are multiple programs with full authority on your data, "cybersecurity" happens. And internet/web is that to the power of 100.

---

### devinabox

The cost of this is going to come down dramatically - just throwing the model at the codebase is a really inefficient process. My own experiments show that spending more tokens on understanding and transforming how the codebase can be explored(i.e enumerating source to sink traces) drastically lowers the cost to confirm vulnerabilities.Something that excites me greatly is that software quality has been incredibly difficult primarily because no single developer can hold the entire contract in their head and analyze it. It's now a reality that we can transform raw source code into actionable artifacts that allow a system to see the big picture and pin point the fracture points within it.

---

### admiralrohan

"Security economy: to harden a system we need to spend more tokens discovering exploits than attackers spend exploiting them. To harden a system you need to spend more tokens discovering exploits than attackers will spend exploiting them." - This feels similar to missile defense dilemma. Spending 2M$ missile to attack a 20k$ drone.

---

### chaitanyya

What do they mean when they say "no diminishing returns?" does this essentially mean the code you are testing has no bounded state space and you continue to find infinite paths?

Because we have tools and techniques that can guarantee the absence of certain behavior in a bounded state space using formal methods (even unbounded at times)

Sure, it's hard to formally verify everything but if you are dealing with something extremely critical why not design it in a way that you can formally verify it?

But yeah, the easy button is keep throwing more tokens till you money runs out of money

---

### chromacity

I discussed this in more detail in one of my earlier comments, but I think the article commits a category error. In commercial settings, most of day-to-day infosec work (or spending) has very little to do with looking for vulnerabilities in code.

In fact, security programs built on the idea that you can find and patch every security hole in your codebase were basically busted long before LLMs.

> **Muromec**: Commercial infosec is deleting firefox from develop machines, because it's not secure and explaining to muggles why they shouldn't commit secret material to the code repository. That and blocking my ssh access to home router of course.

> > **chromacity**: I mean, often, yep. The real reason why they are unhappy with you having an unsupported browser is simply that it's much harder to reason about or enforce policies across bespoke environments. And in an enterprise of a sufficient scale, the probability that one of your employees is making a mistake today is basically 1. Someone is installing an infostealer browser extension, someone is typing in their password on a phishing site, etc. So, you really want to keep browsers on a tight leash and have robust monitoring and reporting around that.
> > 
> > Yeah, it sucks. But you're getting paid, among other things, to put up with some amount of corporate suckiness.

> > > **GuB-42**: The thing that kills me every time is how IT treat development machines the same way as the rest of the corporate network.
> > > 
> > > Developers usually need elevated privileges, executing unverified arbitrary code is literally their job. Their machines are not trustworthy, and yet, they often have access to the entire company internal network. So you get a situation where they have both too much privilege (access to resources beyond the scope of their work) and too little (some dev tools being unavailable).

> > > **gerdesj**: "The real reason why they are unhappy with you having an unsupported browser"
> > > 
> > > I tend to encourage Firefox over Cr flavoured browsers because FF (for me) are the absolute last to dive in with fads and will boneheadedly argue against useful stuff until the cows come home ... Web Serial springs to mind (which should finally be rocking up real soon now).
> > > 
> > > Oh and they are not sponsored by Google errm ... 8)
> > > 
> > > I'm old enough to remember having to use telnet to access the www (when it finally rocked up and looked rather like Gopher and WAIS) (via a X.25 PAD) and I have seen the word "unsupported" bandied around way too often since to basically mean "walled garden".
> > > 
> > > I think that when you end up using the term "unsupported browser" you have lost any possible argument based on reason or common decency.

---

### jerf

I've said for decades that, in *principle*, cybersecurity is advantage defender. The defender has to leave a hole. The attackers have to find it. We just live in a world with so many holes that dedicated attackers rarely end up bottlenecked on finding holes, so in practice it ends up advantage attacker.

There is at least a possibility that a code base can be secured by a (practically) finite number of tokens until there is no more holes in it, for reasonable amounts of money.

This also reminds me of what I wrote here: [https://jerf.org/iri/post/2026/what_value_code_in_ai_era/](https://jerf.org/iri/post/2026/what_value_code_in_ai_era/) There's still value in code tested by the real world, and in an era of "free code" that may become even more true than it is now, rather than the initially-intuitive less valuable. There is no amount of testing you can do that will be equivalent to being in the real world, AI-empowered attackers and all.

> **mapontosevenths**: >in principle, cybersecurity is advantage defender
> 
> I disagree.
> 
> The defender must be right every single time. The attacker only has to get lucky and thanks to scale they can do that every day all day in most large organizations.

> > **janalsncm**: My understanding of defense in depth is that it is a hedge against this. By using multiple uncorrelated layers (e.g. the security guard shouldn’t get sleepier when the bank vault is unlocked) you are transforming a problem of “the defender has to get it right every time” into “the attacker has to get through each of the layers at the same time”.

> > > **mapontosevenths**: It is a hedge, that said it only reduces the probability of an event and does not eliminate it.
> > > 
> > > To use your example, if the odds of the guard being asleep and the vault being unlocked are both 1% we have a 0.0001 chance on any given day. Phew, we're safe...
> > > 
> > > Except that Google says there are  68,632 bank branch locations in the US alone. That means it will happen roughly 7 times on any given day someplace in America!
> > > 
> > > Now apply that to the scale of the internet.  The attackers can rattle the locks in every single bank in an afternoon for almost zero cost.
> > > 
> > > The poorly defended ones have something close to 100% odds of being breached, and the well defended ones how low odds on any given day, but over a long enough timeline it becomes inevitable.
> > > 
> > > To again use your bank example. if we only have one bank, but keep those odds it means that over about 191 years the event will happen 7 times. Or to  restate that number, it is like to happen at least once every 27 years. You'll have about 25% odds of it happening in any 7 year span.
> > > 
> > > For any individual target, it becomes unlikely, but also still inevitable.
> > > 
> > > From an attackers perspective this means the game is rigged in their favor. They have many billions of potential targets, and the cost of an attack is close to zero.
> > > 
> > > From a defenders perspective it means realizing that even with defense in depth the breach is still going to happen eventually and that the bigger the company is the more likely it is.
> > > 
> > > Cyber is about mitigating risk, not eliminating it.

> > **NegativeK**: The defender must be right every single time, and the attacker right only once.
> > 
> > Until the attacker has initial access.
> > 
> > Then the attacker needs to be right every single time.

> > **traderj0e**: Well, the attacker has something to lose too. It's not like the defender has to be perfect or else attacks will just happen, it takes time/money to invest in attacking.

> > > **mapontosevenths**: The cost to your average ransomware crew can be rounded down to zero, because it's pretty darn close. They use automated tools running on other peoples computers and utilizing other peoples connectivity. The tools themselves for most RaaS (ransomware as a service) affiliates are also close to zero cost, as they pay the operator a percentage of profits.
> > > 
> > > The time is a cost, but at scale any individual target is a pretty minor investment since it's 90%+ automated. Also, these aren't folks that are otherwise highly employable. The opportunity cost to them is also usually very low.
> > > 
> > > The last attacker I got into a conversation with was interesting. Turns out, he was a 16 year old from Atlanta GA using a toolkit as an affiliate. He claimed he made ~100k/year and used the money on cars and girls. I felt like he was inflating that number to brag. His alternative probably would have been McDonalds, and as a minor if he got caught it would've been probation most likely. I told him to come to the blue team, we pay better.

> > **coldtea**: Not to mention an attacker motivated by financial gain doesn't even need a particular targer  defender. One/any found available will do.

> > **tptacek**: The attacker and defender have different constant factors, and, up until very recently, constant factors dominated the analysis.

> **traderj0e**: I agree for the type of attacks the article focuses on, but DDoS and social engineering seem like advantage attacker.

---

### tptacek

It looks like it, but it isn't. It's the work itself that's valued in software security, not the amount of it you managed to do. The economics are fundamentally different.

Put more simply: to keep your system secure, you need to be fixing vulnerabilities faster than they're being discovered. The token count is irrelevant.

Moreover: this shift is happening because the automated work is outpacing humans for the same outcome. If you could get the same results by hand, they'd count! A sev:crit is a sev:crit is a sev:crit.

> **keeda**: I think the premise is:
> 
> 1) The number of vulnerabilities surfaced (and fixed?) in a given software is roughly proportional to the amount of attention paid to it.
> 
> 2) Attention can now be paid in tokens by burning huge amounts of compute (bonus: most commonly on GPUs, just like crypto!)
> 
> 3) Whoever finds a vulnerability has a valuable asset, though the value differs based on the criticality of the vulnerability itself, and whether you're the attacker or the defender.
> 
> More tokens -> more vulns is not a guarantee of course, it's a stochastic process... but so is PoW!

---
