# IPv6 traffic crosses the 50% mark

- **Link**: https://www.google.com/intl/en/ipv6/statistics.html?yzh=28197
- **HN**: https://news.ycombinator.com/item?id=47777894
- **Score**: 511 points
- **By**: Aaronmacaron
- **Date**: 2026-04-15 11:59 UTC
- **Comments**: 328

---

## Comments

### rtdq

And still, in the year of our lord 2026, GitHub does not support IPv6.

[https://github.com/orgs/community/discussions/10539](https://github.com/orgs/community/discussions/10539)

> **growse**: A non-trivial minority of the time, they don't support IPv4 either!

> > **CupricTea**: GitHub is at the point where it immediately rate limits me if I try to look at a project's commit history without being logged in, as in the first time I even open a single URL to the commit history, I get "Too Many Requests" from GitHub thrown at me. I don't know if my work's antivirus stack is causing GitHub to be suspicious of me, but it's definitely egregious.

> > **sidewndr46**: should we try going back to IPX ?

> > > **MisterTea**: IPX/SPX is datagram only. *BUT* it would be an opportunity to build a QUIC-like that runs over it :-)

> > > **MikeNotThePope**: Only if we're bringing back Token Ring, too.

> > **hsbauauvhabzb**: What? One nine isn’t good enough for you?

> > > **lambda**: Excuse me. Zero nines. Or two nines if you relax your definition of where they are in the number. [https://infosec.exchange/@0xabad1dea/116334321751266751](https://infosec.exchange/@0xabad1dea/116334321751266751)

> > > **fogllgldl**: You guys have nines?

> > > **Ekaros**: As long as it is after the decimal separator I can try for that...

> > > **wiredfool**: Personally I’d look for the coveted 5 eights uptime.

> **jermaustin1**: Same with Twilio. We have an internal server that does system alerts. We recently moved it to an IPv6 only host, and a few weeks went by and noticed there were no longer receiving alerts.
> 
> Turns out we could not connect to Twilio's API which is IPv4 only.

> **throw0101a**: > *And still, in the year of our lord 2026, GitHub does not support IPv6.*
> 
> Especially given that it is now owned by Microsoft, which has been working on IPv6-only (at least on their corporate network) for almost a decade:
> 
> * [https://blog.apnic.net/2017/01/19/ipv6-only-at-microsoft/](https://blog.apnic.net/2017/01/19/ipv6-only-at-microsoft/)
> 
> * [https://www.arin.net/blog/2019/04/03/microsoft-works-toward-...](https://www.arin.net/blog/2019/04/03/microsoft-works-toward-ipv6-only-single-stack-network/)

> > **rekoil**: I mean Azure doesn't really support IPv6 well either for a lot of the big-ticket services.

> > > **fogllgldl**: More importantly, it doesn’t support uptime well.

> **Landing7610**: Our university has bad problems with ipv4. Every few days you'll notice some websites being unreachable, including github. Although with their uptime recently, you never know who's to blame...

> **jeroenhd**: They supported IPv6 for a short time, but then stopped their experiment.
> 
> An excellent reason to move away from Github, I find.

> > **literalAardvark**: I've been there. Management was fine with the testing but it added too much overhead for nearly no benefit to us.
> > 
> > One more thing to troubleshoot at 3 am, one more thing to teach to a disinterested tier 1 support team, one more thing for Chrome to be weird about, hundreds more rules to manage in a hostile load balancer, logging tools that don't understand ipv6.
> > 
> > Turned it off. End customer asked why the site got a little slower (CGN) and when we can turn ipv6 back on. As far as I know it's still on the backlog.

> > > **jeroenhd**: One of the big challenges with IPv6 remains that many of the knows-just-enough-about-networking people, like support staff, often never received any IPv6 training (or, for that matter, even enough IPv4 training that they don't need to Google things that come up in real life). Another is that the weird, awful, everyone-hostile corporate "solutions" often break IPv6 in stupid ways (like load balancers and logging tools being unable to cope with minor changes and requiring a full configuration rework).
> > > 
> > > Things have definitely gotten better over time, though. The massive 90s style corporate networks will probably never transition, but smaller and more modern companies don't have that issue.
> > > 
> > > Apple mandating that apps are IPv6 compatible and various government legislation forcing companies to make their shitty middleware IPv6-compatible has improved things quite a bit so far. As uptake keeps rising, the need for technologies like STUN and TURN will slowly start decreasing, and as a result more and more people will end up in "untested" situations where not having IPv6 and falling back to legacy paths starts becoming a problem.

> > > **throw0101a**: Facebook is (AIUI) 100% IPv6-only on their internal network, and has been for many years:
> > > 
> > > * [https://engineering.fb.com/2017/01/17/production-engineering...](https://engineering.fb.com/2017/01/17/production-engineering/legacy-support-on-ipv6-only-infra/)
> > > 
> > > * [https://www.internetsociety.org/blog/2014/09/facebook-launch...](https://www.internetsociety.org/blog/2014/09/facebook-launches-ipv6-only-data-cluster/)
> > > 
> > > IPv4 is actually the "leftover" stuff they have to deal with at the front end.
> > > 
> > > But they are an eye-balls heavy service, with a lot of mobile devices, which also tend to be IPv6-native.

> **sschueller**: Just found this little site. [https://isgithubipv6.web.app/](https://isgithubipv6.web.app/)
> 
> Maybe we shouldn't even measure percentage adoption and instead just if github has finally adopted..

> **farfatched**: GitHub should absolutely support IPv6, but until then... transip.eu provide IPv6 addresses which transparently proxy to github.com: 
> [https://www.transip.eu/knowledgebase/5277-using-transip-gith...](https://www.transip.eu/knowledgebase/5277-using-transip-github-ipv6-proxy)
> 
> You'll need to update your DNS server to include those as AAAA records.
> 
> Do providers like NextDNS or RethinkDNS allow these sorts of overrides?

> > **voltagex_**: >The Github IPv6 Proxy can only be used for traffic to Github using a VPS from TransIP which uses IPv6.

> **globular-toast**: Do we know any technical reason for this? Or are we left to think this is somehow a political thing?

> > **michh**: Perhaps a little tin foil hatty and definitely not the only reason but Microsoft owns Github and also makes a boatload of money off of Azure. Incumbent cloud providers like Azure have a major advantage in terms of having plenty of IPv4 addressing available whereas a new entrant to that market would have to buy or lease that space at a premium. Thus, these companies have an incentive to keep IPv4 a necessity.

> > > **IshKebab**: IPv4 is going to be a necessity for many many decades no matter what Microsoft do. Even when IPv6 is at 99%, people aren't going to want 1 in every 100 people to not be able to access their site at all. It'll need to be like 99.9% before we start seeing serious IPv6-only services.

> > **alex_duf**: It's a possibly a managerial thing, which KPI are you improving when spending engineering time on adding IPv6 support?
> > 
> > That said, for their HTTP stack they use fastly (as far as I understand), which should make the shift moderately easier.

> > **denkmoon**: Outdated beliefs probably. When I talk about v6 support in our b2b saas, PM laughs and says nobody uses that shit. Big tech are massive laggards on this funnily enough.

> > > **throw0101d**: > *Outdated beliefs probably. When I talk about v6 support in our b2b saas, PM laughs and says nobody uses that shit.*
> > > 
> > > Nobody except the 140M subscribers on T-Mobile US's network:
> > > 
> > > * [https://www.youtube.com/watch?v=d6oBCYHzrTA](https://www.youtube.com/watch?v=d6oBCYHzrTA)
> > > 
> > > But sure, be IPv4-only and add latency by forcing traffic through an extra translation box.

> > > **ViscountPenguin**: It's because big tech is USA based mostly, where there's still a glut of ipv4 available.

> > > **paulddraper**: Well it’s over 50%…

> > > **10000truths**: Definitely not for the biggest ones. Google and Meta have so many machines in their data centers that IPv6 addressing becomes a technical necessity due to the risk of exhausting the RFC 1918 address space. Naturally, they were early adopters of IPv6.

> > **mmbleh**: IPv6 is very difficult to implement and enforce reliable rate limits on anonymous traffic. This is something we've struggled a lot with - there is no consistent implementation or standard when it comes to assigning of IPv6 addresses. sometimes a machine gets a full /64, other times a whole data center uses a full /64. So then we need to try and build knowledge of what level to block based on which IP range and for some it's just not worth the hassle.

> > > **RiverCrochet**: Well, even if there was a standard, that's still not a guarantee that the other side of the /64 would be following it. It's correct for you to rate-limit the whole /64.

> > > **Tuna-Fish**: ... But that's no different from IPv4. Sometimes you have one per user, sometimes there are ~1000 users per IP.
> > > 
> > > Most of the ipv4 world is now behind CGNAT, one user per ip is simply a wrong assumption.

> > **skywhopper**: IPv6 rollout is a lot of operational work that ends with next to no immediate quantifiable benefit. So I’ll never be prioritized in a cost-cutting environment.

> > **direwolf20**: It could be that they don't want to implement IP bans in IPv6.

> > > **merpkz**: How does IP bans work in IPv6 case? One just blocks whole /64 or /56 address range?

> > > **c0balt**: Or the most likely more expensive rate limiting (computational wise)

> > **AtNightWeCode**: You probably need a hefty security reimplementation if you want to add IPv6 to Github.

> **jiggawatts**: The irony of this is that pretty much all they'd have to do to enable IPv6 support is to use Azure Front Door as their CDN. Or... use any other CDN, they pretty much all default to providing IPv6!

> **sandeepkd**: Came here to exactly check on this to see if there are any changes on Github side too

> **missingdays**: Most websites still don't

---

### keybits

Tailscale have a great FAQ about IPv4 vs IPv6: [https://tailscale.com/docs/reference/faq/ipv6](https://tailscale.com/docs/reference/faq/ipv6)

If you're not an expert in this area it's worth a read - I certainly learned a few things!

> **rmunn**: That was excellent, thanks for recommending it. I particularly liked how it's a pretty factual FAQ, not particularly cheerleading for IPv6 nor saying "IPv6 is a failure, give up on it".

> **menotyou**: "IPv6 is the next generation of the Internet Protocol (IP), the successor to IPv4."
> 
> This is a misconception. It is not the successor to IPv4, it is an alternative. Maybe the alternative is so good it will eventually make the older extinct, but it does not look like that

> > **Galanwe**: I agree with you. While I can see some benefits to v6 on the internet, I find v4 to be miles easier and cleaner to work with in a LAN setup. Unfortunately though v6 oversteps on LAN features and makes bridging v4 and v6 way uglier than it should.

---

### usui

It has barely hit 50% and it's already plateauing. This adoption rate is ridiculous despite basically all network interfaces supporting it. I thought I would see IPv6 take over in my lifetime as the default for platforms to build on but I can see I was wrong. Enterprise and commercial companies are literally going to hold back internet progress around 60 to 75 years because it's in their best interest to ensure users can't host services without them. Maybe even 75 years might be too optimistic? They are literally going to do everything in their power to avoid the transition, either being dragged out kicking and screaming or throwing their hands up and saying they can't support IPv6 because it costs too much.

Try going IPv6-only by disabling IPv4 on your computer as a test and notice that almost nothing works except Google. End users shouldn't need to set up NAT64/6to4 tunneling. It should be ISPs doing that to prepare for the transition.

Also, notice how Android and iOS don't support turning off IPv4.

> **RiverCrochet**: > It has barely hit 50% and it's already plateauing. This adoption rate is ridiculous despite basically all network interfaces supporting it
> 
> It's fine. IPv4 and IPv6 can be used at the same time. There's no hurry. Network interfaces support anything as long as both sides agree (nothing stopping you from building your own IPX network over MPLS).
> 
> People can move to IPv6 when the IPv4-as-real-estate speculators get out of control, and if IPv6 prevents IPv4 rental prices from going haywire, then it's served a useful purpose.
> 
> I saw a news article that said something about India considering moving to IPv6-only? That's going to be interesting if the rest of the world moves to IPv6 and the U.S. doesn't.
> 
> > End users shouldn't need to set up NAT64/6to4 tunneling. It should be ISPs doing that to prepare for the transition.
> 
> 100%

> **keeperofdakeys**: Nearly all ISPs these days are deploying IPv6 for their mobile networks and core service networks, especially in less developed markets^1. The reason is simple, a cost justification. What doesn't exist is a cost justification for Enterprises to deploy IPv6, and for ISPs to deploy Residential / Corporate Internet IPv6.
> 
> IMO with the right market conditions, IPv6 could spread really fast within 6-24 months. For example, most cloud providers are now charging for IPv4 addresses when IPv6 is free. Small changes like that push in the right direction.
> 
> ^1 [https://www.theregister.com/2025/08/04/asia_in_brief/](https://www.theregister.com/2025/08/04/asia_in_brief/)

> > **reddalo**: Hetzner makes you pay 1 € per IPv4, while IPv6 is free. I'd gladly get rid of all IPv4's given that I have many servers.

> **dtech**: Apple/iOS is probably one of the biggest individual drivers of IPv6 adoption. They've been requiring that iOS apps work on IPv6-only networks for close to 10 years now

> > **throw0101d**: > *They've been requiring that iOS apps work on IPv6-only networks for close to 10 years now*
> > 
> > This was at the behest of mobile network. E.g., T-Mobile US has 140M subscribers, and moved to IPv6-only many years ago:
> > 
> > * [https://www.youtube.com/watch?v=d6oBCYHzrTA](https://www.youtube.com/watch?v=d6oBCYHzrTA)

> > **lxgr**: The requirement is to support IPv6 only networks with IPv4 transition mechanisms. It does not preclude contacting v4-only servers.

> > > **moduspol**: And the higher level libraries mostly do it for you, too, even if you directly specify IPv4 addresses in your code (due to NAT64 [1]). I think it only even requires special work from you as a developer if you're using low-level or non-standard libraries.
> > > 
> > > [1] [https://en.wikipedia.org/wiki/NAT64](https://en.wikipedia.org/wiki/NAT64)

> > **aniviacat**: If that's the case, how does the Github app work on iOS?

> > > **dtech**: Nat64: [https://developer.apple.com/support/ipv6/](https://developer.apple.com/support/ipv6/)

> > > **eptcyka**: Differential enforcement.

> > > **nothrabannosir**: I’m guessing the app works but their prod servers don’t? If they can point the app during review at a “self hosted” GitHub Enterprise server on a test domain with AAAA that would pass the requirement as stated by gp , without requiring GitHub.com actually support ipv6.

> **imoverclocked**: ISPs often fail to do this because there is always someone in the hierarchy who says, "nobody is demanding it."

> > **betaby**: Nobody is demanding IPv4 either. Or Ethernet.
> > People buy "Wi-Fi", literally "Wi-Fi", not Internet access.

> > **bluGill**: I with I knew how to get through that I want it. I'm supposed to be a tech guy - that means I need experience with the latest tech in my house

> > > **moduspol**: I switched my home ISP from cable (which supported IPv6) to fiber (which doesn't) and I've had a nagging disappointment ever since. But I guess consumers aren't really demanding it enough.

> > **FridgeSeal**: I worked at a place where they refused to run it _anywhere_ because a couple of people were insistent that it was “insecure”.

> > > **Galanwe**: ... and they were right.
> > > 
> > > v6 adoption is often an all or nothing, because if you run both stacks, you have to ensure they are consistent. While you can reasonably do it on your home LAN, doing it across an entire infrastructure is the worst.
> > > 
> > > Now you have to make sure all your subnets, routing, VLANs, firewall rules, etc work exactly the same in two protocols that have very little in common.
> > > 
> > > It is the equivalent of shipping two programs in different languages and maintaining exact feature parity between both at all times.

> **lmm**: I think we'll hit a tipping point soon, just like with Python3 - for years and years it seemed almost stalled, then it became easier to start with python3 than python2 and suddenly everyone migrated.

> > **usui**: This seems like wishful thinking. Python3 vs. Python2 seems different than IPv6 vs. IPv4.

> > > **tucnak**: "seems" is doing a lot of heavy-lifting in your message

> > **yangm97**: “Gradually, then suddenly.”

> **MiscIdeaMaker99**: Since when was there ever a plan to disable IPv4 on the Internet? Just because IPv6 is around doesn't mean that IPv4 is going to go away.

> > **bluGill**: That was always the plan for "the future".  That is get everyone to IPv6 and then get rid of IPv4.  IPv4's days are numbered - but the number looks really big.

> **ectospheno**: > Also, notice how Android and iOS don't support turning off IPv4.
> 
> You can trivially connect an iOS device via IPv6 only.

> **zokier**: > End users shouldn't need to set up 6to4 tunneling. It should be ISPs doing that to prepare for the transition.
> 
> Which is what ISP are doing with 464XLAT deployments. IPv6-mostly networking and IPv4-as-a-service are things that are happening in real world right now.

> > **kalleboo**: Yeah in Japan my ISP even lets me choose which IPv4 provider I want to use, as the fiber network is IPv6-native and IPv4 is "just another service" like IPTV.

> **drpixie**: >> It has barely hit 50% and it's already plateauing.
> 
> Well, the curve has got to level-out at 100%.

> > **cowsandmilk**: No, it can level out below that and is (as the parent was saying).

> > > **bluGill**: How far below is the question.  It could level out at 60% - that is believable.  However it can't level out at 99% - Somewhere around 95% major sites will decide IPv4 isn't worth supporting and they will just ignore that final 5% of customers, which will force them to upgrade - which in turn will give others confidence to remove their final 4% of customers - until IPv4 dies.

> **vr46**: My German ISP supports it now, which was the limiting factor for me, and a new VPS I just bought also does, so finally I was able to create my first personal AAAA record. I am hoping that we're seeing a tipping point. Again.

> **waynesonfire**: > It has barely hit 50% and it's already plateauing.
> 
> That makes sense. The majority of IPv6 deployment is mobile.
> 
> The next wave of adoption requires ISPs start offering residential IPv6. Once this happens, router manufacturers will innovate around the IPv6 offering as a differentiator, making it easy to deploy by end-users. IPv6 wifi APs will then become ubiqutious and so forth across other services. Has to start with ISPs.

> > **dtech**: ISPs in the US and Europe mostly have been offering IPv6 for a while now

> > > **jabl**: Unfortunately my ISP here in Europe is not one of those offering IPv6.

> > > **Hikikomori**: Other than France or Germany its far from mostly.

> **fogllgldl**: Worst migration plan ever.

> **preisschild**: > It should be ISPs doing that to prepare for the transition.
> 
> Yeah, I dont get why more ISPs don't offer carrier-grade NAT64 instead of the typical CGNAT

> > **lmm**: In parts of the world with fewer IP addresses they already are. My ISP _only_ offers MAP-E access to the IPv4 internet for anyone not grandfathered into an older plan.

> **stackghost**: Is there a reason why adoption has been so abysmally slow?  Like surely all the big players have updated their networking equipment by now, and surely every piece of enterprise-grade kit sold in the last 20 years has supported v6.
> 
> The only arguments I've ever heard against ipv6 that made any sense are that:
> 
> 1:  it's hard to remember addresses, which is mayyyyybe valid for homelab enthusiast types, but for medium scale and up you ought to have a service that hands out per-machine hostnames, so the v6 address becomes merely an implementation detail that you can more or less ignore unless you're grepping logs.  I have this on my home network with a whopping 15 devices, and it's easy.
> 
> and 2:  with v6 you can't rely on NAT as an ersatz firewall because suddenly your printer that used to be fat dumb and happy listening on 192.168.1.42 is now accidentally globally-routable and North Korean haxors are printing black and white Kim Il Sung propaganda in your home office and using up all your toner.  And while this example was clearly in jest there's a nugget of truth that if your IOT devices don't have globally-routable addresses they're a bit harder to attack, even though NAT isn't a substitute for a proper firewall.
> 
> But both of these are really only valid for DIY homelab enthusiast types.  I honestly have no idea why other people resist ipv6.

> > **nottorp**: > But both of these are really only valid for DIY homelab enthusiast types. I honestly have no idea why other people resist ipv6.
> > 
> > Simple. The "homelab enthusiast types" are those that usually push new technologies.
> > 
> > This is one they don't care about, so they don't push it. Other people don't care about any technology if it's not pushed on them.

> > **noirscape**: The big reason is that domestic ISPs don't want to switch (not just in the US, but everywhere really.)
> > 
> > Data centers and most physical devices made the jump pretty early (I don't recall a time where the VPS providers I used didn't allow for IPv6 and every device I've used has allowed IPv6 in the last 2 decades besides some retro handhelds), but domestic ISPs have been lagging behind. Mobile networks are switching en masse because of them just running into internal limits of IPv4.
> > 
> > Domestic ISPs don't have that pressure; unlike mobile networks (where 1 connection needing an IP = 1 device), they have an extra layer in place (1 connection needing an IP = 1 router and intranet), which significantly reduces that pressure.
> > 
> > The lifespan of domestic ISP provided hardware is also completely unbound by anything resembling a security patch cycle, cost amortization or value depreciation. If an ISP supplies a device, unless it fundamentally breaks to a point where it quite literally *doesn't work anymore* (basically hardware failure), it's going to be in place forever. It took *over 10 years* to kill WEP in favor of WPA on consumer grade hardware. To support IPv6, domestic ISP providers need to do a mass product recall for all their ancient tech and they don't want to do that, because there's no real pressure to do it.
> > 
> > IPv6 exists concurrently with IPv4, so it's easier for ISPs to make anyone wanting to host things pay extra for an IPv4 address (externalizing an ever increasing cost on sysadmins as the IP space runs out of addresses) rather than upgrade the underlying tech. The internet default for user facing stuff is still IPv4, not IPv6.
> > 
> > If you want to force IPv6 adoption, major sites basically need to stop routing over IPv4. Let's say Google becomes inaccessible over IPv4 - I guarantee you that within a year, ISPs will suddenly see a much greater shift towards IPv6.

> > > **zokier**: Except that is completely wrong. Consumer/residential networks have significantly higher ipv6 adoption rates that corporate/enterprise networks. That is why you see such clear patterns (weekend vs weekday) in the adoption graphs.

> > > **ENGNR**: It's frustrating that even brand new Unifi devices that claim to support IPv6 are actually pretty broken when you try to use it. So 10 years from right now even, unless they can software patch it upwards.

> > **Dagger2**: *Has* it been abysmally slow? What's the par time for migrating millions of independent networks, managed by as many independent uncoordinated administrators, to a new layer 3 protocol?
> > 
> > We've never done this before at this scale. Maybe this is just how long it takes?

> > **crote**: Sure, the *data plane* supports it - but what about the management plane?
> > 
> > I wouldn't be surprised if ISPs did all the management tasks through a 30-year-old homebrew pile of technical debt, with lots of things relying on basic assumptions like "every connection has exactly one ip address, which is 32 bits long".
> > 
> > Porting all of that to support ipv6 can easily be a multi-year project.

> > > **Sesse__**: > Porting all of that to support ipv6 can easily be a multi-year project.
> > > 
> > > FWIW, as someone who has done exactly this in a megacorp (sloshing through homebrew technical debt with 32-bit assumptions baked in), the initial wave to get the most important systems working was measured in person-months. The long tail was a slog, of course, but it's not an all-or-nothing proposition.

> > > **Hikikomori**: This is true, I worked for an old ISP/mobile carrier that started in the 80s about 10-15 years ago. They had basically any system you could think of still running, from decently modern vmware with windows and linux to hp-ux, openvms, sunos, AIX, etc. Could walk around and see hardware 30 years old still going, I think one console router had an uptime of 14 years or so. One time I opened a cabinet and found a pentium 1 desktop pc on the floor still running and connected, served some webpage. The old SMSC from the 80s on DEC hardware was still in its racks though not operational, they didn't need the space as the room couldn't provide enough power or cooling for more than a few modern racks. The planning program for fiber, transmission, racks, etc, required such an old java that new security bugs didn't apply to it, and looked and worked like an old mainframe program.
> > > 
> > > The core team supported ipv6 for a long time, but its rather easy to do that part. The hard part is the customer edge and CPE and the stack to manage it, it may have a lifetime of 2 decades.

> > **alibarber**: > 1: it's hard to remember addresses
> > 
> > fd::1 is perfectly valid internal IPv6 address (along with fd::2 ... fd::n)

> > > **holowoodman**: fd::1 is somewhere in the reserved ::/8 space where various stuff like old ipv4 mapped addresses and localhost reside. What you probably mean is something like fd00::1, but that is something you shouldn't use, because 'fd00::/8' is a probabilistically unique local address (ULA) block. You are supposed to create a /48 net by appending 40 random bits to fd00::/8. Of course, if your fair dice roll lands on all zeroes, and you are ok with probable collisions in case of a network merge, you are fine ;)

> > **nubinetwork**: > Like surely all the big players have updated their networking equipment by now
> > 
> > My home isp can't even do symmetrical gigabit, let alone ipv6...

> > > **esseph**: That's extremely common unless on "active" fiber (vs GPON, DOCSIS3, DSL, most fixed wireless, satellite, mobile, etc.)
> > > 
> > > Your wifi isn't symmetrical either.

> > **direwolf20**: Ignore all the excuses like longer addresses and incompatible hardware. The *actual* reason is that everyone hates change.

> > **cyberax**: IPv6 is a recursive WTF. It might _look_ like a conservative expansion of IPv4, but it's really not. A lot of operational experience and practices from IPv4 don't apply to IPv6.
> > 
> > For example, in IPv4 each host has one local net address, and the gateway uses NAT to let it speak with the Internet. Simple and clean.
> > 
> > In IPv6 each host has multiple global addresses. But if your global connection goes down, these addresses are supposed to be withdrawn. So your hosts can end up with _no_ addresses. ULA was invented to solve this, but the source selection rules are STILL being debated: [https://www.ietf.org/archive/id/draft-ietf-6man-rfc6724-upda...](https://www.ietf.org/archive/id/draft-ietf-6man-rfc6724-update-23.html)
> > 
> > Then there's DHCP. With IPv4 the almost-universal DHCP serves as an easy way to do network inspection. With IPv6 there's literally _nothing_ similar. Stateful DHCPv6 is not supported on Android (because its engineers are hell-bent on preventing IPv6). And even when it's supported, the protocol doesn't require clients to identify themselves with a human-readable hostname.
> > 
> > Then there's IP fragmentation and PMTU that are a burning trash fire. Or the IPv6 extension headers. Or....
> > 
> > In short, there are VERY good reasons why IPv6 has been floundering.

> > > **teddyh**: > *For example, in IPv4 each host has one local net address, and the gateway uses NAT to let it speak with the Internet. Simple and clean.*
> > > 
> > > No, that’s not the IPv4 design.  That’s an *incredibly ugly hack* to cope with IPv4 address shortage.  It was never meant to work this way.  IPv6 *fixes* this to again work like the original, *simpler* design, without ”local” addresses or NAT.
> > > 
> > > > *In IPv6 each host has multiple global addresses.*
> > > 
> > > Not necessarily.  You can quite easily give each host one, and only one, static IPv6 address, just like with old-style IPv4.

> > > **toast0**: > Then there's IP fragmentation and PMTU that are a burning trash fire.
> > > 
> > > It's not significantly worse on v6 compared to v4. Yes, in theory, you can send v4 packets without DF and helpful routers will fragment for you. In practice, nobody wants that: end points don't like reassembling and may drop fragments; routers have limited cpu budget off the fast path and segment too big is off the fast path, so too big may be dropped rather than be fragmented and with DF, an ICMP may not always be sent, and some routers are configured in ways where they can't ever send an ICMP.
> > > 
> > > PMTUd blackholes suck just as much on v4 and v6. 6rd tunnels maybe make it a bit easier to hit if you advertise mtu 1500 and are really mtu 1480 because of a tunnel, but there's plenty of derpy networks out there for v4 as well.

> > > **dwattttt**: > For example, in IPv4 each host has one local net address, and the gateway uses NAT to let it speak with the Internet. Simple and clean.
> > > 
> > > I assume you mean "interface", not "host". Because it's absolutely not true that a host can only have one "local net address".
> > > 
> > > EDIT: a brief Google also confirms that a single interface isn't restricted to one address either: sudo ip address add <ip-address>/<prefix-length> dev <interface>

> > > **philipallstar**: How do the working IPv6 deployments cope with these issues?

> > > **yangm97**: The reason: Skill issue.

> > > **holowoodman**: > For example, in IPv4 each host has one local net address, and the gateway uses NAT to let it speak with the Internet. Simple and clean.
> > > 
> > > That's only true for smalltime home networks. Try to merge 2 company IPv4 networks with overlapping RFC1918 ranges like 10.0.0.0/8. We'll talk again in 10 years when you are done sorting out that mess ;)
> > > 
> > > > In IPv6 each host has multiple global addresses. But if your global connection goes down, these addresses are supposed to be withdrawn. So your hosts can end up with _no_ addresses.
> > > 
> > > Only a problem for home users with frequently changing dialup networks from a stupid ISP. And even then: Your host can still have ULA and link-local addresses (fe80::<mangled-mac-address>).
> > > 
> > > > ULA was invented to solve this, but the source selection rules are STILL being debated: [https://www.ietf.org/archive/id/draft-ietf-6man-rfc6724-upda](https://www.ietf.org/archive/id/draft-ietf-6man-rfc6724-upda)...
> > > 
> > > RFC6724 is still valid, they are only debating a slight update that doesn't affect a lot.
> > > 
> > > > Then there's DHCP.
> > > 
> > > DHCPv6 is an abomination. But not for the reasons you are enumerating.
> > > 
> > > > With IPv4 the almost-universal DHCP serves as an easy way to do network inspection.
> > > 
> > > IPv4 DHCP isn't a sensible means to do network inspection. Any rougue client can steal any IP and MAC address combination by sniffing a little ARP broadcast traffic. Any rogue client can issue themselves any IPv4 address, and even well-behaved clients will sometimes use 169.254.0.0/16 (APIPA) if they somehow didn't see a DHCP answer. If you want something sensible, you need 802.1x with some strong cryptographic identity for host authentication.
> > > 
> > > > Stateful DHCPv6 is not supported on Android (because its engineers are hell-bent on preventing IPv6).
> > > 
> > > Yes, that is grade-A-stupid stubborness. On the other hand, see below for the privacy hostname thingy in IPv4 and the randomized privacy mac addresses that mobile devices use nowadays. So even if Android implemented stateful IPv6, you will never be reliably able to track mobile devices on your network. Because all those identifiers in there will be randomized, and any "state" will only last for a short time. If you want reliable state, you need secure authentication like 802.1x on Ethernet or WPA-Enterprise on Wifi, and then bind that identity to the addresses assigned/observed on that port.
> > > 
> > > > With IPv6 there's literally _nothing_ similar.
> > > 
> > > Of course there is. DHCPv6 can do everything that IPv4 DHCP can do (by now, took some time until they e.g. included MAC addresses as an option field). But in case of clients like Android that don't do DHCPv6 properly, you still have better odds in IPv6: IPv6 nodes are required to implement multicast (unlike in IPv4 where multicast was optional). So you can just find all your nodes in some network scope by just issuing an all-nodes link-local multicast ping on an interface, like:
> > > 
> > > > ping6 ff02::1%eth0
> > > 
> > > There are also other scopes like site-local:
> > > > ping6 ff05::1%eth0
> > > [https://www.iana.org/assignments/ipv6-multicast-addresses/ip...](https://www.iana.org/assignments/ipv6-multicast-addresses/ipv6-multicast-addresses.xhtml)
> > > 
> > > (The interface ID (like eth0, eno1, "Wired Network", ...) is necessary here because your machine usually has multiple interfaces and all of those will support those multicast ranges, so the kernel cannot automatically choose for you.)
> > > 
> > > > And even when it's supported, the protocol doesn't require clients to identify themselves with a human-readable hostname.
> > > 
> > > DHCP option 12 ("hostname") is an option in IPv4. Clients can leave it out if they like. There is also such a thing as "privacy hostname" which is a thing mobile devices do to get around networks that really want option 12 to be set, but don't want to be trackable. So the hostname field will be something like "mobile-<daily_random>".
> > > 
> > > What you skipped are the really stupid problems with DHCPv6 which make it practically useless in many situations: DHCPv6 by default doesn't include the MAC address in requests. DHCPv6 forwarders may add that option, but in lots of equipment this is a very recent addition still (though the RFC is 10 years old by now). So if you unbox some new hardware, it will identify by some nonsensical hostname (useless), an interface identifier (IAID, useless, because it may be derived from the MAC address, but it may also be totally random for each request) and a host identifier (DUID, useless, because it may be derived from the mac address, but it may also be totally random for each request). Whats even more stupid, the interface identifier (IAID) can be derived from a MAC address that belongs to another interface than the one that the request is issued on. So in the big-company usecase of unboxing 282938 new laptops with a MAC address sticker, you've got no chance whatsoever to find out which is which, because neither IAID nor DUID are in any way predictable. You'll have to boot the installer, grab the laptop's serial number somewhere in DMI and correlate with that sticker, so tons of extra hassle and fragility because the DHCPv6 people thought that nobody should use MAC addresses anymore...

> **themafia**: Comcast,  one of the largest residential ISPs in the USA,  has almost full IPv6 deployment by default.  The majority Verizon Wireless is IPv6 by default.  Residential customers in the USA have great access if they just enable the stack.
> 
> There is nothing about IPv6 that prevents ISPs from filtering ports for all customers.  They almost all actively filter at least port 25, 139 and 445 regardless of the actual transport.  So I'm not sure "blocking service hosting" is the actual goal here.
> 
> The problem seems to be that all of the large and wealthy nations of the world have made the necessary huge investments into IPv6 while many of their smaller neighbors and outlying countries and islands have struggled to get any appreciable deployment.
> 
> It should be a UN and IMF priority to get IPv6 networks deployed in the rest of the world so we can finally start thinking about a global cutover.

> > **dtech**: In many developing countries IPv6 adoption is far and sometimes networks are IPv6-only, because IPv4 is expensive and they have relatively little addresses compared to users...
> > 
> > You can see southeast Asia is pretty green on the map of the post.

> > **kortilla**: A UN priority!? They have real issues they should be dealing with like the life and death of millions of people

> **panny**: I don't want IPv6. Why would I? It's like a permanent global cookie. You're uniquely tagged and identifiable on every website you visit.
> 
> >it's in their best interest to ensure users can't host services without them.
> 
> They'll just keep blocking port 25. IPv6 won't change anything with regards to self hosting.

> > **kstrauser**: > You're uniquely tagged and identifiable on every website you visit.
> > 
> > Almost every modern OS enables IPv6 privacy extensions, ie address randomization, by default.

> > **farfatched**: My OS gives me IPv6 privacy addresses out-the-box which rotate every few hours.

---

### colmmacc

If GitHub flipped a switch and enabled IPv6 it would instantly break many of their customers who have configured IP based access controls [1]. If the customer's network supports IPv6, the traffic would switch, and if they haven't added their IPv6 addresses to the policy ... boom everything breaks.

This is a tricky problem; providers don't have an easy way to correlate addresses or update policies pro-actively. And customers hate it when things suddenly break no matter how well you go about it.

[1] [https://docs.github.com/en/enterprise-cloud@latest/organizat...](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization)

> **alibarber**: Having been messing around personally with getting my own blocks of IP addresses and routing[1] - I've become terrified at the idea of implementing access control based on IP address.
> 
> Unless your own organisation in the RR has the IP addresses assigned to you as Provider Independent resources, there just seems to be so many places where 'your' IP address could, albeit most likely accidentally, become not yours any more. And even then, just like domain names, stop renewing the registration and someone else will get them - I was that someone else recently...
> 
> [1] AS202858

> > **yosamino**: Oh, cool!  that's on my bucket list as well. I am still grappling with some concepts, though.
> > 
> > Do you have a writeup of your setup somewhere or can you recommend some learning materials ?

> > > **alibarber**: It's fun and has now become an addictive rabbit hole - trying to get packets from one location to the other in the fastest, most direct way (and at hobbyist budget level).
> > > 
> > > Initial writeup based on IPv6: [https://abarber.com/Setting-Up-ASN-IPv6-Routing-BIRD-Teltoni...](https://abarber.com/Setting-Up-ASN-IPv6-Routing-BIRD-Teltonika-Router-Wireguard/)
> > > 
> > > Have been having fun recently with an IPv4 block and Asynchronous routing, working on writing that up right now :)

> **progbits**: Anyone who relies on IP filtering for security deserves to have it broken. Change my mind.

> > **omh**: I'll take that bait ;-)
> > 
> > IP filtering is a valuable factor for security. I know which IPs belong to my organisation and these can be a useful factor in allowing access.
> > 
> > I've written rules which say that access should only be allowed when the client has both password *and* MFA *and* comes from a known IP address.
> > Why shouldn't I do that?
> > 
> > And there are systems which only support single-factor (password) authentication so I've configured IP filtering as a second factor. I'd love them to have more options but pragmatically this works.

> > > **friendzis**: Why are you (re-)implementing client security on provider end? If a client requires that only requests from a particular network are permitted... Peer in some way.
> > > 
> > > I do understand the value of blocking unwanted networks/addresses, but that's a bit different problem space.

> > **sebiw**: Defense in depth is a thing but I agree that relying on it is not a good idea.

> > > **tucnak**: Defense in depth is not the point, zero trust networking is.

> > **apexalpha**: IP filtering + proper security is better than just having the security.
> > 
> > There's value in restricting access and reducing ones attack surface, if only to reduce noice in monitoring.

> **bluGill**: If you can't handle sites switching to ipv6 in 2015 (ten years ago) your security plan is garbage.

> **TabTwo**: Thanks to the trend to SASE like Palo Alto GlobalProtect or ZScsler this practice is not a good idea anymore. Speaking of ZScaler, they are still IPv4 only, right?

---

### rmunn

Zoom in on that graph using the controls at the bottom, and you'll see a repeating pattern of crests and troughs, weekly. There's about a 5% difference between the crests and the troughs: the crests are hitting the 50% line or just below it, and the troughs are down around 45%.

The real question is, why are the crests so predictable? They're always on Saturdays; Sunday dips down a little below the crest, then Monday-Friday is down in the 45% range before the next Saturday jumps up to 50% again. (Fridays usually have a small rise, up to the 46-47% area).

My theory: mobile access rises on weekends. People are more often accessing Google services from their work computers Monday-Friday, but on Saturdays and Sundays most (not all) people are away from the office. Many of them will end up using smartphones rather than laptops for Internet access, for various reasons such as being outdoors. And since smartphones are nearly all using IPv6 these days, that means an uptick in IPv6 usage over the weekends.

> **kalleboo**: It's not just mobile networking but residential ISPs in general have better IPv6 support. In the US, Comcast was one of the first big IPv6 deployments, in Europe CGNAT+IPv6 is common in many places.
> 
> Meanwhile corporate IT for business and education networks have less incentive to upgrade and typically lag behind in adoption in general.

> **Xirdus**: Residential vs. business. If the graph was hourly and per country, you'd see the same rise every morning and drop every evening (likely by more than 5pp).

---

### mgulick

I get an IPv6 address from my ISP (a /56 I believe), but I wish there was some good information on how to update my OpenWRT VLAN configuration, routing, and firewall rules to be able to support native IPv6 on my devices.  Would love to be able to have direct IPv6 connections to the internet from my devices, but I want to make sure I can do it safely.

> **nzeid**: This was surprisingly complicated for me on Altice/Optimum, which is why my home didn't have IPv6 for a while even after they started provisioning.
> 
> We actually have a /128 address only, and had to tweak several settings including enabling IPv6 masquerading (NAT).
> 
> I haven't the slightest clue why they didn't give us a block.

> **_bernd**: You only need to set nothing and it should setup ipv6 on all downstream vlan interfaces.
> For static prefix I'd you can set ip6hint per vlan interface.
> For each vlan interface you need a stanza in the DHCP config file.
> And regarding firewall, as with the default lan zone you might need to add new zones with the vlan interfaces and configure forwarding rules. That's it.

---

### loevborg

Sometimes TCP/IP is a leaky abstraction, and recently ipv6 peeked through in two separate instances:

- In a cafe wifi, I had partial connectivity. For some reason my wifi interface had an ipv6 address but no ipv4 address. As a result, some sites worked just fine but github.com (which is, incredibly, ipv4-only) didn't

- I created a ipv6-only hetzner server (because it's 2026) but ended up giving up and bought a ipv6 address because lack of ipv4 access caused too many headaches. Docker didn't work with default settings (I had to switch to host networking) and package managers fail or just hang when there's no route to the host. All of which is hard to debug and gets in your way

> **pastage**: You can solve this issue if you have one server with ipv6/ipv4 you can run NAT with Jool and connect ipv6 only servers to that. Like Android does.
> 
> I wish hosting providers would give you a local routed ipv4 on ipv6 servers with a default NAT server. It is not that expensive I move 10Gbps "easily" and they could charge for that traffic.

> > **zokier**: > I wish hosting providers would give you a local routed ipv4 on ipv6 servers with a default NAT server.
> > 
> > You mean like AWS NatGW [https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gat...](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)

> > > **emj**: 30 USD/month and 0.045 USD/GB for ingress it is ok if you are big. It is a cheap service to build yourself. I do feel the pain of it being hard to get IPv4 minimal connectivity on ipv6 only hosts, i.e. for me a 1 USD/GB would be fine.

> > > **crote**: Those are still per-customer and require you to dedicate an entire IP address to it. That's overkill for a server which mostly talks over ipv6 but needs to connect to an ipv4-only service like Github once in a blue moon.

> > > **loevborg**: Any services like this for Hetzner?

---

### zokier

This google metric measures adoption in access networks, but at this point I feel more interesting metric is adoption in services.

One such stat is here:

> adoption ranging from 71% among the top 100 to 32% in the long tail

[https://commoncrawl.org/blog/ipv6-adoption-across-the-top-10...](https://commoncrawl.org/blog/ipv6-adoption-across-the-top-100k-web-hosts)

Getting full coverage on AWS (/GCP/Azure) and few other key services (GitHub...) would be significant here imho.

---

### Anonyneko

And yet I still haven't ever connected to an internet provider that supports IPv6, across two countries I spend time in...

---

### Leomuck

What I have asked myself the last few months: I've read about IPv4 becoming sparce a few years ago. I haven't read much about it lately. And I've thought maybe the advance of cloud computing and load balancer kind of mitigated the issue of sparce IP4?

---

### neitsab

As a French national, I am surprised to discover we are topping the charts according to this analysis.

Does anybody know why that might be the case? What's the story of IPv6 deployment in France?

> **timpera**: The regulatory body, ARCEP, has been very proactive since 2002 (!) on IPv6. The recent uptick is due to IPv6 obligations bundled in the 5G spectrum licences.
> 
> [https://www.arcep.fr/la-regulation/grands-dossiers-internet-...](https://www.arcep.fr/la-regulation/grands-dossiers-internet-et-numerique/lipv6.html)

> **garganzol**: Maybe my guess only, but France has its bit of a technological centralization. I mean, a lot of people use internet from operators like "Orange" / "Free", and in contrast to other countries, routers provided by the operators in France do not suck. The routers are OEM, but overall quality you get from them is on-par with Ubiquity/Mikrotik.
> 
> This gives operators a benefit of the vertical control for the whole ecosystem - from top to the bottom, including intricate parts of protocols and routing. And France, in contrast to other countries, does not suck here too - operators usually do a good job of meticulously maintaining their assets.
> 
> My personal impression is that this is the result of several cultural factors:
> 
> 1. Ingrained respect of privacy, private property, and a peace of heart as they call it. As a practical result of that, you do not get spammy messages and ads from operators, banks, etc. You may get some, like 3 or 4 discounts/offers in a year. Compare that to other countries where you can easily get 10s/100s messages like that in a single day. In other countries, instead of upgrading the infrastructure, people are busy with spamming each other.
> 
> 2. The harsh oceanic environment with hurricanes and storms fosters an appreciation for reliability and functionality. It also encourages a certain frugality: every cent matters. As a result, people tend to develop a strong sensitivity to situations where form is prioritized over function, and such approaches are quickly dismissed as impractical. This gives a certain internal freedom of being able to see through things to determine what they are in the long run and not what they appear to be on the surface.
> 
> 3. French people don't like to overwork outside of working hours. So choosing something like IPv6 over IPv4 seems like a natural forward-looking investment for the future where you can have less maintenance burden and thus you can devote more time to enjoying other things in life.
> 
> Having all those things combined, it's not hard to see why France chose IPv6. It's a natural choice there and it's imposed by survival.
> 
> P.S. I've spent some time in France, but was born in another country.

> **dwedge**: I worked with the internet society to mobitor ipv6 adoption for the top million sites ipv6matrix.org it's broken down by country so might answer some of your curiosity

> **ankit_mishra**: I'm wondering the same thing for India. Not the top but looks surprisingly surprisingly high. Perhaps I'm reading the data wrong.

> > **lazide**: India has about 1.5 billion people, and has only recently been getting most of them online.  Less IPv4 legacy, and it has always been obvious that IPv4 was never going to be ‘enough’ to actually onboard everyone anyway.
> > 
> > When I lived in India, everything had IPv6 out of the box.

> > **ggm**: Reliance Jio deployed cheap native v6 and tool massive market share. They single-handedly moved the market.
> > 
> > It's been discussed on the apnic blog and at meetings heaps

> > > **toast0**: Adding on. Jio was a late entrant, so they could not get significant ipv4 address space without great expense. They deployed as mostly v6 with a tiny CGNAT. They also had an extensive 'pre-release' offering at zero cost to subscribers which got them a huge number of subscribers and clout to encourage internet services to offer ipv6.

> **DANmode**: Technical literacy, hacker culture, and culture of well-considered infrastructure, have been French characteristics - at least, historically.
> 
> Has something changed for the worse?

---

### p4bl0

It amuses me to see that according to the map, France is best in class or close to be, while just a few weeks ago, my ISP in France stopped providing me IPv6 connectivity…

The story is that at the beginning I had IPv6, and a shared dynamic IPv4 behind a CGNAT, I asked for a rollback to a full duplex static IPv4 and for three years I had both a static personal IPv4 and an IPv6. A few weeks ago my router went down and since it went back up, I no longer have an IPv6 address. I called my ISP and they explained that I could either have IPv6 or a static IPv4, but not both, and that it's abnormal that I had both for so long… welp, it's sad to see IPv6 but getting it back is not worth abandoning my static IPv4 and going back to a dynamic shared IPv4.

> **basilikum**: You might be interested in [https://tunnelbroker.net/](https://tunnelbroker.net/) and [https://route64.org/](https://route64.org/) although the later looks a little shady and I haven't tried them.
> 
> A cheap VPS or one with spare bandwidth with > /64 that is properly routed (some providers do NDP for some reason) and a Wireguard tunnel would also get you a simple DIY solution.

> **harg**: Are you with SFR? I also seem to only have a static IPv4 (I don't pay for it, but it's never changed in the lifetime of the connection). I asked for an IPv6 but they said it was not possible/difficult.

> > **p4bl0**: Yep, with "RED by SFR" specifically.

> > > **fossilwater**: Among all the major French providers, SFR lags far behind its competition unfortunately

---

### pjf

NB: this is not "IPv6 traffic crosses the 50% mark" but "availability of IPv6 connectivity among Google users", which is a very important difference. This means roughly half of Google users have IPv6 *capability*, which does not 1:1 correspond how much *traffic* is actually transferred over IPv6, which is what this submission says in the title.

> **usui**: Yeah and this distinction explains the fact that because China's Great Firewall blocks Google, this website shows 4.66% adoption as a reflection of that. I think China's IPv6 support rate is actually much higher than that, maybe a little over 50% because of its central initiative to increase IPv6 adoption?
> 
> EDIT: Apparently it's 77% [https://pulse.internetsociety.org/en/news/2026/01/china-hits...](https://pulse.internetsociety.org/en/news/2026/01/china-hits-865m-ipv6-users/)

> **kalleboo**: It also means you're excluding China, who has has it as a long-term priority to deploy IPv6 and have made huge strides.

---

### molf

It's only a matter of time before laptops get 5G. Macbooks have been rumoured for a while to get cellular modems. [1]

This will probably help adoption. On the one hand it will generate more IPv6 traffic. On the other hand it will expose more developers to IPv6; which will expose them to any lack of support for IPv6 within their own products.

[1]: [https://9to5mac.com/2025/08/14/apples-first-mac-with-5g-cell...](https://9to5mac.com/2025/08/14/apples-first-mac-with-5g-cellular-might-be-coming-sooner-than-we-thought/)

> **nottorp**: > It's only a matter of time before laptops get 5G.
> 
> So you want laptops to cost <whatever the laptop costs> plus a measly 19.99/month for internet connectivity?
> 
> What's wrong with just tethering to my existing phone?

> **venzaspa**: Dell, HP and Lenovo have had laptops with cellular modems for maybe 15 years at this point.

> > **gempir**: *A few select models got celluar modems.
> > 
> > I have owned several Dell, HP and Lenovo Laptops in the past 15 years and I have never had a cellular modem.
> > 
> > When Apple makes a change like that it impacts a lot of customers because they have way fewer skews.

> > **theandrewbailey**: I can confirm this. I work at an e-waste recycling company, and the vast majority of my inventory is corporate IT decommissioned gear. About 1 out of 10 laptops I tear down has a cellular modem, going back to about Intel Core 5th gen.

> **Glemllksdf**: Thats quite surprising thing to me and weirdly obvious.
> 
> If you are single, have a phone contract, you would need some extra contract for a landline internet and wifi router because thats what a lot of people just do and now they can just add an esim and pay a little bit more.
> 
> Interesting that this sounds/feels a lot more right or useful than it did 5 years ago.

> **panny**: I can't imagine a worse privacy nightmare. Always on backdoored baseband in 5G with a unique permanent IPv6 address assigned to the machine. Okay, maybe it could be worse if each user account is assigned its own unique IPv6 perma-cookie.

> > **nottorp**: > Okay, maybe it could be worse if each user account is assigned its own unique IPv6 perma-cookie.
> > 
> > They will. One from facebook, one from google, one from tiktok, several from Palantir and its partners...

> > **Dagger2**: You're thinking of MAC addresses. Machines don't have permanently-assigned v6 addresses, rather the IP is assigned by whatever network they're currently attached to and will change based on that network's whims, just like it does in v4.

> > **merpkz**: As if people doesn't already carry always online machine in their pockets

---

### imoverclocked

The question is, "what will the graph look like in the next 10 years?"

I get the whole s-curve trend but if I squint at 2017, there is an inflection to slow the s-curve down.

Annoyingly, when setting up service with a fiber company in the last couple months, I explicitly asked about IPv6 connectivity and they said, "yes." Turns out "yes, but not in my region."

> **snvzz**: >I explicitly asked about IPv6 connectivity and they said, "yes."
> 
> ABC, Always Be Closing.

---
