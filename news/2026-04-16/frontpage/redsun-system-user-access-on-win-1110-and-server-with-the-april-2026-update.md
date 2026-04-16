# RedSun: System user access on Win 11/10 and Server with the April 2026 Update

- **Link**: https://github.com/Nightmare-Eclipse/RedSun
- **HN**: https://news.ycombinator.com/item?id=47788473
- **Score**: 128 points
- **By**: airhangerf15
- **Date**: 2026-04-16 03:54 UTC
- **Comments**: 30

---

## Comments

### egeozcan

I wonder why Windows Defender has the privilege to alter the system files. Read them for analysis? Sure! Reset (as in, call some windows API to have it replaced with the original), why not? But being able to write sounds like a bad idea.

However, I don't know what I'm talking about so take it with a grain of salt!

> **EvanAnderson**: AV had traditionally run as SYSTEM on Windows (and, in the past, often had kernel mode drivers too). I've always thought it was a terrible idea. It opens up exciting new attack surfaces. Kaspersky and McAfee both had privilege escalation vulnerabilities that I can recall. There have been a ton in multiple products over the years.

> > **labelbabyjunior**: They kind of have to, though.
> > 
> > If malware exploits a privilege escalation vuln, what's the AV going to do about it when it's reduced to the software equivalent of a UK police officer? Observe and report? Stop or I'll say "stop" again?
> > 
> > AV requires great power, which requires great responsibility. The second part is what often eludes AV developers.

> > > **EvanAnderson**: The OS should do the SYSTEM-level lifting and scanning processes and behavior analysis should run sandboxed as low priv processes. It would require a clearly defined API and I feel like MSFT was always reticent to commit, leaving AV manufacturers to create hacky nightmares.

> > > **bux93**: Windows has separate SeBackupPrivilege for backup software, so why not for AV?

> > > **formerly_proven**: “Because the remediation component requires SYSTEM, the entire AV needs to run as SYSTEM and we have to unpack malware in the kernel”

> > **Fokamul**: Because to get Ring0, you just need signed vulnerable driver.
> > 
> > There are tons of signed drivers to explore ;-)

> **labelbabyjunior**: Some files under Windows are protected as the TrustedInstaller user, which is a more restrictive level of permissions than SYSTEM.

---

### lexicality

helpfully the user provides a second tool which automatically turns off Windows Defender so you can't be affected by this: [https://github.com/Nightmare-Eclipse/UnDefend](https://github.com/Nightmare-Eclipse/UnDefend)

---

### IFC_LLC

I remember the times when Microsoft had a lot of problems 20 years ago because of Sasser and other viruses that were taking over Windows. They did not have any contenders. Yet they have stopped any software development for 9 months just to re-work their entire codebase to prevent things like direct memory execution and stuff like that. The result of that was Windows XP Service Pack 2. After that thing windows XP became a legend.

Now, when Linux is slowly creeping on one side, and Mac NEO on another they keep releasing this AI-slop.

By the looks of it they make most of their money from the cloud and other software things nowadays. And Windows has become a sidekick in their processes.

> **toyg**: I don't think SP2 made much of a difference in the popularity of XP. It was already dominant, and it's mostly remembered as "legendary" because it had become the target platform for every hardware and software vendor on the planet. Windows 98 was too flaky to engender any serious friction to upgrades, and Windows 2000 was not consumer-friendly enough; XP effectively unified the consumer and professional desktop markets, and became the gold standard.
> 
> SP2, if anything, *slowed down* adoption, since it threw a bunch of spanners in the way of third-party code. It was probably necessary, just to stem the flow of bad press, but no mean a key in XP's overall success.

> > **IFC_LLC**: It was not that bad. I remember when SP fixed a bunch of issues with bluetooth, and windows CD burning program was better than any of the Nero Burning ROMs, cause those became unusable overbloated.

> **nailer**: > Windows XP Service Pack 2. After that thing windows XP became a legend.
> 
> God that was an era. XP SP2 was a great OS, IE was the best browser, MSN was the most popular messenger, Skype was acquired, HTC's Windows CE devices were shipping real web browsers that worked over 3G.
> 
> By the end of the Ballmer era, Microsoft has lost the OS, the browser, the messenger, the meeting service and mobile.

> > **uep**: I agree with you on everything except the browser. I'm pretty sure I was using Firefox (or maybe Opera?) on Windows before the release of Vista. I know I was still using IE for some ActiveX web apps for a while. This was the era that I switched over to Linux full-time, but both Windows 2000 and XP were great OSes at this time. Linux was painful to adopt, but I really loved the promise of "full-control" over my computer.
> > 
> > My peeve today is how bad modern chat programs feel compared to the old instant messengers. The modern programs all feel slow and clunky in comparison. I felt that all of the messengers I used (MSN, AIM, ICQ) were more responsive than their modern day equivalents.

> > > **IFC_LLC**: Boy oh boy, have we forgotten the Maxthon? [https://en.wikipedia.org/wiki/Maxthon](https://en.wikipedia.org/wiki/Maxthon)
> > > 
> > > I remember the times when IE passed ACID test? Do we remember the ACID? [http://acid2.acidtests.org/#top](http://acid2.acidtests.org/#top)
> > > 
> > > Ah, what the times were those. Firefox was just gaining traction.
> > > 
> > > And I agree. Slack is sitting there, consuming over gig of memory on my computer, and Miranda NG was able to do the same functionality with cool skins and just 30 megs of ram.
> > > 
> > > Skins... Skins... We've lost even those...

> > > **IFC_LLC**: [https://gs.statcounter.com/browser-market-share#monthly-2009...](https://gs.statcounter.com/browser-market-share#monthly-200901-202603)
> > > 
> > > Yes, I've just checked, even in 2009 you still have IE over 64% of browser usage.

---

### hathym

cl /std:c++17 /EHsc /W4 /O2 /DUNICODE /D_UNICODE /wd4005 /Fe:RedSun.exe RedSun.cpp advapi32.lib ole32.lib user32.lib

---

### luma

Tried to download and Defender blocks it.

> **trollbridge**: That's how the exploit works.

> > **luma**: I can't seem to find any system files replaced, and the .exe was never executed.  I'm running this in a test VM, but from what I can see, Defender signatures have been updated to block this prior to execution.
> > 
> > The exploit, from my reading, needs to be executed in order to do it's thing, but Defender isn't allowing it to be written to the filesystem on download.

---

### ranger_danger

> normally I would just drop the PoC code and let people figure it out

Looks like that's exactly what they did though?

Or maybe they just meant that they don't usually explain how it works?

> **kijin**: Tney gave it a sexy name and set up a website about it (a github repo, at any rate), instead of just talking about it in a mailing list and getting a CVE like a proper bearded security researcher.

> > **tclancy**: It’s getting warm above the equator, they may have shaved for the season.

---

### labelbabyjunior

A local privilege escalation to root via an exploitable service?

Doesn't Linux have one of these CVEs...each week?

> **hnlmorg**: Only if you’re running daemons as root. Which would be an idiotic move to begin with because that’s not how distros package their services. So you’d have to intentionally make this mistake.

> > **GuestFAUniverse**: Intentionally?
> > 
> > Ignorance is bliss!
> > Simply use docker in its (old) default setup, instead of podman, apptainer, docker-rootless ...
> > and that world is yours.
> > 
> > Added bonuses are the incredible stupid integration with ufw on Ubuntu, images with laughable uid mapping, ...
> > 
> > How that shit got traction baffles me.

> **BodyCulture**: No.

> **IshKebab**: Not quite every week, but yeah it has a lot. And if the target uses sudo at all you don't even need an exploit!
> 
> But nobody mentioned Linux. There's no need for whataboutism. They both shouldn't have these vulnerabilities.

> **hsbauauvhabzb**: Probably, but is that service deployed as part of the base operating system or a third party package? Can you remove the service if you deem the crazy service behaviour is unnecessary or too risky for your usecase?

---
