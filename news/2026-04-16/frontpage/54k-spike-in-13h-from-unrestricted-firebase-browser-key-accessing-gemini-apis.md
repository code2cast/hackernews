# €54k spike in 13h from unrestricted Firebase browser key accessing Gemini APIs

- **Link**: https://discuss.ai.google.dev/t/unexpected-54k-billing-spike-in-13-hours-firebase-browser-key-without-api-restrictions-used-for-gemini-requests/140262
- **HN**: https://news.ycombinator.com/item?id=47791871
- **Score**: 251 points
- **By**: zanbezi
- **Date**: 2026-04-16 12:13 UTC
- **Comments**: 166

---

## Comments

### benterix

> We had a budget alert (€80) and a cost anomaly alert, both of which triggered with a delay of a few hours

> By the time we reacted, costs were already around €28,000

> The final amount settled at €54,000+ due to delayed cost reporting

So much for the folks defending these three companies that refused to provide hard spending cap ("but you can set the budget", "you are doing it wrong if you worry about billing", "hard cap it's technically impossible" etc.)

> **startages**: Yeah, that the main reason I never use services like Google Cloud if I don't have to, it's impossible to have a hard cap, and anyone pretending to be an expert, is just off.
> Google says that they can't provide a hard cap because that would mean shutting down all your services..bla bla, but at least give users the option.

> > **logankilpatrick**: We have spend caps at the billing account level and the project level (developer set) in the Gemini API now. There is up to a 10 minute delay in processing everything but this should significantly mitigate the risk here: [https://ai.google.dev/gemini-api/docs/billing#tier-spend-cap...](https://ai.google.dev/gemini-api/docs/billing#tier-spend-caps)
> > 
> > By default, new Tier 1 paid accounts can only spend $250 in a given month.

> **Leomuck**: That's actually crazy. So I can build a project I love, that does good, but somehow get in a situation where I'm accidentally paying 30.000€ (or 50.000€) to a big tech company? How is that fair? I mean yes, as a software engineer, you ought to reflect on all possible weaknesses, but there was a time when overlooking something meant something completely different than being down 30/50k. That is actually life-altering.

> > **benoau**: Your kid can do this in a smartphone game designated suitable for children, heavily optimized to exacerbate the possibility, and depending on where you live they can just choose not to refund you.
> > 
> > When the FTC went investigating a decade-ish ago they found Facebook saying the quiet parts out loud: it was all extremely deliberate.

> > **sdevonoes**: It’s not fair. Google, Amazon, Microsoft… they have never played fairly. They will never do.

> **ch0wn**: This should be illegal. If a contractor your hired to swap out a tile on your bathroom floor billed you for remodelling your back garden, you would obviously have the legal right to refuse that.

> > **layer8**: My guess is that they would have a good chance to fight this in court and get their money back, but it’s a pain having to go through such a lawsuit.

> > **jubilanti**: Not if your contractor had you first sign a 15 page contract that commits you to whatever costs they dream up and requires forced arbitration by a corporate friendly firm when any dispute arises.
> > 
> > Because that's somehow normal in today's tech world.

> > > **sdevonoes**: So if their TOS say they can also rape my cat, then I cannot do anything about it, right? Ridiculous

> **Maxious**: > The Gemini API supports monthly spend caps at both the billing account tier and project levels. These controls are designed to protect your account from unexpected overages, and the ecosystem to ensure service availability
> 
> [https://ai.google.dev/gemini-api/docs/billing#project-spend-...](https://ai.google.dev/gemini-api/docs/billing#project-spend-caps)

> > **rtkwe**: The problem is it's specific to that API and defaults to uncapped so people who aren't using it and haven't heard about the issues with the Firebase API keys probably won't have set them.

> > > **isoldex**: Spend caps exist for Gemini (Maxious linked them) - they just default to OFF. For an API that can bill four figures per hour, opt-in safety by default isn't a UX choice, it's a billing strategy

> > > **zozbot234**: Except that Google's own statements are extremely clear that "leaked" (i.e. public) API keys should not be able to access the Gemini API in the first place: "We have identified a vulnerability where some API keys may have been publicly exposed. To protect your data and prevent unauthorized access, *we have proactively blocked these known leaked keys from accessing the Gemini API*. ... We are defaulting to blocking API keys that are leaked and used with the Gemini API, helping *prevent abuse of cost and your application data*." [https://ai.google.dev/gemini-api/docs/troubleshooting#google...](https://ai.google.dev/gemini-api/docs/troubleshooting#googles_security_measures_for_leaked_keys)
> > > 
> > > For extra clarity on the exact so-called "vulnerability" that Google identified, see: [https://news.ycombinator.com/item?id=47156925](https://news.ycombinator.com/item?id=47156925) This describes the very issue where some API keys were public *by design* (used for client-side web access), so the term "leaked" should be read in that unusually broad sense.  Firebase keys are obviously covered, since they're also public by design.
> > > 
> > > As for "Firebase AI Logic", it is explicitly different: it's supposed to be implemented via a proxy service so the Gemini API key is never seen by the client: [https://firebase.google.com/docs/ai-logic](https://firebase.google.com/docs/ai-logic)

> > **whywhywhywhy**: Why is the default uncapped then other than the hopes of billing people who screw up or get exploited.

> > > **logankilpatrick**: We have a bunch of different protections in place, every account has a billing account cap by default (see: [https://ai.google.dev/gemini-api/docs/billing#tier-spend-cap...](https://ai.google.dev/gemini-api/docs/billing#tier-spend-caps)), in the addition to the ability to set more granular developer spend caps.

> > > **drfloyd51**: See also: Why is the default cap so low? I lost €78bojillion because my API stopped working.

> **reaperducer**: *hard cap it's technically impossible*
> 
> These companies can sell your personal information in a microsecond in an advertising auction, but somehow can't figure out how to give you timely alerts that stop their cash flow.
> 
> Big shock.

> **varispeed**: This is clearly setup for VC backed companies where shareholders don't care about spend as long as they can brag about investing in this cool start up at dinner parties. Normal and true business should stay away.

> **janandonly**: Yet another good reason to use a pre-paid service.
> 
> There are many to choose from now, like Openrouter.com, PPQ.ai, and routstr.com.

> > **adriand**: You mean openrouter.ai. And yes, on reading this blog post, I immediately reviewed my API keys in OpenRouter to make sure that they were capped. My prod key was capped at $20/day (phew!) but my dev key had no cap, which I just updated. What a horrible story.

> **villgax**: Shirky’s principle at work is all

> **nurettin**: I'd buy the technically impossible angle.
> 
> Even if you manage to get your microservices to synch every penny spent to your payment account at realtime (impossible) you still have to waiver the excess, losing some money every time someone goes past their quota.

> > **benterix**: I invite you to look at the various solutions implemented by those public cloud providers that actually implemented this feature.

> > **bartread**: Sure, but 80 -> 28,000 -> 54,000 is a hell of a lot of slippage.
> > 
> > Trading platforms can guarantee a maximum slippage on stops, and often even offer guaranteed stops (with an attached premium), so I don’t see why Google and Firebase can’t do similar.
> > 
> > The way it works at present is ridiculous.

> > > **zbentley**: Yep. And cloud providers could eat any slippage cost (enforcing, say, every 5 minutes by stopping service) without even a rounding error on their balance sheets.
> > > 
> > > The fact that they don’t indicates that there’s no market reason to support small spenders who get mad about runaway overages, not that it’s technically or financially hard to do so.

> > > **nurettin**: > Trading platforms can guarantee a maximum slippage on stops
> > > 
> > > Yeah no, physically impossible. If nobody is selling at that price, there is no guarantee your sell stop will execute near that price. They can sweep the market, find the best seller price and execute.
> > > 
> > > There might be a costly way to do it with microservices as I indicated, but your example easily falls apart.

> > **walthamstow**: I'm with you. And what do you even do when the quota is breached, nuke the resources? People will complain about that just as much as overspends.
> > 
> > I don't buy the 'evil corp screwing people' angle either. They are making farrr too much legit money to care about occasionally screwing people out of 20k and 50k.

> > > **johnmaguire**: If I set a limit, and you cut off my service because I reached the limit, I would definitely not "complain just as much" as if I set a limit and you allowed me to spend past it.
> > > 
> > > We're not talking about an EC2 or EBS volume here, this is access to an API.

---

### JohnScolaro

> We had a budget alert (€80) and a cost anomaly alert, both of which triggered with a delay of a few hours. By the time we reacted, costs were already around €28,000.

I had a similar experience with GCP where I set a budget of $100 and was only emailed 5 hours after exceeding the budget by which time I was well over it.

It's mind boggling that features like this aren't prioritized. Sure it would probably make Google less money short term, but surely that's more preferable to providing devs with such a poor experience that they'd never recommend your platform to anyone else again.

> **arcticfox**: I get furious every time this comes up and somehow there are bootlickers ready to defend big tech on it.
> 
> My ~2 person small business was almost put out of business due to a runaway job. I had instrumented everything perfectly according to the GCP instructions - as soon as billing went over the cap the notification was hooked up to a kill switch, which it did instantly.
> 
> GCP sent the notification they offered as best practice 6 HOURS late. They did everything they could to not credit my account until they realized I had the receipts. They said an investigation revealed their pipeline was overwhelmed by the number of line items and that was the reason for the lag. ... The exact scenario it is supposed to function in. JFC.

> **zanbezi**: Exactly my thoughts, can not really understand how delayed alerts are acceptable... Have you managed to settle the cost with Google, what was the outcome?

> > **sillysaurusx**: Back in 2020 I had a similar situation. Ended up charging $500 due to an overnight TPU training run using egress bandwidth across zones.
> > 
> > Google support was surprisingly understanding, after I explained the issue. They asked some clarifying questions. Then they said that they can offer a *one time* refund for this case.
> > 
> > Since then I was paranoid not to accidentally do it again. I don't know whether GCP would refund a second time.

> > > **genxy**: GCP charging for interzone traffic is an interesting financial choice. They own all the infra and in many cases this is literally moving from building to building.

> **Hamuko**: Which cloud provider actually prioritises features that cut off your money supply? Because AWS sure as shit doesn't either.

> > **benterix**: Amazon, Microsoft and Google don't offer hard cap. Most other/smaller public cloud providers do. The reasons are quite obvious.

> > > **zotex**: we love Amazon, Microsoft and Google being altruistic and making sure your not burdened with too much money

> **miltonlost**: > Sure it would probably make Google less money short term, but surely that's more preferable to providing devs with such a poor experience that they'd never recommend your platform to anyone else again.
> 
> Welcome to late-stage capitalism, where there is no long-term thinking, only short-term profit stealing, and Fuck You I Got Mine.

---

### embedding-shape

Considering the amount of repositories on public GitHub with hard-coded Gemini API tokens inside the shared source code ([https://github.com/search?q=gemini+%22AIza%22&type=code](https://github.com/search?q=gemini+%22AIza%22&type=code)), this hardly comes as a surprise. Google also has historically treated API keys as non-secrets, except with the introduction of the keys for LLM inference, then users are supposed to treat those secretly, but I'm not sure everyone got that memo yet.

Considering that the author didn't share what website this is about, I'd wager they either leaked it accidentally themselves via their frontend, or they've shared their source code with credentials together with it.

> **zozbot234**: > Google also has historically treated API keys as non-secrets, except with the introduction of the keys for LLM inference, then users are supposed to treat those secretly
> 
> This was reported a *long* time ago, and was supposed to be fixed by Google via making sure that these legacy public keys would not be usable for Gemini or AI. [https://news.ycombinator.com/item?id=47156925](https://news.ycombinator.com/item?id=47156925) [https://ai.google.dev/gemini-api/docs/troubleshooting#google...](https://ai.google.dev/gemini-api/docs/troubleshooting#googles_security_measures_for_leaked_keys) "We are defaulting to blocking API keys that are leaked and used with the Gemini API, helping prevent abuse of cost and your application data." Why are we hearing about this again?

> > **addandsubtract**: FWIW, I just create a new Gemini API key today, and it had a different format than my old ones (created 10 days ago). So maybe they changed something?

> > **PunchyHamster**: the topic is cost overruns. they still allow for cost overruns. What's so hard to comprehend ?

> **ckbkr10**: theres not a single real gemini api key in the results

> > **dminik**: Try this one. Should remove most readme keys:
> > 
> > Edit: self censor based on a request

> > > **sillysaurusx**: I know you're well within your rights to post this, but would you consider replacing your comment with something like "It's easy to find working keys on github if you search the appropriate terms"?
> > > 
> > > Think of it this way: although you're not to blame, HN drives a lot of traffic to your preconfigured github search. There are also bad actors who browse HN; I had a Firebase charge of $1k from someone who set up an automated script to hammer my endpoint as hard as possible, just to drive the price up. Point being, HN readers are motivated to exploit things like what you posted.
> > > 
> > > It's true that the github search is a "wall of shame", and perhaps the users deserve to learn the hard way why it's a good idea to secure API keys. But there's also no benefit in doing that. The world before and after your comment will be exactly the same, except some random Gemini users are harmed. (It's very unlikely that Google or Github would see your comment and go "Oh, it's time we do something about this right now".)
> > > 
> > > EDIT: I went through the search results and confirmed that the first several dozen keys don't work. They report as error code 403 "Your API key was reported as leaked. Please use another API key." or "Permission denied: Consumer 'api_key:xxx' has been suspended." So at least HN readers will need to work hard(er) to find a valid key.
> > > 
> > > I wonder how you report a gemini API key as leaked... Searching "report gemini api key leaked" on Google only brings up similar horror stories (a $55k bill, waived [https://www.reddit.com/r/googlecloud/comments/1noctxi/studen...](https://www.reddit.com/r/googlecloud/comments/1noctxi/student_hit_with_a_5544478_google_cloud_bill/)) and (a $13k bill from 3d ago [https://www.reddit.com/r/googlecloud/comments/1sjzat3/api_ke...](https://www.reddit.com/r/googlecloud/comments/1sjzat3/api_key_compromised_13428_fraudulent_charges/))

> > > **ratsimihah**: this is such a wall of shame haha

> > > **duskdozer**: Oh, wow.

> > **imdsm**: [https://github.com/JustForSO/Sentra-Auto-Browser/blob/c048d3...](https://github.com/JustForSO/Sentra-Auto-Browser/blob/c048d333cb99ca735e0028840886dc26a6b5a081/README.md?plain=1#L172)

> > **embedding-shape**: Setup a watcher and you'll come across live ones eventually :)

> **mdrzn**: ...JCip3SJw => Your API key was reported as leaked. Please use another API key.
> 
> ...afnt0t-E => Your API key was reported as leaked. Please use another API key.
> 
> ...-UYzYTYU => Your API key was reported as leaked. Please use another API key.
> 
> I think they all get immediately reported as leaked and invalidated.

> **singpolyma3**: Um. What? In what world are API keys not secrets?

> > **boredpudding**: Google API keys have been used for ages on the frontend. For example on Google Maps embeds. Those are not possible without exposing a key to the frontend. They weren't secret, until Gemini arrived.
> > 
> > [https://trufflesecurity.com/blog/google-api-keys-werent-secr...](https://trufflesecurity.com/blog/google-api-keys-werent-secrets-but-then-gemini-changed-the-rules)
> > 
> > [https://medium.com/@ahhyesic/your-google-maps-api-key-now-ha...](https://medium.com/@ahhyesic/your-google-maps-api-key-now-has-access-to-gemini-ai-and-you-were-never-told-c8800129757b)
> > 
> > [https://www.malwarebytes.com/blog/news/2026/02/public-google...](https://www.malwarebytes.com/blog/news/2026/02/public-google-api-keys-can-be-used-to-expose-gemini-ai-data)

> > > **someothherguyy**: If one ignores 70% of the documentation, it makes for a demonizing blog post about it, sure.
> > > 
> > > "
> > > API keys for Firebase services are not secret
> > > 
> > > API keys for Firebase services only identify your Firebase project and app to those services. Authorization is handled through Google Cloud IAM permissions, Firebase Security Rules, and Firebase App Check.
> > > 
> > > All Firebase-provisioned API keys are automatically restricted to Firebase-related APIs. If your app's setup follows the guidelines in this page, then API keys restricted to Firebase services do not need to be treated as secrets, and it's safe to include them in your code or configuration files.
> > > Set up API key restrictions
> > > 
> > > If you use API keys for other Google services, make sure that you apply API key restrictions to scope your API keys to your app clients and the APIs you use.
> > > 
> > > Use your Firebase-provisioned API keys only for Firebase-related APIs. If your app uses any other APIs (for example, the Places API for Maps or the Gemini Developer API), use a separate API key and restrict it to the applicable API."
> > > 
> > > [https://firebase.google.com/support/guides/security-checklis...](https://firebase.google.com/support/guides/security-checklist#api-keys-not-secret)

> > **darrenf**: In Firebase world API keys are for identification, not authorisation.
> > 
> > [https://firebase.google.com/docs/projects/api-keys](https://firebase.google.com/docs/projects/api-keys)
> > 
> > *Public by design: API keys for Firebase services only identify your Firebase project and app to those services. Authorization is handled through Google Cloud IAM permissions, Firebase Security Rules, and Firebase App Check.*

> > **fg137**: Google's world. They explicitly tell you that API keys are not secrets.
> > 
> > [https://trufflesecurity.com/blog/google-api-keys-werent-secr...](https://trufflesecurity.com/blog/google-api-keys-werent-secrets-but-then-gemini-changed-the-rules)

> > > **lxgr**: API keys *for Firebase*. While Google really messed up here, I doubt they ever published anything claiming that *no Google API keys at all* are secrets.

> > **embedding-shape**: In the frontend world where you have client-side API keys talking directly to 3rd party services from the client. Think things like Google Maps and similar.

> > > **londons_explore**: Which is a stupid idea for something where there is billing involved...      Anyone on the internet can take that key and scrape the Google maps API (faking  the referer header) and cost you $$$$$.
> > > 
> > > Google should have simply done with by origin URL if they wanted stuff to be open like that.

> > **lxgr**: Public API keys are a thing. Arguably they are poorly named (it's really more of a client identifier), and modeling them as primarily a key instead of primarily as a non-secret identifier can go very wrong, as evidenced here.

---

### dabedee

As others have said, this is a "feature" for Google, not a bug. There is no easy way to set a hard cap on billing on a project. I spent the better time of an hour trying to find it in the billing settings in GCP, only to land on reddit and figuring out that you could set a budget alert to trigger a Pub/Sub message, which triggers a Cloud Function to disable billing for the project. Insanity.

> **onemoresoop**: Call it for what it is, an antifeature, a trap for the user.

> **alasano**: My favorite Google LLM benchmark is asking Gemini models to create a script that fetches API usage (just request counts) for a project from GCP.
> 
> 100% failure rate.

> **lxgr**: This is presumably by design: How can it be the vendor's fault if *your custom billing protection implementation* failed you at a critical time? Much harder to defend against a switch on their dashboard allowing billing overshoot.

> **imafish**: This is from my experience the same in AWS and Azure. I would love for a kill-switch if the usage goes above a critical threshold. 5 hours down time will not kill my app but a huge cloud bill might.

> **intended**: As the other user said - this would be an anti-feature and user hostile.
> 
> This is a sign that somehow there isn’t sufficient incentive to work on these features.

---

### p2detar

I read the following [0] and immediately went to my firebase project to downgrade my plan. This is horrific.

> Yes, I’m looking at a bill of $6,909 for calls to GenerativeLanguage.GenerateContent over about a month, none of which I made. I had quickly created an API key during a live Google training session. I never shared it with anyone and it’s not pushed to any public (or private) repo or website.

0 - [https://discuss.ai.google.dev/t/unexpected-gemini-api-billin...](https://discuss.ai.google.dev/t/unexpected-gemini-api-billing-spike/114095/7)

> **jasonjmcghee**: So someone took a picture of the key at the live training session or something? What's the suspected cause?

---

### alibarber

Forgive my ignorance - but what's the payoff for fraudsters in getting access to a generative AI service for a short-ish period of time, before they get cut off?

With EC2 / GCC credentials, I could understand going all out on bitcoin mining - but what are they asking the AI to do here that's worth setting up some kind of botnet or automation to sift the internet for compromised keys?

> **Aurornis**: Early Generative AI was popular with spammers before it became mainstream because it could be used to write infinite variations of spam messages. Making each message unique is more likely to bypass spam filters.
> 
> There are also a lot of AI use cases that require a lot of token spend to brute force a problem. Someone might want to search for security exploits in a codebase but they don’t want to spend the $50,000 in tokens from their own money. Finding someone’s key and using it as hard as possible until getting locked out could move these projects forward.

> **LelouBil**: Totally speculating here, but maybe they provide some sort of LLM as a service, and they rotate stolen API keys in the background so they don't have to pay anything ?
> 
> Or they use the LLMs for criminal purposes (like automated social engineering) and so the API key can't be traced to their personal info (but they could also use a local model for this, so I don't know).

> **lxgr**: There are plenty of services offering AI inference at a discount. Some of these will be using your data for future distillation; others might be making use of bulk discounts and passing these through to a number of individual users (while taking on billing, support etc. risk) – and maybe some are just selling tokens falling off the back of a truck?

> **varispeed**: If they work for hostile state, the payoff is destruction of economy and social contract. Damage here, damage there. It all adds up.

> **jddj**: Distillation maybe?

---

### naturalauction

We had this exact same problem (the key initially wasn’t a secret but became a secret once we enabled Gemini API with no warnings).

We managed to catch it somewhat early through alerting, so the damage was *only* $26k.

We asked our Google cloud support rep for a refund - they initially came back with a no but now the case is under further consideration.

I’d escalate this up the chain as much as possible.

> **whalesalad**: they dgaf. i've been told anything over 10k requires sign off from the executive team

---

### time0ut

It is scary building on the public cloud as a solo dev or small team. No real safety net, possibly unbounded costs, etc. A large portion of each personal project I do is spent thinking about how to prevent unexpected costs, detect and limit them, and react to them. I used to just chuck everything onto a droplet or VPS, but a lot of the projects I am doing lately need services from Google or AWS. I tend to prefer GCP at this point because at least I can programmatically disconnect the billing account when they get around to tripping the alert.

---

### mdrzn

Related: [https://news.ycombinator.com/item?id=47156925](https://news.ycombinator.com/item?id=47156925)

---

### mcccsm

Two things that should be default on any GCP project touching generative-AI APIs:

1 API-key restrictions by HTTP referrer AND by API (`generativelanguage.googleapis.com` only),

2 a billing budget with a Pub/Sub "cap" action, not just an email alert. Neither is on by default, and almost nobody sets them before shipping. 13 hours is actually fast for detection. most teams find out at end-of-month reconciliation.

> **PunchyHamster**: I want API keys with monthly and hourly quotas and RATE LIMITING.
> 
> like 50k requests per hour, above that 1/s/client up to 20 req/sec.
> 
> I don't want to shotgun my service for every user if one user is misbehaving. I want to set rate of bleeding

---

### drtz

> Are there recommended safeguards beyond ... moving calls server-side?

This implies the API calls originated in the client, suggesting the client may have had they API key.

> **dpkirchner**: That's standard for Firebase apps. It's also recommended by Google (they describe the keys as "public by design").

> > **Retr0id**: Feels like a confusing thing to name "key" if it's presumably more of an identifier.

> **pwdisswordfishs**: It's "implied" throughout the whole post (or more like assumed that the reader understands this, because it's the basic premise of the problem).  It's why they link to a post that explains the basic concept after a remark that "This describes our issue in more detail".
> 
> > *tl;dr Google spent over a decade telling developers that Google API keys (like those used in Maps, Firebase, etc.) are not secrets. But that's no longer true: Gemini accepts the same keys to access your private data. We scanned millions of websites and found nearly 3,000 Google API keys, originally deployed for public services like Google Maps, that now also authenticate to Gemini even though they were never intended for it. With a valid key, an attacker can access uploaded files, cached data, and charge LLM-usage to your account. Even Google themselves had old public API keys, which they thought were non-sensitive, that we could use to access Google’s internal Gemini.*
> 
> From Google themselves, in the Firebase docs:
> 
> > API keys for Firebase services are not secret.  Firebase uses API keys only to identify your app's Firebase project to Firebase services, and not to control access to database or Cloud Storage data, which is done using Firebase Security Rules.  For this reason, you do *not* need to treat API keys for Firebase services as secrets, and you can safely embed them in client code.
> 
> <[https://firebase.google.com/support/guides/security-checklis...](https://firebase.google.com/support/guides/security-checklist#api-keys-not-secret)>
> 
> ... or at least that's what it used to say, until they quietly updated the docs to say this:
> 
> > API keys for Firebase services are not secret.  API keys for Firebase services only *identify* your Firebase project and app to those services.  *Authorization* is handled through Google Cloud IAM permissions, Firebase Security Rules, and Firebase App Check.
> 
> > All Firebase-provisioned API keys are *automatically* restricted to Firebase-related APIs.  If your app's setup follows the guidelines in this page, then *API keys restricted to Firebase services* do *not* need to be treated as secrets, and it's safe to include them in your code or configuration files.
> 
> Followed later by (in different section):
> 
> > Use your Firebase-provisioned API keys *only* for Firebase-related APIs.  If your app uses any other APIs (for example, the Places API for Maps or the Gemini Developer API), use a separate API key and restrict it to the applicable API.

> **embedding-shape**: Yeah, the amount of people creating, running and maintaining websites yet don't understand how websites actually work in practice is very high and seems we haven't even come close to the ceiling yet.

---

### Illniyar

I think the logistics of calculating cost in real time is something that is extremely hard. I don't think there is one big cloud service provider that has hard limits instead of alerts.

As long as they revert the charge when notified of scenarios like this , and they have historically done so for many cases, it's fine. It's an acceptable workaround for a hard problem and the cost of doing business ( just like Credit Cards accept a certain amount of loss to fraud as part of business)

> **Nathanba**: Why would it be hard to calculate cost? Multiply a fixed price * requests/time ? It doesn't have to be exact in real time, it just has to report something approximately useful in realtime.
> 
> It's absolutely not fine to be at the mercy of other people, that's what we buy cloud products or really any products for: So that we are not at the mercy of hardware faults, bad weather, bad teeth, hunger, thirst, [insert anything]

> **wongarsu**: Cutting off at the exact cent is difficult, but a hard limit that triggers within one dollar of the actual limit should really be possible
> 
> If for some resources you can't sample measurements fast enough you could weaken it to "triggers within one dollar or five minutes after cost overrun, whichever comes later". But LLM APIs are one of those cases where time isn't a factor, your only issue is that if you only check quota before each inference a given query might bring you over

> **EdwardDiego**: > I think the logistics of calculating cost in real time is something that is extremely hard.
> 
> What makes you think that?

> **zulban**: Ridiculous. They are clearly not trying at all. A hard wall preventing going over budget by 100x in a couple hours is not some devilishly complicated decentralized system problem.
> 
> Don't tote the party line.
> 
> Same reason why Azure AI only has easy rate limits by minute, not by day or week or month. Open source proxy projects do it easily tho. Think about the incentives.
> 
> Going over a hard cap by 3% would be a reasonable failure to make, not by 30000%.

---

### ozlikethewizard

The top comment on the post physically hurt me. We've moved past the era of keep env files in code bases and are now actually serving them lol.

---

### luanmuniz

Unfortunately, yet just another story like this. One of these unexpected usage charges in the thousands appears every month, and with the same automatic denied too. This is one of the reasons I just stopped using these kinds of pay-per-usage cloud services long ago. At best, I still use services that have hard-bounded usage limits, like EC2 from AWS, where one instance can never go beyond 24h/day usage and is always capped, with shutdowns when exceeded, and limited credit cards, too.

It's super frustrating that this is the only option to realistically deal with this issue, since all stories end up the same way: The cloud company just saying "f* you, we don't care, pay up." and legal fees are always expensive :(

> **embedding-shape**: > At best, I still use services that have hard-bounded usage limits, like EC2 from AWS, where one instance can never go beyond 24h/day usage and is always capped, with shutdowns when exceeded, and limited credit cards, too.
> 
> Is this possible on AWS today? I'm the same way, if I cannot set a hard-limit for the billing so I can know for a fact how much it'll maximum cost in a month, I'm not interested in using that service for anything. Which is one of the top reasons I've stayed clear of AWS, they used to have only billing-alerts, but you couldn't actually set limits, guess one step forward that they've finally implemented that now.

---
