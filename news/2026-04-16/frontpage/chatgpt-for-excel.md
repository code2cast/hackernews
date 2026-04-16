# ChatGPT for Excel

- **Link**: https://chatgpt.com/apps/spreadsheets/
- **HN**: https://news.ycombinator.com/item?id=47785397
- **Score**: 258 points
- **By**: armcat
- **Date**: 2026-04-15 21:21 UTC
- **Comments**: 165

---

## Comments

### lateforwork

This looks bad for Microsoft. They added a Copilot button to all their products but it doesn't do much more than open a chat side panel.

I recently tried Claude Cowork for PowerPoint and I was stunned by the content as well as design quality of the deck it produced. That's a threat for Microsoft because now you don't need the editing tools of PowerPoint, AI replaces it, so all you need is the presentation mode of PowerPoint.

Copilot for Excel is useless. Ask it what is in cell A1 and it can't answer. I am looking forward to trying ChatGPT for Excel.

> **brookst**: PowerPoint is the poster child for the class of applications that AI totally obsoletes:
> 
> * A large application whose outputs are independent of the all (people still print slides; when presenting nobody knows or cares what app was used)
> * Complicated and requires users to learn lots of skills unrelated to the work they’re doing (compare to Excel, where the model and calculations require and reflect domain knowledge about the data)
> * Practically zero value add in document / info management (compare to word where large documents benefit from structure and organization)
> 
> We’re pretty close to presentations just being image files without layers and objects and smartart and all that.
> 
> AI will come for all productivity tools, but PowerPoint will be the canary that gets snuffed first, and soon.

> **nsiemsen**: Claude for excel is already amazing. Fully capable of doing junior work. Formatting is great. Can refactor large multi-tab spreadsheets. It just burns tokens. If OpenAI is going to subsidize this on the monthly enterprise plans for a while then it's a game changer.
> 
> Claude for Excel (I work in finance) was one of the absolutely critical reasons we added Anthropic enterprise licenses. But they've turned out to be quite expensive ($100/day for heavy users). We'll see what OpenAI's quotas are.

> > **infecto**: Work in a firm similar to yours and we have been going to though the motions of figuring ways for the bullpen to make use of these tools and would love to hear your thoughts if you would be willing to share!

> > **wouldbecouldbe**: I work with large files a lot, running claude code on it is not token intense at all. Probably because it does a lot with scripts. But its a bit more raw, but i think in the end more powerful. Have to pick a good excel library and language. I do node, maybe python can work as well

> > **intended**: How’s that been in practice ? From what I’ve been following - Claude in finance results in models with errors that an analyst won’t make.
> > 
> > You get models that are formatted and structured and which balance - but there are errors introduced which an analyst / human wouldn’t make.
> > 
> > Stuff like hard coded values, or incorrect cell logic which guarantees the model balances.

> > > **balderdash**: Just my experience, it’s not a solution but rather a productivity tool. I mostly use it for tasks I can do myself but it would probably take 20-30min to dial in - now Claude can do it in 2-3min. (E.g. in a data table - add a new column that checks column a if the data is a, do x, if the data is b, do y, if the data is c, do z - then combine that with the word after the hyphen in column b —- or another example —- create a new sheet that is the same format as sheet one but show calculates the difference between column a and b bot for sheets 1-12 in a summary)
> > > 
> > > I don’t get good results when I just have Claude build things on its own - but for these types of specific productivity tasks I can save a couple of hours here and there.

> > > **mukmuk**: From my experience, LLM performance in these areas is being massively oversold. I have repeatedly tried using Claude to modify a range of models typical of investment banking / private equity / sellside research contexts, and the results have been generally disastrous. On multiple occasions, the xlsx would no longer open.

> > **p_ing**: Cheaper to get M365 Copilot licenses for the Claude models in Excel.

> > > **jxmesth**: I tried looking this up but wasn't able to find info on this on Microsoft's website. Do you have a link for this?

> > > **WillAdams**: What are the costs on that?
> > > 
> > > Does this remove (or at least increase) the upload limit?

> **giancarlostoro**: I am still surprised that outside of open source AI models, Microsoft is just routing to external models, to a degree its kind of smart because they don't have to have all the skin in the game for the infrastructure, plus they sell some of the hosting anyway, but man. Why does Microsoft not have a frontier model yet? Would have been a great time any time in the last few years to introduce a real Cortana AI model.

> > **ebiester**: They explicitly said they were ceding the frontier model game to others, and that they were content saying a few months behind the state of the art. In the long run, this is an interesting freeloader play that a few people are making. [https://www.cnbc.com/2025/04/04/microsoft-ai-chief-sees-bene...](https://www.cnbc.com/2025/04/04/microsoft-ai-chief-sees-benefits-to-ai-models-that-are-months-behind.html)

> **evanjrowley**: There is a significant difference in experience between Copilot Basic for a M365 user whose IT admins have blocked integration capabilities with Sharepoint content vs Copilot Premium for a M365 user whose IT admins have allowed integration capabilities with Sharepoint content.

> > **interroboink**: A recent funny story on this topic: [https://idiallo.com/blog/what-is-copilot-exactly](https://idiallo.com/blog/what-is-copilot-exactly)
> > 
> > HN discussion: [https://news.ycombinator.com/item?id=47603231](https://news.ycombinator.com/item?id=47603231)

> > **mohamedkoubaa**: Microsoft is better off not allowing copilot basic because of the reputational harm it will do. Not that they are thinking through copilot rationally

> > > **basch**: it was a good name when chosen.  too bad they have burned bob, clippy, cortana, sydney, and copilot already.

> **LuxBennu**: Chatgpt for Excel is still an office add-in running in the same sandbox though. strongpigeon described the exact bottleneck upthread, process boundary crossings, context.sync() roundtrips that take seconds on web. That's a platform limitation, not a model limitation.
> Swapping AI behind the add-in doesn't fix the fundamental constraint that third-party add-ins can't deeply integrate with Excel's runtime the way a native feature can. If copilot is bad despite having more access to excel internals(I don't like how Copilot is designed or implemented tho), an add-in with less access is likely not be better.

> > **angadsg**: Would love for you to try both copilot and ChatGPT for Excel. Agreed on the limitations - but in our experience, ChatGPT for Excel does really well on complex sheets.

> > **com2kid**: There is an irony here that this would be more performant with a 2002 coding model. A native plugin, COM, OLE, whatever. C++, crash prone, but fast.

> > > **strongpigeon**: Maybe but not drastically so. My guess is that most of the slowness comes from the tool calls round tripping+processing on Anthropic/OpenAI’s servers rather than the app latency.
> > > 
> > > That’s without talking about the poor UI and security story of COM add-ins and the inability to run on Excel for iOS.

> > **phyalow**: Try writing your own comments rather than posting AI slop

> **Gareth321**: > They added a Copilot button to all their products but it doesn't do much more than open a chat side panel.
> 
> I was hyped when I heard about Copilot. "I can tell it to make pivot tables now!" When I tried to use it I was shocked how underbaked it was. Below even my worst expectations. This really was someone shoving ChatGPT into Excel with almost zero additional effort. Copilot can't DO anything useful.

> > **chris_money202**: stride.microsoft.com -> this is a virtual machine instance with developer tools that allow for same sort of work Claude cowork does. Copilot in excel has to access the excel document through excel provided APIs and can’t completely redo the document like cowork does everytime running developer scripts to generate it because the document instance is open. The model of work is entirely different.

> **screye**: If AI winning means that data center companies win out, then the wins for Azure will more than make up for the death of Office.
> 
> I am surprised that Microsoft's own copilot product is so far behind though.

> > **boringg**: Aren't they providing a wrapper for the work of another company?  IE msft isn't actually doing any foundational work thus they can't meaningfully move product capability,  just wait for the model to improve and integrate it?

> **ryanjshaw**: There’s a magic button you have to press to make it integrate fully. Everybody is confused about why this isn’t the default behavior.

> **vipipiccf**: I've had the same experience. Copilot for Excel can't even parse basic cell references. Meanwhile Claude handles document formatting in one pass. The catch is it works externally, not inside the app, but at least it works.
> 
> The MCP ecosystem is what makes this interesting. Claude isn't just a chat panel bolted onto existing software, it's building integrations that actually manipulate the files. Microsoft had the distribution advantage but they're losing on capability.

> > **chris_money202**: stride.microsoft.com -> microsoft has this stuff you just don’t know it unless you are an M365 power user

> > > **compass_copium**: I would consider myself an M365 power user and I was not aware of this. It is not well promoted--and after all the Copilot crap, I would be annoyed even if it was.
> > > 
> > > Regardless, I just tried to log in with my work MS account, and I can't do so.

> **vessenes**: Microsoft has rights to all this IP. So, it might look bad for their product folks, but for the corporation this is great, to the extent it works.

> **sarreph**: > This looks bad for Microsoft.
> 
> Maybe(?) from a product catalogue perspective... But from a strategic perspective less so because they own ~27% of OpenAI.[0]
> 
> [0] - [https://openai.com/index/next-chapter-of-microsoft-openai-pa...](https://openai.com/index/next-chapter-of-microsoft-openai-partnership/)

> **xeyownt**: it would be bad for Microsoft if that would use Calc on LibreOffice.

> **ebbi**: We have many people in my wider team (Finance) that are AI skeptics purely because of their experience with Copilot. Like they don't know what AI is actually capable of when outside of the shackles of Copilot.
> 
> Microsoft fumbled so badly here.

> **Handy-Man**: You have to use the "agent" toggle for Copilot to behave the same way lol. Otherwise its pretty simple chat interface with the context, that's all.

> **chris_money202**: stride.microsoft.com is the cowork equivalent I believe.

> > **p_ing**: Only for personal accounts. Enterprise customers have a Frontier agent called Copilot Cowork via the M365 Copilot app.... copilot.

> **bwat49**: its baffling how badly microsoft has handled copilot, this is exactly what copilot in office should have been

> **miohtama**: It's called Microslop for a reason.

> **d3Xt3r**: > I recently tried Claude Cowork for PowerPoint and I was stunned by the content as well as design quality of the deck it produced. That's a threat for Microsoft because now you don't need the editing tools of PowerPoint, AI replaces it, so all you need is the presentation mode of PowerPoint.
> 
> Actually, someone here posted a Claude Code skill recently that generates a presentation as a self-contained HTML5 file, so all you need is a browser.
> 
> PowerPoint, as a whole, is doomed.

> > **hgoel**: Powerpoint will continue to persist because other people need to be able to edit your slide deck without understanding your HTML.
> > 
> > My employer blocks office plugins, so I can't try Claude for PowerPoint, but sometimes I get Claude to generate Python scripts, which produce PowerPoint slides via python-pptx. This also benefits from being able to easily read and generate figures from raw data.
> > 
> > I don't really like the way Claude tends to format slides (too much marketing speak and flowcharts), but it has good ideas often enough that it's still worth it to me. So I treat this as a starting point and replace the bad parts.

> > **basch**: Or you could just talk to powerpoint, which creates a self contained pptx, which also plays anywhere.
> > 
> > we've hit this point where its cool to have claude reinvent every wheel just because it can.

> > > **d3Xt3r**: It's not self-contained, it requires PowerPoint to be indfled. Which is not an issue on corporate machines of course, but maybe you want to do a presentation for a general/broader audience.

> > **usrme**: I'd love to get a link to that comment/post!

> > **jason_zig**: I'm not sure that's true - try getting someone to pull up an html5 file on their computer for a presentation...

> > > **DrSAR**: hrm, double-click and your browser does the rest.
> > > 
> > > For added benefit, full screen?
> > > 
> > > Until you need presenter notes or other niceties, this covers a large space of usage.

> > > **raincole**: You mean like, double-click?

> > **apsurd**: you could do that for the past 20 years. i've always hated slides as a medium for *anything*, but i've been proven wrong tine and again that people love their pp.

> > > **bad_haircut72**: Because it was drag and drop interface. This existed for HTML but because web pages got too complicated, so did the WYSIWYGs. By just being a program to show slides, the editing experience was manageable for anyone. But if you can hust type what you want to happen into claude, editng experience doesnt matter as much/at all

---

### arjie

I’ve always found it unbelievable how bad Gemini’s Google Sheets interaction is. Copying the sheets into Claude and then modifying them there and copying them back actually outperforms it.

Nowadays I just make single-purpose websites with Claude Code because Google Sheets has such poor AI integration and is outrageously tedious to edit.

They had all the parts and I have a subscription and it still does terrible things like prompt me to use pandas after exporting as a CSV. It will mention some cell and then can’t read it. It can’t edit tables so they just get overwritten with other tables it generates.

It reminds me of something a friend told me: he heard that Google employees do dogfood their products; some even multiple times every year. There’s no way anyone internal uses Sheets even that often.

> **bdcravens**: I tried it the other day to work on some exported CSVs when doing my taxes. I was finally able to get it to do what I wanted, but it was definitely an exercise, feeling like I was talking to Chat GPT from a couple of years ago. (as in a really smart but easily distracted and confused child)

> **charlieflowers**: I'm having great luck having Claude Code generate, read, and update spreadsheets by writing Python code that uses gspread.

> > **speleding**: It also works fine with Ruby and the "caxlsx" gem. Codex works fine with it as also.

> > **VadimPR**: Can it work with comments in sheets as well? When I looked into it, that seemed like a limitation.

> **yabutlivnWoods**: My local models interact with Sheets exclusively over the API with Python scripts I been curating for years
> 
> Given how well the API works, that we are discussing Googlers, my guess is that's how they dog food their services. Programmers don't get hired by Google for mouse skills.
> 
> The GUI is for spot checking results, final presentation.
> 
> If you're sitting there point-n-clicking everything into place perhaps consider you are doing it wrong.

> > **beepdyboop**: That sounds like an extremely narrow use case, compared to what the vast majority of Sheets users will be comfortable with

> > > **mbreese**: At the same time, it makes some sense... the programmers for a system aren't always the best users of a system. So if you're expecting them to dogfood their own system (Google Sheets), you might find that they test/interact with the system primarily through the API and not the GUI.
> > > 
> > > I have no idea if they do or not, but it's a plausible explanation...

> > > **yabutlivnWoods**: Use case feels like the wrong term.
> > > 
> > > Do you mean restricted workflow? Googles APIs are pretty much 1:1 to the GUI
> > > 
> > > And using Python makes it trivial to copy-paste out of files and other APIs with one run of Python
> > > 
> > > Versus all the fiddling in browser tabs with a mouse, it actually affords an incredibly wide set of options to quickly collate and format data

> > **intended**: How? This argument would make sense if sheets *wasn’t* targeted at a general audience.

> **dminik**: Yeah, the Sheets integration is weird. It's usually ok when it wants to place something down the first time. But then it seems incapable of making any changes to it. Or even acknowledging the data in the sheet. What's up with that?

> **buccal**: You should try MS Copilot which uses open source Python libraries to interact with Office file formats.
> 
> The libraries themselves are OK, but MS uses them stupidly. If you want to fill out some form in DOCX or XSLX format you will get broken formatting. And this is from Office company.

> > **darkwater**: Obviously. Because they didn't train the model on proprietary MS code. Which is bad but also good in some way, as it might force MS to support better their formats in the open source world.

> > **devmor**: I recently experimented with trying to generate a passable slide deck from a script and outline I had written beforehand. The ChatGPT integration built into Powerpoint was abysmally bad. Like to the point it was embarrassing as a product.
> > 
> > Claude one-shot something with a Python script that was pretty okay.

> **AznHisoka**: I love Sheets, but I dont care for using Gemini to interact with Sheets. It seems like a recipe for disaster. Do I really want it to muck around with thousands of rows and no intuitive way to diff its changes? Nope, sticking with basic Sheets

> **killerdhmo**: I mean, you're wrong. As a Xoogler, everything was in Sheets. Our roadmap was in Sheets. It's more they don't care.

---

### strongpigeon

Oh wow, I used to work on Excel Add-Ins about 10 years ago. Even got a patent for it. I'd be curious to see how they implemented the calls.

We came up with what I still consider a pretty cool batch-rpc mechanism under the hood so that you wouldn't have to cross the process boundary on every OM calls (which is especially costly on Excel Web). I remember fighting *so* hard to have it be called `context.sync()` instead of `context.executeAsync()`...

That being said, done poorly it can be slow as the round-trip time on web can be on the order of seconds (at least back then).

> **Acmeon**: Do you mean that you worked on the Excel Add-Ins platform in Excel (and not on a specific Add-In)?
> 
> If you were working on the platform itself, then I would be interested in hearing your more detailed thoughts on the matters you mentioned (especially since I am developing an open source Excel Add-In Webcellar ([https://github.com/Acmeon/Webcellar](https://github.com/Acmeon/Webcellar))).
> 
> What do you mean with a "OM" call? And why are they especially costly on Excel web (currently my add-in is only developed for desktop Excel, but I might consider adding support for Excel web in the future)?
> 
> In any case, `context.sync()` is much better than `context.executeAsync()`.

> > **strongpigeon**: I worked on the Excel Add-Ins platform at Microsoft, yes. By OM call I mean "Object Model" call, basically interacting with the Excel document.
> > 
> > The reason those calls are expensive on Excel Web is that you're running your add-in in the browser, so every `.sync()` call has to go all the way to the server and back in order to see any changes. If you're doing those calls in a loop, you're looking at 500ms to 2-3s latency for every call (that was back then, it might be better now). On the desktop app it's not as bad since the add-in and the Excel process are on the same machine so what you're paying is mostly serialization costs.
> > 
> > Happy to answer more questions, though I left MSFT in 2017 so some things might have changed since.

> > > **Acmeon**: Yeah, that makes sense. For some reason, I was under the impression that all calculations run locally in the browser, which would have been comparable to how Excel desktop works (i.e., local calculations). Is there a reason for why the Excel calculations run on the server (e.g., excessive workload of a browser implementation, proprietary code, difficult to implement in JavaScript, cross browser compatibility issues, etc.)? Furthermore, if the reason for this architecture is (or was) limitations in JavaScript or browsers, do you find it plausible that the Excel calculations will some day be implemented in Webassembly?
> > > 
> > > Regardless, I have always preferred Excel desktop over Excel web (and other web based spreadsheet alternatives). This information makes me somewhat less interested in Excel web. Nonetheless, I find Excel Add-Ins useful, primarily because they bring the capabilities of JavaScript to Excel.

> > > **com2kid**: Does Excel for Web still spin up an actual copy of Excel.exe on a machine somewhere? I heard that is how the initial version worked.

> > > **DaiPlusPlus**: > though I left MSFT in 2017 so some things might have changed since.
> > > 
> > > Honestly, I struggle to think about what has actually changed between Office 2013 and Office 2024 (and their Office 365 equivalents); I know the LAMBDA function was a big deal, but they made the UI objectively worse by wasting screen-space with ever-increasingly phatter *non-touch* UI elements; and the Python announcement was huge... before deflating like a popped party balloon when we learned how horribly compromised it was.
> > > 
> > > ...but other than that, Excel remains exactly as frustrating to use for even simple tasks - like parsing a date string - today just as it was 15 years ago[1].
> > > 
> > > [1]: [https://stackoverflow.com/questions/4896116/parsing-an-iso86...](https://stackoverflow.com/questions/4896116/parsing-an-iso8601-date-time-including-timezone-in-excel)

---

### angadsg

Hi everyone, engineer on ChatGPT for Excel here - we launched ChatGPT for Excel to bring the power of GPT-5.4 to Excel. Keen to hear feedback and happy to answer any questions!

> **bsenftner**: I've had a spreadsheet integrated with ChatGPT API for a few years already. It really was not until GPT-5.4 that the models were able to actually be useful.
> 
> What is the data model that you use for the spreadsheet itself? I found I could create a chat completion persona that believed it is one of the developers of a popular open source spreadsheet, and I put this "agent" directly inside the open source spreadsheet. I did this before tool calling was available at all, so I made my own system for that, and the "tools" are the API of that open source spreadsheet. My agent(s) that operate like this can do anything the spreadsheet can do, including operate the spreadsheet engine from the inside.

> **carderne**: What API/approach does it use to edit sheets?
> 
> I made a CLI (+skill) so agents could edit files with verbs like `insert A1:A3 '[1,2,3]'`, but did some evals and found it underperformed Anthropic's approach (just write Python).

> **rahimnathwani**: How well does this work compared with using GPT-5.4 in Nicopreme’s Pi for Excel?

> > **howdareme9**: have you got a link to this?

> > > **rahimnathwani**: Sorry, I got the author wrong.
> > > 
> > > It's here: [https://github.com/tmustier/pi-for-excel](https://github.com/tmustier/pi-for-excel)

> **e38383**: I probably could find some really useful things for it to help me … but all software nowadays only works outside my earth region :(
> 
> This time even for pro.

---

### dangoodmanUT

On this episode of "chatgpt just killed my startup"

Tune in for the next episode: Word

---

### TrackerFF

I've experimented with ChatGPT for spreadsheets the past 6 months, and while the results look nice now it has been *excruciatingly* slow for even the simplest spreadsheet. I'm talking 15-20 minutes to make some pretty basic calculator with graphs. IIRC, it used a lot of time purely on the styling.

> **angadsg**: Engineer on ChatGPT for Excel here. Useful feedback. We have improved the latency inside the add-in a lot and a lot more to come. We also have the Fast, Standard and Heavy thinking modes, where you can adjust the thinking time depending on the task complexity. Curious to hear your feedback once you try this out!

> **jannyfer**: Adding a tangential anecdote.
> 
> I asked GPT-5.4 High to draw up an architecture diagram in SVG and left it running. It took over an hour to generate something and had some spacing wrong, things overlapping, etc. I thought it was stuck, but it actually came back with the output.
> 
> Then I asked it to make it with HTML and CSS instead, and it made a better output in five seconds (no arrows/lines though).
> 
> SVG looks similar to the XML format of spreadsheets. I wonder if LLMs struggle with that?

> > **bob1029**: The LLMs seem to struggle at anything that isn't relatively well anchored in whatever space. HTML documents have a lot of foundation to them in the training data, so they seem to perform well by comparison to other things.
> > 
> > I just spent a few hours trying to get GPT5.4 to write strict, git compatible patches and concluded this is a huge waste of time. It's a lot easier and more stable to do simple find/replace or overwrite the whole file each time. Same story in places like Unity or Blender. The ability to coordinate things in 3d is really bad still. You can get clean output using parametric scenes, but that's about it.

> > > **jqbd**: Parametric scenes is the whole of Houdini and any node based compositor etc. so there is some applications no?

> > **scronkfinkle**: Claude's diagramming tool that they have built into their web UI is my goto for this task. It's reliable enough that I often will delegate to it first with what I need written in prose instead of using mermaid/lucid diagram

> > **brett-jackson**: I’d try asking it for a mermaid diagram. I think ChatGPT’s web interface will render them.

> > **cubefox**: Gemini is very good with SVG, but I don't really see the similarity to spreadsheets.

---

### chux52

How do the OpenAI models/reasoning effort map to Fast, Standard, Heavy in the add-in?

---

### flybrand

Several months ago, ChatGPT swore to me it had interoperability with both excel and Google Sheets. I spent 90 minutes thinking I was an idiot, trying to follow its guidance before asking the internet.

---

### Acmeon

In principle, I find it valuable to integrate tools. However, in this case I would be somewhat cautious, especially as "your chats, attachments, and workbook content — may be shared with OpenAI" (as per the Microsoft Marketplace description: [https://marketplace.microsoft.com/en-us/product/WA200010215?...](https://marketplace.microsoft.com/en-us/product/WA200010215?tab=Overview)).

This seems like a security nightmare, which is especially relevant because sensitive data is often stored in Excel files.

> **angadsg**: Hi, engineer on this add-in. Fair concern but we never train on any of our business or enterprise user data, or if you have opted-out of training on your ChatGPT account.

> > **Avicebron**: Forgive my ignorance. How do you folks manage context retention? Say if someone had a sensitive excel document they wanted inference done over, how is that data actually sent to the model and then stored or deleted?
> > 
> > It seems one of the biggest barriers to people's adoption is concern over data leaving their ecosystem and then not being protected or being retained in some way.
> > 
> > Is this is an SLA that a small or medium sized company could get?

> > > **p_ing**: If you're concerned, you don't send it outside of the M365 boundary and presumably your admin has Purview Sensitivity Labels in place covering the document to prevent such activity.

> > **Acmeon**: Yeah, I was expecting that you do not train on business or enterprise user data. However, I am not just worried about "training", but also about "sharing". Furthermore, I am worried about cases where an individual has chosen to integrate an add-in and then inadvertently leaks sensitive data.
> > 
> > However, it may be important to note that these security considerations are relevant for most Office Add-Ins (and not just the ChatGPT add-in).

> **p_ing**: That's the nature of these add-ins. Modern Add-ins are all little XML frames with some JS or whatever. All processing occurs server-side, hosted by the add-in publisher.
> 
> This is counter to the old (security nightmare) COM model where processing could be local.

> > **strongpigeon**: To clarify: add-ins are essentially web pages. They can do some processing client side if they want, but yeah in the case of a ChatGPT add-in it's not like they're running the model in a web frame.

---

### tills13

These AI in Excel products are a financial crisis waiting to happen. Or maybe just Enron but stupider.

---

### kbos87

From time to time I've tried using ChatGPT for financial modeling, and I have to say my experiences don't inspire much confidence.

Just this past week I used it to generate a simple model of a few different scenarios related to an investment property I own.

The first problem I ran into is that it was unable to output a downloadable XLS file. Not a huge deal - it suggested generating CSV tables I could copy/paste into a spreadsheet. The outputs it gave me included commas in a handful of numbers over 1,000 (but not all of them!) which of course shifted cells around when brought into Google Sheets. We pivoted our approach to TSV and solved this problem. Big deal? No. Seemingly basic oversight? Absolutely.

This is where the real fun began. Once I started to scrutinize and understand the model it built, I found incorrect references buried all over the place, some of which would have been extremely hard to spot. Here's my actual exchange with ChatGPT:

- - - - - - - - - -

> Can you check the reference in cell F3? It looks like it's calling back to the wrong cell on the inputs tab. Are there similarly incorrect references elsewhere?

> Yes, F3 is incorrect, and there are multiple other incorrect references elsewhere: (It listed about 30 bulleted incorrect references)

Bottom line - 
 - Many formulas point to the wrong Inputs row because of the blank lines
 - The Sell + Condo section also has a structural design problem, not just bad references.

The cleanest fix is for me to regenerate the entire AnnualModel TSV with:
 - all references corrected
 - all 15 years included
 - the condo scenario modeled properly with a separate housing asset column

- - - - - - - - - -

This was me asking about the exact output I had just received (not something I had made any changes to or reworked.)

There are plenty of domains where I have enough faith and error tolerance to use ChatGPT all day, but this just sends a chill down my spine. How many users are really going to proof every single formula? And if I need to scrutinize to that level of detail, what's the point in the first place?

---

### thih9

> Follow along so you can trust the work

> (…) you can verify each step and revert edits if needed.

I wish there were different workflows.

It feels like current most popular way of working with GenAI requires the operator to perform significant QA. The net time savings are usually positive. But it still feels inefficient, risky and frustrating, especially with more complex and/or niche problem areas.

Are there GenAI products that focus more on skill enhancement than replacement? Or any other workflows that improve reliability?

---

### linzhangrun

This should have been implemented when Microsoft launched Copilot two years ago. Instead, they’d rather hijack the right Ctrl on every computer than do this.

---

### gauravsc

I had built this [https://novasheets.com/](https://novasheets.com/) based on my experience building agentic enterprise automation for financial industry and works as well as chatgpt and perhaps better :)

---

### p_ing

Microsoft has this built-in using Claude models (for M365 Copilot licensed users). I don't know why you'd use this as an M365 subscriber in an enterprise. I'm sure there's some edge cases, but MSFT has been moving away from OAI. Even Copilot Studio agents now default to Sonnet 4.6 and not GPT 5.

> **strongpigeon**: > I'm sure there's some edge cases, but MSFT has been moving away from OAI.
> 
> You're not wrong, but you'd think that given their 27% stake in OpenAI they'd put more weight behind ChatGPT integration.

> > **ralph84**: MSFT also has a stake in Anthropic (although much less than 27%) and they host Anthropic models in Foundry now. The end game for MSFT has always been being the compute provider, so MSFT is just as happy to use any model as long as it's running in Foundry.

> > **p_ing**: Based on my discussion with DSEs, enterprises have not been impressed in the results of "Copilot", i.e. OAI models. MSFT has been replacing (or changing the default) to Claude across a variety of Copilot endpoints.

---
