# Cal.com is going closed source

- **Link**: https://cal.com/blog/cal-com-goes-closed-source-why
- **HN**: https://news.ycombinator.com/item?id=47780456
- **Score**: 352 points
- **By**: Benjamin_Dobell
- **Date**: 2026-04-15 15:26 UTC
- **Comments**: 276

---

## Comments

### simonw

Drew Breunig published a very relevant piece yesterday that came to the opposite conclusion: [https://www.dbreunig.com/2026/04/14/cybersecurity-is-proof-o...](https://www.dbreunig.com/2026/04/14/cybersecurity-is-proof-of-work-now.html)

Since security exploits can now be found by spending tokens, open source is MORE valuable because open source libraries can share that auditing budget while closed source software has to find all the exploits themselves in private.

> If Mythos continues to find exploits so long as you keep throwing money at it, security is reduced to a brutally simple equation: *to harden a system you need to spend more tokens discovering exploits than attackers will spend exploiting them*.

> **dang**: Thanks - I've re-upped* that one here: *Cybersecurity looks like proof of work now* - [https://news.ycombinator.com/item?id=47769089](https://news.ycombinator.com/item?id=47769089) (no comments yet)
> 
> * a la [https://news.ycombinator.com/item?id=26998308](https://news.ycombinator.com/item?id=26998308)

> **DrammBA**: I have a feeling the real reason is them trying to avoid someone using AI to copyright-wash their product, they're just using security as the excuse.

> > **OsrsNeedsf2P**: An app like Cal.com can be vibe coded in a few evenings with a Chrome MCP server pointed to their website to figure out all the nooks and crannys. The moat of Cal.com is not the code, it's the users who don't want to migrate.
> > 
> > The real answer is they are likely having a hard time converting people to paid plans

> > > **notnullorvoid**: > The moat of Cal.com is not the code, it's the users who don't want to migrate.
> > > 
> > > That's a very weak moat unless you have something else like the friction of network dependence similar to a social network.

> > > **opem**: For real, one of the reasons I use cal.com is because it's open source. Time to migrate.

> > > **il-b**: > An app like Cal.com can be vibe coded in a few evenings
> > > 
> > > Do it then

> > > **indianmouse**: May be trying creating one and see how much effort and time is required to clone such a functionality to a proper working state! Something for personal use can be created in about 5-10 days, but even then the skill that is required and the amount of tokens to burn, hosting and security etc, will easily kill. This is exactly the thought process of many, but it will surely kill many opensource contributors. I've stopped committing anything to any open source repos as a personal choice. I do not want to train a LLM which will eventually create more slop and headaches since for me, time is the only important factor which holds the maximum value! Nothing else!

> > > **j45**: Coding something vs maintaining it can be quite different things.

> > **theahura**: At risk of self promotion, I think more people should adopt something like the Ship of Theseus license ([https://github.com/tilework-tech/nori-skillsets/pull/465/cha...](https://github.com/tilework-tech/nori-skillsets/pull/465/changes)). It's not obvious if this will patch the clean room hole in licensing, but I'd rather see it play out in court than assume opensource is just fully dead

> > > **klempner**: I am incredibly skeptical that license is legally meaningful. (but obligatory IANAL.)
> > > 
> > > Generally speaking it is very very difficult to have a license redefine legal terms. Either this theseus copy is legally a derivative work or it isn't, and text of a license is going to do at most very very little to change that.

> > > **hrimfaxi**: > It's not obvious if this will patch the clean room hole in licensing, but I'd rather see it play out in court than assume opensource is just fully dead
> > > 
> > > Are you willing to bear the burden of litigation?

> > > **duskdozer**: I like the spirit but I do find it a bit ironic to include it in a project where almost every commit is made by an LLM

> > > **devmor**: I cannot imagine that license addendum is legally enforceable (let alone provable) in most jurisdictions on earth but it is interesting.

> > > **imtringued**: I don't think you understand how copyright works.
> > > 
> > > Copyright can only deny the right to make copies.
> > > 
> > > If someone spends years using your software and they have learned a mental model of how your software works, they can build an exact replica and there is nothing you can do about that since there is no copy you can sue over. Said user is also allowed to use AI tools to aid in the process.
> > > 
> > > What you want is an EULA, which is a contract users explicitly have to agree with. A license file only grants access or the right to copy, it doesn't affect usage of your software.

> > **lisperforlife**: Exactly this! Classic open source bait and switch.

> > **bit1993**: Called this 9 months ago
> > [https://news.ycombinator.com/item?id=44559840](https://news.ycombinator.com/item?id=44559840)
> > 
> > "AI slop is rapidly destroying the WWW, most of the content is becoming more and more low-quality and difficult to tell if its true or hallucinated. Pre-AI web content is now more like the golden-standard in terms of correctness, browsing the Internet Archive is much better. This will only cause content to go behind pay-walls, allot of open-source projects will be closed source not only because of the increased work maintainers have to do to not only review but also audit patches for potential AI hallucinations but also because their work is being used to train LLMs and re-licensed to proprietary."

> > > **teleforce**: Typical FUD.
> > > 
> > > Replace AI with "open source and Linux", and "open source" with "Windows" in the statements. That's what Microsoft's PR team would have said about open source and Linux about 20 years back in the 2000s.
> > > 
> > > After the unsuccessful FUD era, now Microsoft is running away with Linux by running its Windows alongside via WSL to combat MacOS Unix-like popularity, and due to Linux and open source dominance in the cloud OS demographic.

> **timcobb**: but if your source is closed, your attacker's surface area is way smaller.

> **pietz**: This conclusion makes more sense to me, but maybe I'm too naive.
> 
> The media momentum of this threat really came with Mythos, which was like 2 or 3 weeks ago? That seems like a fairly short time to pivot your core principles like that. It sounds to me like they wanted to do this for other business related reasons, but now found an excuse they can sell to the public.
> 
> (I might be very wrong here)

> **haritha-j**: I like that LLMs have basically switched to the weapons business model. Buy our LLM so that the bad guy we'll sell our LLM to doesnt destroy your code. As a bonus, we'll give  you a little head start. And if you're a small company that can't afford our LLM, too bad.

> **mgdev**: This is an economically sound conclusion.
> 
> It also means that you need to extract enough value to cover the cost of said tokens, or reduce the economic benefit of finding exploits.
> 
> Reducing economic benefit largely comes down to reducing distribution (breadth) and reducing system privilege (depth).
> 
> One way to reduce distribution is to, raise the price.
> 
> Another is to make a worse product.
> 
> Naturally, less valuable software is not a desirable outcome. So either you reduce the cost of keeping open (by making closed), or increase the price to cover the cost of keeping open (which, again, also decreases distribution).
> 
> The economics of software are going to massively reconfigure in the coming years, open source most of all.
> 
> I suspect we'll see more 'open spec' software, with actual source generated on-demand (or near to it) by models. Then all the security and governance will happen at the model layer.

> > **cassianoleal**: > I suspect we'll see more 'open spec' software, with actual source generated on-demand (or near to it) by models. Then all the security and governance will happen at the model layer.
> > 
> > So each time you roll the dice you gamble on getting a fresh set of 0-days? I don't get why anyone would want this.

> > > **mgdev**: You already do this with human-authored code, just slowly.
> > > 
> > > Project model capabilities out a few years. Even if you only assume linear improvement at some point your risk-adjusted outcome lines cross each other and this becomes the preferred way of authoring code - code nobody but you ever sees.
> > > 
> > > Most enterprises already HATE adopting open source. They only do it because the economic benefit of free reuse has traditionally outweighed the risks.
> > > 
> > > If you need a parallel: we already do this today for JIT compilers. Everything is just getting pushed down a layer.

> > **xigoi**: I love using software that changes every time you compile it.

> **jstummbillig**: > to harden a system you need to spend more tokens discovering exploits than attackers will spend exploiting them.
> 
> That can't be right, can it? Given stable software, the relative attack surface keeps shrinking. Mythos does not *produce* exploits. Should be defenders advantage, token wise, no?

> > **rhplus**: It’s the classic asymmetric warfare problem:
> > 
> > Defenders have to find all the holes in all their systems, while attackers just need to find one hole in one system.

> > > **lexlambda**: A slight factor differentiating security systems here is involved to the advantage of defenders: Attackers have to find a whole exploit chain, while defenders only need to fix one part of it.

> > > **jstummbillig**: The point is that, as the defender, you only have to find each hole once, while the attacker can spend an infinite amount of tokens trying to find more holes, that are increasingly harder to find and might, eventually, not exist at all. The defender can do that too, of course, but being in the defense, there is value in not being able to uncover new holes (your system keeps working, ostensibly) while as the attacker that's simply how you fail.

> > **JoshTriplett**: > Mythos does not produce exploits.
> > 
> > AI in general will, don't worry. "Move fast and break things" makes more exploits than "move steadily and fix things" does.

> > **paisawalla**: So long as that OSS keeps accumulating features, there isn't quite the equilibrium you're imagining. If you can pin to a stable version, which continues to audited, you're fine. But if the rest of the world moves on to newer versions of the software, you'll have to as well, unless you want to own the burden of hardening older versions.

> **MerrimanInd**: I wonder if we could find a way to donate unused tokens or even local compute resources to open-source projects we support. Especially for security auditing where it could probably be somewhat more asynchronous and disconnected than the open-source developers' personal tool choices.

> > **jeroenhd**: "unused tokens" are the force driving token cost down. If everyone used all of the tokens they thought they were paying for, prices would explode. People with subscriptions that don't get out everything they can are subsidizing the system.
> > 
> > There are ways to use LLM service providers that leave no tokens unused, by just billing per token. Unsurprisingly, this quickly becomes much more expensive than subscriptions.

> > > **lrvick**: And that is why the only winning move is owning a GPU.

> > **throwuxiytayq**: “Unused tokens” are a weird, fragile concept that I wouldn’t want to build upon. You can just donate money, you know. That’s what money’s for - it’s the universal exchange thingy.

> > > **rswail**: Maybe if we reframed money as a "fungible token" people would start understanding its use again?

> **pllbnk**: It's been a common wisdom now for decades that open source is more secure. Security is just a scapegoat here.

> > **aleph_minus_one**: > It's been a common wisdom now for decades that open source is more secure.
> > 
> > This is not true.
> > 
> > The problem rather is that the managers of many companies don't allow their programmers to apply their knowledge about security - the programmers should rather weed out new features.

> **skybrian**: This seems similar to the lesson learned for cryptographic libraries where open source libraries vetted by experts become the most trusted.
> 
> Your average open source library isn’t going to get that scrutiny, though. It seems like it will result in consolidation around a few popular libraries in each category?

> > **layer8**: An important difference between SaaS offerings and open source libraries is that the latter have not liability. They can much more easily afford exhibiting vulnerabilities until those are fixed.

> **flying_sheep**: > to harden a system you need to spend more tokens discovering exploits than attackers will spend exploiting them
> 
> This is true until certain point, unless the requirement / contract itself has loophole which the attacker can exploit it without limit. But I don't think this is the case.
> 
> Let's say, if someone found an loophole in sort() which can cause denial-of-service. The cause would be the implementation itself, not the contract of sorting. People + AI will figure it out and fix it eventually.

> **alienbaby**: This feels like it misses the point. Tokens = money. The real differentiator is time and effort.
> 
> Llm's will find your issues faster, but not necessarily more accurately than a domain expert. But experts cost money and effort takes longer to apply.
> 
> Are llm's going to reduce everyone's wages because they are cheap labour?

> **criddell**: How may open source libraries have auditing budgets?

> > **simonw**: I expect we're about to find that it's a lot easier to convince a company to spend money running an AI security scan of their dependencies and sharing the results with the maintainers than it is to have them give those maintainers money directly.
> > 
> > (I just hope they can learn to *verify the exploits are valid* before sharing them!)

> > **Mordisquitos**: Their commercial users have auditing budgets.

> > > **dspillett**: Does your ideal world have an easy path to citizenship?
> > > 
> > > I might like to live there.

> **tonymet**: This may be true long term but not short term. It also assumes that white hats will be as motivated as black hats – not true.
> 
> For projects with NO WARRANTY, the risk is minimal, so yes there are upsides.
> 
> For a commercial project like cal.com, where a breach means massive liability, they don’t have the resources to risk breaches in the short term for potentially better software in the long term.

> **not-chatgpt**: Security should be a non issue in the age of AI now that auditing is cheaper than ever.
> 
> I'd give them more credits if they use the AI slop unmaintainability argument.

---

### ryanleesipes

Head of Thunderbird project here.

Our scheduling tool, Thunderbird Appointment, will always be open source.

Repo here: https://
github.com/thunderbird/appointment

Come talk to us and build with us. We'll help you replace Cal.com

> **raybb**: You should add some screenshots to the readme or somewhere before a sign in screen.
> 
> Sounds like a great tool though. How much is the hosted version?

> > **devmount**: We added some screenshots to the repository now. Thanks so much for the suggestion!

> > **ryanleesipes**: Yes, we should. Will do that today

> > **bean469**: There are screenshots in the link[1] provided in the README.md
> > 
> > 1. [https://stage.appointment.day](https://stage.appointment.day)

> > **m3nu**: A Docker image would be good too.

> **jen729w**: 1. Goes to site. Clicks appointment.tb.pro link in sidebar.
> 
> 2. Gives email address.
> 
> 3. Is told to join the waitlist.
> 
> 4. Blocks email address given at 2.
> 
> Hardly a terrific experience.

> > **kewisch**: I'm curious how it blocked your email, could you share more details on what message you got? Feel free to reach out to me outside of HN.

> > **ryanleesipes**: Yeah. We need to create a docker container and make it easy to deploy for folks. We're not ready with the hosted option at the moment.

> **sashimimono**: I would like to, but... have you tried to use thunderbird on an "older" linux laptop nowadays? Even with 8 gigs of ram, and a non-fancy memory-saving windowmanager, thunderbird is almost unusable now (large imap mbox), firefox even worse. I don't see why all that additional bloat is needed, or wanted. Please keep in mind, that a lot(!) of people are not able to afford buying new hardware every now and then anymore. And this is getting worse. First the pandemic, then the war in Ukraine, now the war in Middle-East. Shortage of ram/storage/everything (thanks ai) and massivly increased costs of energy, housing, food, insurance, everything. And in the years to come, I am afraid, that will be getting worse. Please think about it, when adding the "next cool feature", 'Keep the internet affordable'. --thunderbird user since 1.0

> > **hedora**: Regarding FF:  Something is probably wrong with your install, or the websites you have open.
> > 
> > As a datapoint: FF + Chrome with lots of stuff open uses 2.6GB on my machine.  With XFCE and a GB of other apps, it’s using about 4GB.  15 year old machine.  Perf is fine.

> **winrid**: > Come talk to us and build with us
> 
> do we need an appointment :)

> **bean469**: Thanks, looks like a great alternative

> **ezekg**: "Thunderbird, the open source Cal.com"

> > **ryanleesipes**: Love it!

---

### ButlerianJihad

This seems kind of crazy. If LLMs are so stunningly good at finding vulnerabilities in code, then shouldn't the solution be to run an LLM against your code after you commit, and before you release it? Then you basically have pentesting harnesses all to yourself before going public. If an LLM can't find any flaws, then you are good to release that code.

A few years ago, I invoked Linus's Law in a classroom, and I was roundly debunked. Isn't it a shame that it's basically been fulfilled now with LLMs?

[https://en.wikipedia.org/wiki/Linus%27s_law](https://en.wikipedia.org/wiki/Linus%27s_law)

> **johnfn**: After a release, attackers have effectively infinite time to throw an LLM against every line of your code - an LLM that only gets smarter and cheaper to run as time passes. In order to feel secure you’d need to do all the work you’d imagine an attacker would ever do, for every single release you ship.

> > **utopiah**: > attackers have effectively infinite time
> > 
> > No, attackers are also rational economical actors. They don't randomly attack any software just for the aesthetics beauty of the process. They attack for bounty, for fame, for national interest, etc. No matter the reason it's not random and thus they DO have a budget, both in time and money. They attack THIS project versus another project because it's interesting to them. If it's not, they might move to another project but they certainly won't spend infinite time precisely because they don't have infinite resources. IMHO it's much more interesting to consider the realistic arm race then theoretical scenarii that never take place.

> > **mixdup**: The first few times it's going to be expensive, but once everyone level sets with intense scans of their codebases, "every single release" is actually not that big a deal, since you are not likely to be completely rebuilding your codebase every release

> > > **techpression**: You still have to account for the non-deterministic behavior of an LLM, when do you know you have exhausted its possible outcomes for any given piece of code?

> > **stavros**: This assumes that the relationship between "LLM tokens spent" and "vulnerabilities found" doesn't plateau, though.

> > **rhubarbtree**: But so do you and all your users what’s your point?

> **r2vcap**: As LLMs improve and adoption grows, maintaining a FOSS project is becoming more complex and more expensive in terms of time and manpower. That part is easy to understand.
> 
> It is also become a trend that LLM-assisted users are generating more low-quality issues, dubious security reports, and noisy PRs, to the point where keeping the whole stack open source no longer feels worth it. Even if the real reason is monetization rather than security, I can still understand the decision.
> 
> I suspect we will see more of this from commercial products built around a FOSS core. The other failure mode is that maintainers stop treating security disclosures as something special and just handle them like ordinary bugs, as with libxml2. In that sense, Chromium moving toward a Rust-based XML library is also an interesting development.

> > **d3Xt3r**: Just use AI to fight AI, that's the only sensible way we can keep up. So if you're low-quality PRs, reports etc, have LLMs filter them out. Like how once upon a time we used to drown in email spam but it's now mostly a non-issue thanks to intelligent spam filters, the same needs to happen for opensource projects. Use AI to fight AI.

> > > **wartywhoa23**: In other words, have more money to pay than your enemy.
> > > 
> > > This game will end horribly.

> **vlapec**: LLMs really are stunningly good at finding vulnerabilities in code, which is why, with closed-source code, you can and probably will use them to make your code as secure as possible.
> 
> But you won't keep the doors open for others to use them against it.
> 
> So it is, unfortunately, understandable in a way...

> > **paprikanotfound**: I'm not a security expert but can't close source applications be vulnerable and exploited too? I feel like using close source as a defense is just giving you a false sense of security.

> > > **layer8**: Finding a vulnerability in a black box is drastically different from finding one in a white box. This isn’t about whether there is a vulnerability or not, but about the likelihood of it being found.

> > > **sandeepkd**: What is being phrased as obscurity is one of the approaches to security as long as you are able to keep the code safe. Your passwords, security keys are just random combination of strings, the fact that they are obscure from everyone is what provides you the security

> > > **pixel_popping**: Delaying attacks is a form of valid security.

> > **eloisant**: LLM like humans can find vulnerabilities in black boxes. We already established 30 years ago that open source is usually more secure than closed source and that security by obscurity doesn't work.

> > **genxy**: You don't need the source, the LLM has the source, it is called the binary.

> **sandeepkd**: Every change would introduce the possibility of a vulnerability being added to the system and one would need to run the LLM scan across the entire code base. It gets very costly in a environment where you are doing regular commits. Companies like Github already provide scanning tools for static analysis and the cost is already high for them.

> > **pianopatrick**: Might lead to a move away from continuous delivery back towards batched releases.

> **pcblues**: Write simple code. Do what you said, which is a very good idea. Test LLM security against the compiler too.

> **layer8**: Attackers only need LLMs to be good at randomly finding one vulnerability, whereas service providers need them to be good at finding *all* such vulnerabilities.

> **samename**: That’s a non-trivial cost for commonly severely underfunded open source projects

> > **yawndex**: Cal.com is not a severely underfunded project, it raised around $32M of VC money.

> > > **evanelias**: It's not a "project" though; the *business* Cal.com Inc raised that VC money. Their open source repo did not raise the money.
> > > 
> > > Did they ever promise to keep their codebase FOSS forever, in a way that differs from what they're already doing over at cal.diy? If not, I don't see why it would be reasonable to expect them to spend a huge amount of money *re-scanning on every single commit/deploy* in order to keep their non-"DIY" product open source.

> **dgellow**: I mean, you should definitely have _some_ level of audit by LLMs before you ship, as part of the general PR process.
> 
> But you might need thousands of sessions to uncover some vulnerabilities, and you don’t want to stop shipping changes because the security checks are taking hours to run

> **fwip**: It's entirely possible to address all the LLM-found issues and get an "all green" response, and have an attacker still find issues that your LLM did not. Either they used a different model, a different prompt, or spent more money than you did.
> 
> It's not a symmetric game, either. On defense, you have to get lucky every time - the attacker only has to get lucky once.

> > **earthnail**: > It's not a symmetric game, either. On defense, you have to get lucky every time - the attacker only has to get lucky once.
> > 
> > This! I love OSS but this argument seems to get overlooked in most of the comments here.

---

### gouthamve

This is a weird knee-jerk reaction. I feel like this is more a business decision than a security decision.

I feel like with AI, self-hosting software reliably is becoming easier so the incentives to pay for a hosted service of an OSS project are going down.

> **tecoholic**: I think people are finding ways to either enable “pro” features and at least find the right extension points to implement them easily with LLMs. Security is window dressing.

> **fhn**: Yeah, I don't buy it. If they don't want these security reports, ignore them and continue your path. Blaming AI is just an excuse to close source. If you don't want AI to learn from your code, too late. Add genetic algorithms and fuzzing into AI and it can iterate and learn a billion times faster, no need to learn for humans.

> **badgersnake**: AI is certainly getting a lot of milage as an excuse for doing bad things.
> 
> Wanna sack a load of staff? - AI
> 
> Wanna cut your consumer products division? - AI
> 
> Wanna take away the source? - AI

> > **rhubarbtree**: Well, first AI uses security to sell models. So other companies hijack their narrative for their purposes. This is how marketing works.

> **esafak**: Their product is getting commoditized: [https://workspace.google.com/resources/appointment-schedulin...](https://workspace.google.com/resources/appointment-scheduling/)

> > **rhubarbtree**: Remember when calendly went out of business?

> > **gp14**: Calendar apps have been commoditized for about 15 years now but they keep growing!

> > **bensyverson**: The real downside to Google's solution is that you have to use Google Meet. Depending on your opinion of Meet, this is either no big deal or a total deal breaker.

> > **no_wizard**: I always felt it was a matter of time before Google took notice.
> > 
> > It has always been odd to me they didn’t have this functionality years ago. It’s been requested for a long long time

> **kartika36363**: correct. guy's doing mental gymnastics all to say he's a sellout.

---

### Hendrikto

> Today, AI can be pointed at an open source codebase and systematically scan it for vulnerabilities.

So do that and fix your bugs. This post makes no sense.

---

### robinhood

Very weak argument. You could have had the same speech before AI.

I would rather say that the core product is not strong and differentiated enough to resist this new age of coding, and it's an attempt to protect revenues.

---

### Tepix

Hey cal.com, as a potential customer, you have just lost me.
Open source is set to profit from improved transparency in the SSDLC. With closed source, you will have to trust the software vendor instead.

I'm not sure I agree with Drew Breunig, however. The number of bugs isn't infinite. Once we have models that are capable enough and scan the source code with them at regular intervals, the likelihood of remaining bugs that can be exploited goes way down.

---

### m11a

I'm not sure security through obscurity is a great practice?

Not to mention, I presume the core bits of Cal.com's source code are already in place and aren't going to change significantly?

Like, this feels like a business decision and not a security decision

---

### diebillionaires

Lame. "We don't want AI pointed at our code so we're going closed source". That's hilarious and a cover up.

> **szszrk**: I think them going closed source is as much related to security and AI, as work from office is related to productivity in large companies.
> 
> So not really.
> 
> I think they went closed source as there are too many decent clones based off their code and they realized it's eating up their niche.

---

### doytch

I get the mentality but it feels very much like security through obscurity. When did we decide that that was the correct model?

> **keeda**: Security through obscurity is only problematic if that is the only, or a primary, layer of defense. As an incremental layer of deterrence or delay, it is an absolutely valid tactic. (Note, not commenting on whether that is the rationale here.)

> > **traderj0e**: That, and plenty of closed-source software at least has a decent security track record by now. I haven't seen an obvious cause-and-effect of open-source making something more secure. Only the other direction, where insecure closed-source software is kept closed because they know it's Swiss cheese.

> **1970-01-01**: This is not security via obscurity; it is reducing your attack surface as much as possible.

> > **dspillett**: Reducing your attack surface as much as possible via obscurity.

> > > **jqbd**: I think cal.com is assuming LLMs are only good at hacking with the source code of the target, whether that's true I don't know

> > > **1970-01-01**: Going closed source is making the branch secret/private, not making it obscure. Obscurity would be zipping up the open source code (without a password) and leaving it online. Obscurity is just called taking additional steps to recover the information. Your passwords are not obscure strings of characters, they are secrets.

> > **behringer**: right, they're just securing their application by making the bugs obscure. It's totally different.

> **ergocoder**: Security through obscurity is still better than no obscurity...

> **Peer_Rich**: hey cofounder here. since it takes my 16 year old neighbors son 15 mins and $100 claude code credits to hack your open source project

> > **simonw**: Are you at all worried that the message you are spreading here is "We are no longer confident in our own ability to secure your data?"

> > > **wild_egg**: That's exactly the message I got from the video

> > **doytch**: Right, but those capabilities are available to you as well. Granted the remediation effort will take longer but...you're going to do that for any existing issues _anyway_ right?
> > 
> > I understand why this is a tempting thing to do in a "STOP THE PRESSES" manner where you take a breather and fix any existing issues that snuck through. I don't yet understand why when you reach steady-state, you wouldn't rely on the same tooling in a proactive manner to prevent issues from being shipped.
> > 
> > And if you say "yeah, that's obv the plan," well then I don't understand what going closed-source _now_ actually accomplishes with the horses already out of the barn.

> > > **throwaway5752**: > those capabilities are available to you as well
> > > 
> > > Give him $100 to obtain that capability.
> > > 
> > > Give each open source project maintainer $100.
> > > 
> > > Or internalize the cost if they all decide the hassle of maintaining an open source project is not worth it any more.
> > > 
> > > I'm not aiming this reply at you specific, but it's the general dynamic of this crisis. The real answer is for the foundational model providers to give this money. But instead, at least one seems to care more about acquiring critical open source companies.
> > > 
> > > We should openly talk about this - the existing open source model is being killed by LLMs, and there is no clear replacement.

> > **toast0**: I don't think this really helps that much. Your neighbor could ask an LLM to decompile your binaries, and then run security analysis on the results.
> > 
> > If the tool correctly says you've got security issues, trying to hide them won't work. You still have the security issues and someone is going to find them.

> > > **evanelias**: If I understand correctly, their primary product is SaaS, and their non-DIY self-host edition is an enterprise product. So your neighbor wouldn't have access to the binaries to begin with.

> > **wild_egg**: It only takes 20 minutes and $200 to hack a closed source one too though. LLMs are ludicrously good at using reverse engineering tools and having source available to inspect just makes it slightly more convenient.

> > > **keeda**: Very true, but that is still a meaningfully higher cost at scale. If, as people are postulating post-Mythos, security comes down to which side spends more tokens, it is a valid strategy to impose asymmetric costs on the attacker.

> > **sambaumann**: Couldn't you just spend those $100 on claude code credits yourself and make sure you're not shipping insecure software? Security by obscurity is not the correct model (IMO)

> > **Maken**: Was open source any more secure before LLMs became so cheap? For those same 100$ you could have a North Korean hacking your code for a whole month.

> > **bayindirh**: Why not can’t you (as in Cal.com) spend that amount of money and find vulnerabilities yourself?
> > 
> > You can keep the untested branch closed if you want to go with “cathedral” model, even.

> > **senko**: What makes you think it'll take him more than 16 mins and $110 claude code credits to hack your closed source project?

> > **otabdeveloper4**: No it doesn't. Have you been actually "hacked"?

> > **bakugo**: *This comment sponsored by Anthropic

> > **hypeatei**: > neighbors son 15 mins and $100 claude code credits
> > 
> > Is that true? Didn't the Mythos release say they spent $20k? I'm also skeptical of Anthropic here doing essentially what amounts to "vague posting" in an attempt scare everyone and drive up their value before IPO.

> > **discordianfish**: Please, go ahead!

> > **pdntspa**: whooptie fuggin doo, then spend $200 on finding and fixing the issues before you push your commits to the cloud

> > **ErroneousBosh**: > since it takes my 16 year old neighbors son 15 mins and $100 claude code credits to hack your open source project
> > 
> > To what end? You can just look at the code. It's right there. You don't need to "hack" anything.
> > 
> > If you want to "hack on it", you're welcome to do so.
> > 
> > Would you like to take a look at some of my open-source projects your neighbour's kid might like to hack on?

> **quotemstr**: They probably lack a sufficient density of people who remember *why* "security through obscurity" become an infamous concept. It belongs to that family of bad ideas that's superficially appealing, especially if you're still at that stage of your career at which you think past generations were full of idiots and you, alone, have discovered how to do *real* software development.

---

### theahura

I'm sorta suspicious. I don’t really think this is why they are moving to closed source. It’s true that there is more security risk, but that actually justifies being open source, because open source tooling can spend more tokens hardening itself against security vulns than closed source tooling (at least, that’s the theory). My strong hunch is they are moving to closed source because it is now trivial to copy a product with AI clean rooms. Which, tbf, is a totally valid reason to move closed source. But I'd want to see more adoption of something like the Ship of Theseus license ([https://github.com/tilework-tech/nori-skillsets/pull/465/cha...](https://github.com/tilework-tech/nori-skillsets/pull/465/changes)) before giving up on open source entirely

> **sgbeal**: >  My strong hunch is they are moving to closed source because it is now trivial to copy a product with AI clean rooms. Which, tbf, is a totally valid reason to move closed source.
> 
> Since such "clean room" implementations ostensibly do not see the source, it's arguably irrelevant whether such sources are open are not. Such implementations will happen regardless of whether the sources they're reimplementing are opened or closed.

> **ezekg**: I very much doubt that addendum would hold up to a lawyer.

---

### opem

> When we started Cal.com, we believed deeply in open source.

No you certainly didn't, otherwise you shouldn't have come up with such a meaningless excuse!

---

### Tepix

The AI companies profit *hugely* from open source. In fact, without open source, their most significant financial success (coding assistants) wouldn't exist.

They should provide free *continued* git commit security analysis for open source projects. That would increase the quality of open source projects and would inspire more projects to go open source, which is also a win for the AI companies.

> **alienbaby**: This was my thought too. Your tool is great at finding vulnerabilities, and we want software to be secure for everyone, secure code should not be out of reach to those who can't afford it.
> 
> Scan everyone's code, for free. Make all code as secure as an llm can make it as a baseline.

---

### tudorg

It's funny that this news showed up just as we (Xata) have gone the other direction, citing also changes due to AI: [https://xata.io/blog/open-source-postgres-branching-copy-on-...](https://xata.io/blog/open-source-postgres-branching-copy-on-write)

We did consider arguments in both directions (e.g. easier to recreate the code, agents can understand better how it works), but I honestly think the security argument goes for open source: the OSS projects will get more scrutiny faster, which means bugs won't linger around.

Time will tell, I am in the open source camp, though.

> **microflash**: Just wanted to appreciate the open-source work by Xata. I’ve been eyeing pgroll [1] for schema migrations after Liquibase license shenanigans (the only barrier for me is json-based migration instead of sql-based migrations)
> 
> [1] [https://github.com/xataio/pgroll](https://github.com/xataio/pgroll)

---

### aswerty

Surely the argument is just to have an LLM stressing for vulnerabilities during the build pipeline before merging to main? Resulting in better security from LLMs.

One must assume this was a direction they wanted to move towards and this is the  justification they thought would be most palatable.

---
