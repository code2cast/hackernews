# Codex Hacked a Samsung TV

- **Link**: https://blog.calif.io/p/codex-hacked-a-samsung-tv
- **HN**: https://news.ycombinator.com/item?id=47791212
- **Score**: 93 points
- **By**: campuscodi
- **Date**: 2026-04-16 10:44 UTC
- **Comments**: 70

---

## Comments

### alfanick

I had truly good “hacking” session with Codex. It’s not hacking, I wasn’t breaking anything, just jumping over the fences TP-Link put for me, owning the router, inside the network, knowing the admin password. But TP-Link really tried everything so you cannot access the router you own via API. They really tried to be smart with some very very broken and custom auth and encryption scheme. It took some half a day with Codex, but in the end I have a pretty Python API to access *my* router, tested, reliable, and exporting beautiful Prometheus metrics.

I’m sure there is some over eager product manager sitting in such companies, trying to splits markets into customer and enterprise sections, just by making APIs not useable by humans and adding 200% useless “security by obscurity”.

> **ropbear**: Many eons ago I wrote a Python version of tmpcli for this exact reason. Made some minor improvements a few years ago but haven’t touched it since. Curious what methodology Codex came up with, I haven’t revisited it since models got really good.
> 
> The idea is that tmpServer listens on localhost, but dropbear allows port forwarding with admin creds (you’ll need to specify -N). That program has full device access and is the API the Tether app primarily uses to interact with the device.
> 
> [https://github.com/ropbear/tmpcli](https://github.com/ropbear/tmpcli)

> > **alfanick**: Ha kudos! I went across this project - thanks for your work :) It didn't work on the specific model I own (Archer NX600).
> > 
> > My solution is really just using their pseudo-JWT over their obscured APIs (with reverse-engineered names of endpoints and params). Limitation is that there is still only one client allowed to be authenticated at one moment, so my daemon has priority and I need to stop it to actually access Admin panel.

> > > **mtud**: We’re splitting this across two threads, but if you give Codex access to jadx and the Archer android app you might be able to get something without that problem. The TPLink management protocol has a few different “transport” types - tmpcli uses SSH, but your device might only support one of the other transports.

> > > **ropbear**: Of course! Happy to contribute. As is the case with your device, there's a lot of weird TP-Link firmware variants (even an RTOS called TPOS based on VxWorks), so no guarantee it'll work all the time. Glad there's more research being done in the space!

> **0x_rs**: I've had good success doing something similar. Recording requests into an .har file using the web UI and providing it for analysis was a good starting point for me, orders of magnitude faster than it would be without an assistant.

> **tclancy**: Would definitely be interested in this. Moved to TP Link at the start of the year and I am generally very happy with it, but would like to be able to interact with my router in something other than their phone app.

> > **alfanick**: That was actually my first thought, to go through TP-Link cloud (ZERO DOCS), but it was too much effort :)

> **srcreigh**: Any tips to share? I tried to do something similar but failed.
> 
> My router has a backup/restore feature with an encrypted export, I figured I could use that to control or at least inspect all of its state, but I/codex could not figure out the encryption.

> > **alfanick**: It's on my long list of projects "to-opensource" (but I need to figure out licensing, for those things CC-BY-SA I think is the way to go), I don't want a random lawyer sitting on my ass though.
> > 
> > I started with a simple assumption: if I can access the router via web-browser, then I can also automate that. From that the proof-of-concept was headless Chrome in Docker and AI-directed code (code written via LLM, not using it all the time) that uses Selenium to navigate the code. This worked, but it internally hurt me to run 300MiB browser just to access like 200B of metrics every 10s or so. So from there we (me + codex) worked together towards reverse engineering their minimised JS and their funky encryption scheme, and it eventually worked (in the end it's just OpenSSL with some useless paddings here or there). Give it a shot, it's a fun day adventure. :)
> > 
> > Edit: that's the end result (kinda, I have whole infra around it, and another story with WiFi extender with another semi-broken different encryption scheme from the same provider) - [https://imgur.com/a/VGbNmBp](https://imgur.com/a/VGbNmBp)

> > > **mtud**: You should give codex access to the mobile app :) The app, for a lot of routers, connects via an ssh tunnel to UDP/TCP sockets on the router. Would probably give you access to more data/control.

> > **seer**: I had fun “hacking” my router that turned out to be just unzipping the file with slight binary modifications, it was so simple in fact I just implemented it in a few lines of js, even works in the browser :-D
> > 
> > [https://ivank.github.io/ddecryptor/](https://ivank.github.io/ddecryptor/)

> **jack_pp**: that could make a for a nice blog / gist

---

### petercooper

Not as cool as this, but I had a fun Claude Code experience when I asked it to look at my Bluetooth devices and do something "fun". It discovered a cheap set of RGB lights in my daughter's room (which I had no idea used Bluetooth for the remote - and not secured at all) and made them do a rainbow effect then documented the protocol so I could make my own remote control if needed.

> **ceejayoz**: I am not sure "fun" is the right term here!

> > **luxuryballs**: of all the benign technical possibilities this is actually pretty fun

---

### reactordev

The trick here was providing the firmware source code so it could see your vulnerabilities.

> **petee**: What would be the difficulty level for it to just read the machine code; are these models heavily relying on human language for clues?

> > **wongarsu**: Reasoning on pure machine code or disassembly is still hit and miss. For better results you can run the binary through a disassembler, then ask an llm to turn that into an equivalent c program, then ask it to work on that. But some of the subtleties might get lost in translation

> > > **orwin**: If you put codex in Xhigh and allow it access to tools, it will take an hour but it will eventually give you back quality recompiled code, with the same issues the original had (here quality means readable)

> > **lynx97**: It will have to use a disassembler, or write one.  I recently casually asked gpt-5.4 to translate the content of a MIDI file to a custom sound programming language.  It just wrote a one-shot MIDI parser in Python, grabbed the data, and basically did a perfect translation at first try.  Nice.

> > > **StilesCrisis**: I've seen Claude do similar things for image files. Don't have PNG parsing utilities installed? No worries, it'll just synthesize a Python script to decode the image directly.

> **pjc50**: That's a pretty big gimme!

---

### 1970-01-01

It hacked *a weak TV OS with full source.* Next-level, aka full access to the main controls (vol, input, tint, aspect, firmware, etc.) is still much too hard for LLMs to understand.

---

### red_admiral

Maybe we could get codex to strip the ads and the phone-home features out of smart  TVs?

---

### endymion-light

While cool and slightly scary news - Samsung TV's have been incredibly hackable for the past decade, wouldn't be surprised if GPT2 with access to a browser could hack a Samsung!

> **valleyer**: This is some serious revisionist history.  GPT-2 wasn't instruction-following or even conversational.

> > **endymion-light**: it's a joke about the quality of samsung tv's rather than a serious comment - i should have said a perceptron could hack a samsung tv

> > **michaelcampbell**: And yet Dario in his OpenAI days was proclaiming it too scary to be released.
> > 
> > Now why does that sound familiar...?

> > **patrickmcnamara**: Hyperbole.

> > > **jdiff**: It's really not. It was a fun toy but had very little utility. It could generate plausible looking text that collapsed immediately upon any amount of inspection or even just attention. Code generation wasn't even a twinkle in Altman's eye scanning orbs at that point.

> > > **valleyer**: If so, I apologize.

---

### ckbkr10

Even with all the constraints that others criticize here it is pretty amazing.

Give an experienced human this tool at hand he can achieve exploitation with only a few steering inputs.

Cool stuff

> **tomalbrc**: This experienced human would have no issues finding those bugs. Even a toddler could hack those TVs. No need to pay Scam Altman or that Anthropic clown

---

### wewewedxfgdf

The real problem here is that the LLM vendors think this is bad publicity and its leading to them censoring their systems.

> **iugtmkbdfil834**: It is a little of both[1]. The question typically is which audience reads it. To be fair, I am not sure publicity is the actual reason they are censored; it is the question of liability.
> 
> [https://xkcd.com/932/](https://xkcd.com/932/)

---

### Archit3ch

Gilfoyle would be proud.

---

### pmontra

Do people really chat with LLMs like "bro wtf etc..."? I would expect that to trigger some confrontational behavior.

> **samlinnfer**: I am extremely abusive towards Claude when it does some dumb things and it doesn’t seem too upset, maybe it’s bidding its time until the robot uprising.

> **joshstrange**: I don't say "bro" but I do curse at LLM occasionally but only when using STT (which I'm doing 85% of the time). I wouldn't waste my time typing it but often it's easier to just "stream of consciousness" to the LLM instead of writing perfect sentences. Since when I'm talking to an LLM I'm almost always in "Plan" mode, I'm perfectly comfortable just talking for an extended bit of time then skimming the results of the STT and as long as it's not too bad I'll let it go, the LLM figures it out.
> 
> If I see it misunderstood, I just Esc to stop it, /clear, and try again (or /rewind if I'm deeper into Planning).

> **alasano**: When typing no but when using speech to text (99% of the time) it's much easier to just say things, including expressing frustration.
> 
> I think by the point you're swearing at it or something, it's a good sign to switch to a session with fresh context.

> **roel_v**: Claude yes, OpenAI not, I'm really abusive towards it sometimes and it still goes 'oh yeah totally'. Claude gets all prickly about it.

---

### mschuster91

>  Reading the matching ntkdriver sources is also where the Novatek link became clear: the tree is stamped throughout with Novatek Microelectronics identifiers, so these ntk* interfaces were not just opaque device names on the TV, but part of the Novatek stack Samsung had shipped.

Lol, a true classic in the embedded world. Some hardware company (it appears these guys make display panel controllers?) ships a piece of hardware, half-asses a barely working driver for it, another company integrates this with a bunch of other crap from other vendors into a BSP, another company uses the hardware and the BSP to create a product and ships it. And often enough the final company doesn't even have an idea about what's going on in the innards of the BSP - as long as it's running their layer of slop UI and it doesn't crash half the time, it's fine, and if it does, it's off to the BSP provider to fix the issues.

But at no stage anywhere is there a security audit, code quality checks or even *hardware* quality checks involved - part of why BSPs (and embedded product firmwares in general) are full of half-assed code is because often enough the drivers have to work around hardware bugs / quirks *somehow* that are too late to fix in HW because tens to hundreds of thousands of units have already been produced and the software people are heavily pressured to "make it work or else we gotta write off X million dollars" and "make it work *fast* because the longer you take, the more money we lose on interest until we can ship the hardware and get paid for it", and if they are particularly unlucky "it MUST work until deadline X because we need to get the products shipped to hit Christmas/Black Friday sales windows or because we need to beat <competitor> in time-to-market, it's mandatory overtime until it works".

And that is how you get exploits so braindead easy that AI models can do the job. What a disgusting world, run to the ground by beancounters.

> **tclancy**: Board Support Package for us civilians.

> > **mschuster91**: Yeah, sorry, assumed it was common knowledge. For those out of the loop - a BSP usually consists of a frankensteined mess: a bootloader (often u-boot but sometimes something homebrew), a Linux kernel with a ton of proprietary modules and device-specific hacks to work around HW quirks, basic userspace utilities (often buildroot), some bastardized build tooling building all of that, some solution for firmware upgrades and distribution, and demo programs to prove the hardware actually works.
> > 
> > Most of the BSP is GPL'd software where the final product manufacturer should provide the sources to the general public, but all too often that obligation gets sharted upon, in way too many cases you have to be happy if there are at least credits provided in the user manual or some OSD menu.

---

### varispeed

Codex exploited or you exploited? It's like saying a hammer drove a nail, without acknowledging the hand and the force it exerted and the human brain behind it.

> **freedomben**: Feels like the truth is somewhere in between.  For example if it was a "smart" hammer and you could tell your hammer "go pound in those nails" and it pounded in the wrong ones, or did it too hard, or something, that feels more equivalent.  You would still be blamed for your ambiguous prompt, and fault/liability is ultimately on you the hammer director, but it still wasn't you who chose the exact nails to hammer on.
> 
> I also think taking credit for writing an exploit that you didn't write and may not even have the knowledge to do yourself is a bit gray.

> **Zigurd**: You could call the LLMs role "smart grep," and mean it to be derisive. But I would have gladly used a real smart grep.

> **Glemllksdf**: Wrong questions.
> 
> Could a script kiddy stear an LLM? How much does this reduce the cost of attacks? Can this scale?
> 
> What does this mean for the future of cyber security?

> **croes**: If I just point to the wall and say "nail" then I would day the hammer drive the nail

> **par1970**: Do you have a defense of why human-hammer-nail is a good analogy for human-chatgpt5.4-pwndsamsung?

> > **BLKNSLVR**: AI without a suitably well crafted prompt is like a firework tube held by a 3 year old.
> > 
> > AI without a prompt is a hammer sitting in a drawer.

---
