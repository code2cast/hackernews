# Darkbloom – Private inference on idle Macs

- **Link**: https://darkbloom.dev
- **HN**: https://news.ycombinator.com/item?id=47788542
- **Score**: 354 points
- **By**: twapi
- **Date**: 2026-04-16 04:06 UTC
- **Comments**: 172

---

## Comments

### jonhohle

> That is not a technology problem. It is a marketplace problem.

I cringe every time I see this sentence structure. I know the joke is about emdashes, but the “Its not …. It’s ….” drives me crazy.

> **sergiusignacius**: I see it everywhere now, it's even in videos and how people talk.

> **nnevatie**: Only an em dash missing in between to be chefs-kiss-perfect.

---

### kennywinker

I have a hard time believing their numbers. If you can pay off a mac mini in 2-4 months, and make $1-2k profit every month after that, why wouldn’t their business model just be buying mac minis?

> **dgacmu**: No provider maintains 100% utilization of GPUs at full rate. Demand is bursty - even if this project is successful, you might expect, e.g., things to be busy during the stock market times when Claude is throwing API errors and then severely underutilized during the same times that Anthropic was offering two-for-one off peak use.
> 
> And then there's a hit for overprovisioning in general. If the network is not overprovisioned somewhat, customers won't be able to get requests handled when they want, and they'll flee. But the more overprovisioned it is, the worse it is for compute seller earnings.
> 
> I suspect an optimistic view of earnings from a platform like this would be something like 1/8 utilization on a model like Gemma 4. Their calculator estimates my m4 pro mini could earn about $24/month at 3 hours/day on that model. That seems plausible.

> **avidphantasm**: If you start buying minis, then you need to house, power, and cool them. So you are building a mini data center. If you are building a small data center, economies of scale will drive you to want to build larger and larger. However, this gets expensive and neighbors tend to not like data centers (for good reason). To me this seems like asymmetric warfare against hyper-scalers.

> **eigengajesh**: The numbers are optimistically legit -- it's calculated based purely considering we have demand for all machines at all times. We don't have that right now, but fairly optimistic that people will do it.
> 
> That's why we don't recommend purchasing a new machine. Existing machine is no cost for you to run this.
> 
> Electricity is one cost, but it will get paid off from every request it receives. Electricity is only deducted when you run an inference. If you have any questions, DM me @gajesh on Twitter.

> > **stavros**: You're not taking into account the thermal strain on the machine, though. A machine that's 100% utilized (even worse if it's in bursts) will last less than an idle machine.

> > > **washadjeffmad**: Not appreciably, and not before a 5-yr AppleCare+ warranty expires.
> > > 
> > > Out of our >3000 currently active Apple Silicon Macs, failures due to non-physical damage are in the single digits per year. Of those, none have been from production systems with 24/7 uptime and continuous high load, which reflects your parenthetical.
> > > 
> > > Perhaps we haven't met the other end of the bathtub curve yet, but we also won't be retaining any of these very far beyond their warranty period, much less the end of their support life.

> > > **embedding-shape**: > A machine that's 100% utilized (even worse if it's in bursts) will last less than an idle machine.
> > > 
> > > How much though? Say I have three Mac Minis next to each other, one that is completely idle but on, one that bursts 100% CPU every 10 minutes and one that uses 100% CPU all the time, what's the difference on how long the machines survives? Months, years or decades?

> **psychoslave**: Because they don’t have that much initial money in their pocket, while the idle computer is already there, and the biggest friction point is convincing people to install some software. Both producing rhetoric and software are several order of magnitude cheaper than to directly own and maintain a large fleet of hardware with high guarantee of getting the electrical stable input in a safe place to store them.
> 
> Assuming that getting large chunk of initial investment is just a formality is out of touch with 99% of people reality out there, when it’s actually the biggest friction point in any socio-economical endeavour.

> **chaoz_**: Solid q. I think the part of it is that it’s really easy to attract some “mass” (capital) of users, as there are definitely quite a few of idle Macs in the world.
> 
> Non-VC play (not required until you can raise on your own terms!) and clear differentiation.
> 
> If you want to go full-business-evaluation, I would be more worried about someone else implementing same thing with more commission (imo 95% and first to market is good enough).

> > **jonplackett**: I think the point they’re making though is that the numbers seem too good to be true.
> > 
> > ie. Does anyone know the payback time for a B100 used just for inference? I assume it’s more than a couple of months? Or is it just training that costs so much?

> > **Saline9515**: Eigenlayer (which this is spun off from) is a massively VC-funded crypto company.

> **dnnddidiej**: It is too good to be true. When you see it is making more than a claude code subscription for fuck all work per day.
> 
> Prolly gonna make $50 a year tops.

> **thih9**: > These are estimates only. We do not guarantee any specific utilization or earnings. Actual earnings depend on network demand, model popularity, your provider reputation score, and how many other providers are serving the same model.
> 
> Others are reporting low demand, eg.: [https://news.ycombinator.com/item?id=47789171](https://news.ycombinator.com/item?id=47789171)

> **znnajdla**: The numbers are obviously high, because if this takes off then the price for inference will also drop. But I still think it’s a solid economic model that benefits low income countries the most. In Ukraine, for example, I know people who live on $200/month. A couple Mac Minis could feed a family in many places.
> 
> As a business owner, I can think of multiple reasons why a decentralized network is better for me as a business than relying on a hyperscaler inference provider. 1. No dependency on a BigTech provider who can cut me off or change prices at any time. I’m willing to pay a premium for that. 2. I get a residential IP proxy network built-in. AI scrapers pay big money for that. 3. No censorship. 4. Lower latency if inference nodes are located close to me.

> > **kennywinker**: How many of those people who could live off $200USD/month can afford or already have a mac mini in the house?

> > > **znnajdla**: They already have an iPhone. They could save up or borrow for a Mac Mini if they had to. Some of those people I know who live on $200/month have $30k in the bank.

> > **aacid**: Isn't this same premise as "lets buy few GPUs to mine crypto and have passive income"?
> > It didn't work very well and it probably won't work now either. If there is money to be made, bigger players will get in there, buy out all mac minis they can, drive price up for regular people and inevitably drive inference price down so you'll be lucky to get initial investment back

> > > **znnajdla**: No it's not the same premise at all. Crypto doesn't do anything useful for legitimate businesses. AI inference is very useful for legitimate businesses, and so are residential IP proxies for scraping. And by definition, residential IPs cannot be centralized. And as building GPUs becomes more expensive, the existing pool of second hand unused hardware becomes more valuable, not less. The problem with crypto mining is that it quickly becomes unprofitable for small scale deployments. I'm not sure if AI inference would be, especially for the decentralized benefits of lower latency.

> > **NiloCK**: On the latency point - your requests are still going through the coordinator of the system here. So on average strictly worse than a large provider.
> > 
> > You - Darkbloom - Operator - Darkbloom - you, vs
> > 
> > You - Provider - you
> > 
> > ---
> > 
> > On the censorship point - this is an interesting risk surface for operators. If people are drawn my decentralized model provisioning for its lax censorship, I'm pretty sure they're using it to generate things that I don't want to be liable for.
> > 
> > If anything, I could imagine *dumber* and *stricter* brand-safety style censorship on operator machines.

> > > **znnajdla**: I'm not talking about Darkbloom specifically, but rather this business model in general. I'm sure a future version of Darkbloom could be P2P for better latency. Or their central operator nodes could be geo-balanced. Liability for censorship doesn't matter if it's truly zero trust. Anyway censorship is not my main concern. Low-latency decentralized inference with no US BigTech dependency is a much bigger selling point in Europe.

> > **yard2010**: It's quite funny thinking about a chimpanzee seeing a lot of bananas thinking this could feed my family and then same with humans only with Mac Minis

> **gleenn**: Power and racking are difficult and expensive?

> > **kennywinker**: How difficult? Is running 1000 minis worth $1,000,000/month of effort? I feel like it is.

> > > **ffsm8**: And at that scale (1k) it ain't even that hard, a single room could be enough to hazardly drop them on shelves with a big fan to draw out the heat

> > > **runako**: There are many people who do not have ready access to a million dollars to purchase said Mac minis, much less the operating capital to rack & operate them.
> > > 
> > > Very smart play to build a platform, get scale, and prove out the software. Then either add a small network fee (this could be on money movement on/off platform), add a higher tier of service for money, and/or just use the proof points to go get access to capital and become an operator in your own pool.

> **Filligree**: Because their numbers don’t work out. When you do the math on token cost versus inference speed, you get something that barely breaks even even with cheap power.
> 
> Also they’ve already launched a crypto token, which is a terrible sign.

> **znpy**: Being the middleman is often way more profitable

> **agnosticmantis**: "You could see a single robotaxi being worth, or providing, about $30,000 of gross profit per year.
> ... A Tesla is an appreciating asset..."
> 
> - Elon Musk during Tesla's Autonomy Day in April 2019.

> **foota**: Capital and availability?

> > **kennywinker**: I guess if it only works at scale capital is maybe the answer. Like enough cash to buy 5 or 10 or even 100 minis seem doable - but if the idea only works well when you have 10,000 running - that makes some sense.

---

### tgma

I installed this so you don't have to. It did feel a bit quirky and not super polished. Fails to download the image model. The audio/tts model fails to load.

In 15 minutes of serving Gemma, I got precisely zero actual inference requests, and a bunch of health checks and two attestations.

At the moment they don't have enough sustained demand to justify the earning estimates.

> **splittydev**: They released this like a day ago, I'm not surprised that there's not enough demand right now. Give it some time to take off

> > **tgma**: You'd think to bootstrap a marketplace you'd spend your own money to feed fake requests (or perhaps allow free chat so that they induce requests).
> > 
> > Still, absolute *zero* is an unacceptable number. Had this running for more than an hour.

> > > **splittydev**: I kind of see your point, but I also kind of don't.
> > > 
> > > Sure, it would be great if you'd immediately get hammered with hundreds of requests and start make money quickly. It would also be great if it was a bit more transparent, and you could see more stats (what counts as "idle"? Is my machine currently eligible to serve models?). But it's still very new, I'd say give it some time and let's see how it goes.
> > > 
> > > If you have it running and you get zero requests, it uses close to zero power above what your computer uses anyway. It doesn't cost you anything to have it running, and if you get requests, you make money. Seems like an easy decision to me.

> **subroutine**: Has anyone tested the system from the other end... sending a prompt and getting a response?

> **lxglv**: weird to learn that they do not generate inference requests to their network themselves to motivate early adopters at least to host their inference software

> > **lostmsu**: If they paid promised > $1k/m for FLUX 2B on a Mac they would go broke in less than a month. On a single 5090 that model would provide an inference througput so high they'd have to pay close to $50k/m for the results.
> > 
> > The numbers are absolute fraud. You shouldn't be installing their software cause fraud could be not just about numbers.

> > > **rjmunro**: Can you rephrase that? I don't think I've read it correctly. It sounds like you are saying it would normally cost $50k on a 5090 and they can do equivalent work paying $1k. That's sounds like a $49k profit margin, but you say they will go broke.

> **thatxliner**: and I don't think they ever will unless they're highly competitive (hopefully that price they have stays? at least for users)
> 
> I was thinking of building this exact thing a year ago but my main stopper was economics: it would never make sense for someone to use the API, thus nobody can make money off of zero demand.
> 
> I guess we just have to look at how Uber and Airbnb bootstrapped themselves. Another issue with my original idea was that it was for compute in general, when the main, best use-case, is long(er)-running software like AI training (but I guess inference is long running enough).
> 
> But there already exist software out there that lets you rent out your GPU so...

> > **tgma**: People underestimate how efficient cost/token is for beefy GPUs if you are able to batch. Unlikely for one off consumer unit to be able to compete long term.

> > **starkeeper**: What's a good place to do this?

> > > **lostmsu**: For Windows there's [https://borg.games/setup](https://borg.games/setup) (I'm the author).

---

### gleenn

You have to install their MDM device management software on your computer. Basically that computer is theirs now. So don't plan on just handing over your laptop temporarily unless you don't mind some company completely owning your box. Still might be a validate use for people with slightly old laptops lying around, but beware trying to share this computer with your daily activities if you e.g. use a bank on a browser on this computer regularly. MDM means they can swap out your SSL certs level of computer access, please correct me if I'm wrong.

> **mirashii**: MDMs on macOS are permissioned via AccessRights, and you can verify that their permission set is fairly minimal and does not allow what you've described here (bits 0, 4, 10).
> 
> That said, their privacy posture at the cornerstone of their claims is snake oil and has gaping holes in it, so I still wouldn't trust it, but it's worth being accurate about how exactly they're messing up.

> > **mike_hearn**: Edit: deleted post. I see your other post now.
> > 
> > You are right - the "nonce binding" the paper uses doesn't seem convincing. The missing link is that Apple's attestation doesn't bind app generated keys to a designated requirement, which would be required to create a full remote attestation.

> > > **mirashii**: > If you can prove a public key is generated by the SEP of a machine running with all Apple's security systems enabled, then you can trivially extend that to confidential computing because the macOS security architecture allows apps to block external inspection even by the root user.
> > > 
> > > It only effectively allows this for applications that are in the set of things covered by SIP, but not for any third-party application. There's nothing that will allow you to attest that arbitrary third-party code is running some specific version without being tampered with, you can only attest that the base OS/kernel have not been tampered with. In their specific case, they attempt to patch over that by taking the hash of the binary, but you can simply patch it before it starts.
> > > 
> > > To do this properly requires a TEE to be available to third-party code for attestation. That's not a thing on macOS today.

> **keremimo**: MDM is the absolute deal breaker. No way in hell will I ever make my Macbook into an unsellable brick if they so decide to lock my computer with MDM.
> 
> Even moreso, not for pennies/month

---

### nl

They use the TEE to check that the model and code is untampered with. That's a good, valid approach and should work (I've done similar things on AWS with their TEE)

The key question here is how they avoid the outside computer being able to view the memory of the internal process:

> An in-process inference design that embeds the in-
ference engine directly in a hardened process, elimi-
nating all inter-process communication channels that
could be observed, with optional hypervisor mem-
ory isolation that extends protection from software-
enforced to hardware-enforced via ARM Stage 2 page
tables at zero performance cost.[1]

I was under the impression this wasn't possible if you are using the GPU. I could be misled on this though.

[1] [https://github.com/Layr-Labs/d-inference/blob/master/papers/...](https://github.com/Layr-Labs/d-inference/blob/master/papers/dginf-private-inference.pdf)

> **flockonus**: While they do make this argument, realistically anyone sending their prompt/data to an external server should assume there will be some level of retention.
> 
> And more so in particular, anyone using Darkbloom with commercial intents should only really send non-sensitive data (no tokens, customer data, ...) I'd say only classification tasks, imagine generation, etc.

> > **joelthelion**: There's a difference between trusting Anthropic and trusting random mac owners.

> **nitros**: This entire paper smells of LLM, I'm sure even the most distinguished academic would refrain from using notation to prove that the SIP status cannot change during operation.

> **mike_hearn**: Apple Silicon systems have unified memory between CPU and GPU. The hypervisor page table trick is thus claimed to protect GPU memory from RDMA.

> **ramoz**: Macs do not have an accessible hardware TEE.
> 
> Macs have secure enclaves.

> > **nl**: Good point!
> > 
> > But they argue that:
> > 
> > > PT_DENY_ATTACH (ptrace constant 31): Invoked
> > at process startup before any sensitive data is loaded.
> > Instructs the macOS kernel to permanently deny all
> > ptracerequests against this process, including from
> > root. This blocks lldb, dtrace, and Instruments.
> > 
> > > Hardened Runtime: The binary is code-signed with
> > hardened runtime options and explicitly without the
> > com.apple.security.get-task-allow
> > entitlement. The kernel denies task_for_pid()
> > and mach_vm_read()from any external process.
> > 
> > > System Integrity Protection (SIP): Enforces both of
> > the above at the kernel level. With SIP enabled, root
> > cannot circumvent Hardened Runtime protections, load
> > unsigned kernel extensions, or modify protected sys-
> > tem binaries. Section 5.1 proves that SIP, once verified,
> > is immutable for the process lifetime.
> > 
> > gives them memory protection.
> > 
> > To me that is surprising.

> > > **mirashii**: Looking at their paper at [1], there's a gaping hole: there's no actual way to verify the contents of the running binaries. The binary hash they include in their signatures is self-reported, and can be modified. That's simply game over.
> > > 
> > > [1] [https://github.com/Layr-Labs/d-inference/blob/master/papers/...](https://github.com/Layr-Labs/d-inference/blob/master/papers/dginf-private-inference.pdf)

> > > **dinobones**: Couldn't someone just uhh... patch their macOS/kernel, mock these things out, then behold, you can now access all the data?
> > > 
> > > If it's not running fully end to end in some secure enclave, then it's always just a best effort thing. Good marketing though.

> > > **saagarjha**: They quite frankly have no idea what they are talking about.

> > > **ramoz**: I'm not arguing anything. This is how it works. There is no but.
> > > 
> > > Protection here is conditional, best-effort. There are no true guarantees, nor actual verifiability.

---

### dgacmu

@eigengajesh - Your cost estimator lists Mac Mini M4 Pro with only 24 or 48GB options, but the M4 Pro mini can also be configured with 64GB. At least, I hope so, as I'm typing this on one. ;-)

---

### ramoz

Unfortunately, verifiable privacy is not physically possible on MacBooks of today.  Don't let a nice presentation fool you.

Apple Silicon has a Secure Enclave, but not a public SGX/TDX/SEV-style enclave for arbitrary code, so these claims are about OS hardening, not verifiable confidential execution.

It would be nice if it were possible. There's a lot of cool innovations possible beyond privacy.

> **mike_hearn**: I wrote a whole SDK for using SGX, it's cool tech. But in theory on Apple platforms you can get a long way without it. iOS already offers this capability and it works OK.
> 
> macOS has a strong enough security architecture that something like Darkbloom would have at least some credibility if there was a way to remotely attest a Mac's boot sequence and TCC configuration combined with key-to-DR binding. The OS sandbox can keep apps properly separated if the kernel is correct and unhacked. And Apple's systems are full of mitigations and roadblocks to simple exploitation. Would it be as good as a consumer SGX enclave? Not architecturally, but the usability is higher.

> **znnajdla**: As if you get privacy with the inference providers available today? I have more trust in a randomly selected machine on a decentralized network not being compromised than in a centralized provider like OpenAI pinky promising not to read your chats.

> > **ramoz**: Inference providers don't claim private inference. However, they must uphold certain security and legal compliances.
> > 
> > You have no guarantees over any random connected laptop connected across the world.

> > > **znnajdla**: I would say the chances of OpenAI itself getting hacked and your secrets in logs getting leaked are about the same or less as the chances of a randomly selected machine on a decentralized network being reverse-engineered by a determined hacker. There's no risk-free option, every provider comes with risks. If you care about infosec you have to do frequent secret rotation anyway.

> **geon**: Every hardware key will be broken if there is enough incentive to do so. Their claims read like pure hubris.

> > **znnajdla**: Who cares about AI privacy? Most people don’t. If you do, run locally.

---

### jaffee

client side of this kind of needs to be open source unless I'm running it on a dedicated machine and firewalling it from the rest of my network. Or the company needs to have a very strong reputation and certifications. curlbash and go is a pretty hard sell for me

---

### pants2

Cool idea. Just some back-of-the-envelope math here (not trusting what's on their site):

My M5 Pro can generate 130 tok/s (4 streams) on Gemma 4 26B. Darkbloom's pricing is $0.20 per Mtok output.

That's about $2.24/day or $67/mo revenue if it's fully utilized 24/7.

Now assuming 50W sustained load, that's about 36 kWh/mo, at ~$.25/kWh approx. $9/mo in costs.

Could be good for lunch money every once in a while! Around $700/yr.

> **mavamaarten**: Well. Running your machine to do inference will utilize more than 50W sustained load, I'd say more than double that. Plus electricity is more expensive here (but granted, I do have solar panels). Plus don't forget to factor in that your hardware will age faster.
> 
> I'd say it's not worth it. But the idea is cool.

> > **jorvi**: Your hardware will age *slower* if you have consistent load.
> > 
> > Thermal stress from bursty workloads is much more of a wearing problem than electromigration. If you can consistently keep the SoC at a specific temperature, it'll last much longer.
> > 
> > This is also why it was very ironic that crypto miner GPUs would get sold at massive discounts. Everyone assumed that they had been ran ragged, but a proper miner would have undervolted the card and ran it at consistent utilization, meaning the card would be in better condition than a secondhand gamer GPU that would have constantly been shifting between 1% to 80% utilization, or rather, 30°C to 75°C

> > **kennywinker**: Their estimate is based on significantly lower consumption when under load. E.g. 25W for an M4 Pro mac mini. I have no idea if that’s realistic - but the m4s are supposedly pretty efficient ([https://www.jeffgeerling.com/blog/2024/m4-mac-minis-efficien...](https://www.jeffgeerling.com/blog/2024/m4-mac-minis-efficiency-incredible/))

> **torginus**: Also this assumes hardware never fails. I learned about this the hard way back when I started mining crypto on my 5700XT way back when.
> 
> I figured since I already used it a lot, and I've never had a GPU fail on me, it would be fine.
> 
> The fans on it died in a month of constant use, replacing them was more money than what I made on mining.

> **kennywinker**: Their example big earner models are FLUX.2 Klein 4B and FLUX.2 Klein 9B, which i imagine could generate a lot more tokens/s than a 26B model on your machine.
> 
> For Gemma 4 26B their math is:
> 
> single_tok/s = (307 GB/s / 4 GB) * 0.60 = 46.0 tok/s
> 
> batched_tok/s = 46.0 * 10 * 0.9 = 414.4 tok/s
> 
> tok/hr = 414.4 * 3600 = 1,492,020
> 
> revenue/hr = (1,492,020 / 1M) * $0.200000 = $0.2984
> 
> I have no idea if that is a good estimate of how much an M5 Pro can generate - but that’s what it says on their site.
> 
> They do a bit of a sneaky thing with power calculation: they subtract 12Ws of idle power, because they are assuming your machine is idling 24/7, so the only cost is the extra 18W they estimate you’ll use doing inference. Idk about you, but i do turn my machine off when i am not using it.

> > **pants2**: Interesting token numbers they're using, because I've benchmarked it at 69 tok/s single steam and 130 multi stream.

> **nnx**: > My M5 Pro can generate 130 tok/s (4 streams) on Gemma 4 26B.
> 
> This seems high. At which quantization? Using LM Studio or something else?
> 
> Note: Darkbloom seems to run everything on Q8 MLX.

> > **pants2**: Ah good point, this is using Q4, benchmarked total throughout serving with Llama.cpp.

> **todotask2**: OpenAI has only about 5% paying customers, how does it generate revenue?
> 
> I don’t think this is a sustainable business model. For example, Cubbit tried to build decentralised storage, but I backed out because better alternatives now exist, and hardware continues to improve and become cheaper over time.
> 
> Your electricity and ownership are going to get lower return and does not actually requce CO2.

> **chaoz_**: Genuinely curious, is there any way to estimate amortization of Mac?
> 
> I’d imagine 1 year of heavy usage would somehow affect its quality.

> > **pants2**: Yeah, only way to get there is assuming they're not giving prompt caching discounts while my laptop is getting prompt caching benefits, with very many large prompts. So yes I am skeptical of their numbers.

> **xendo**: Any idea what makes for such a diff between your and theirs numbers? Batching? Or could they do a crazy prefix caching across all nodes to reduce the actual processing.

> **znnajdla**: Maybe lunch money for you, but there are people in some parts of the world who live on $200/month. Like Ukraine.

> > **sethherr**: But they probably don’t have M5 MacBook pros idling

> > > **tonyedgecombe**: Or reliable energy or internet.

> > > **znnajdla**: They can acquire one if it offers real opportunities like this.

> **MrDrMcCoy**: Don't forget to factor in cooling costs.

> > **pants2**: Or saved heating costs in the winter!

---

### dangoodmanUT

This feels like defi... de-ai

---

### haspok

Having strong SETI@Home vibes from 25 years ago, except of course, this is not for the greater good of humanity, but a for-profit project.

Problem is, from a technical point of view, what kind of made sense back then (most people running desktops, fans always on, energy saving minimal) is kind of stupid today (even if your laptop has no fan, would you want it to be always generating heat?)...

I definitely want my laptops to be cool, quiet and idle most of the time.

> **kamranjon**: My m4 max mbp with 128gb of memory is constantly training 24/7 on weekends- it’s why I bought the thing.

> **vorticalbox**: I some times play about with local models via ollama/comfyui and more recently ace-step to generate music.
> 
> This is short bursts of heat 5-10 m during the render I would not be happy with that for multiple hours a day. I am sure that would have a negative effect on battery health.

---

### alexpotato

Wasn't there an idea about 15 years ago where you would open your browser, go to a webpage and that page would have a JavaScript based client that would run distributed workloads?

I believe the idea was that people could submit big workloads, the server would slice them up and then have the clients download and run a small slice. You as the computer owner would then get some payout.

Intersting to see this coming back again.

> **thekid314**: Or SETI which would search for signs of alien life.

---

### sharts

Too much to read.

---

### podviaznikov

I've tried to install it on my mac, but not sure what macOS version it should support.

on 15.1 it failed to serve models.

updated to latest 15.5 and it fails to run binary.

---

### TuringNYC

I'd love a way to do this locally -- pool all the PCs in our own office for in-office pools of compute. Any suggestions from anyone? We currently run ollama but manually manage the pools

> **damezumari**: [https://github.com/exo-explore/exo](https://github.com/exo-explore/exo)

> **utopiah**: Seems like so much more work than "just" paying for [https://huggingface.co](https://huggingface.co) or whichever other neocloud who already did all the setup for you and just waits for your credit card per minute/seconds/token.

> **zozbot234**: If you set CPUSchedulingPolicy=idle Nice=19 IOSchedulingClass=idle in the ollama server configuration it should run in the background with lowest priority.

---
