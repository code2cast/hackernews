# Moving a large-scale metrics pipeline from StatsD to OpenTelemetry / Prometheus

- **Link**: https://medium.com/airbnb-engineering/building-a-high-volume-metrics-pipeline-with-opentelemetry-and-vmagent-c714d6910b45
- **HN**: https://news.ycombinator.com/item?id=47788818
- **Score**: 53 points
- **By**: jmarbach
- **Date**: 2026-04-16 05:01 UTC
- **Comments**: 11

---

Full disclosure - I formerly worked for Grafana Labs.

The size of this Grafana Mimir deployment would rank it in the top echelon of customers. The irony is that this may be a $0 revenue user for Grafana Labs.

---

## Comments

### dig1

> The irony is that this may be a $0 revenue user for Grafana Labs.

Why is that ironic? Since Mimir is open-source, $0 revenue users are expected. AFAIK, Grafana Labs relies heavily on go, typescript, and linux, without necessarily being their top financial contributor. They could have kept Mimir proprietary like Splunk, but whether that would have attracted the same level of adoption or community contribution is another matter.

---

### codeduck

> given Prometheus’s widespread adoption and proven reliability in diverse environments.

I have used Prometheus a lot.  Reliable is not a word I would associate with it.

> **pahae**: I set up a fairly large Prom-based architecture which I later on migrated to VictoriaMetrics (VM) so I think I can chime in here.
> 
> Both Prom and VM are exceptionally stable in my opinion, even on _very_ large scales. There were times when I had a single (Prom, later VM) and not-overly-large instances scrape 2Mio samples/s without any issues. In addition to fairly spiky query loads.
> 
> However, *if* something does go wrong, the single most impactful difference between VM and Prom is simply the difference in startup time. Prometheus with 2TB of metrics takes _forever_ to start up. We're talking up to 2 hours on SSD while VM just... starts.

> > **porridgeraisin**: Yeah, at previous work we used both as well. The transition from prom to vm was "ongoing" and from the time I joined to the time I left we did parallel writes to both. Never faced issues with either. If I remember correctly, we wrote from services to a kafka queue first, and then a consumer took that and pushed it to (both) the metrics endpoint(s).

> **hagen1778**: What do you use instead of Prometheus?

> > **codeduck**: Given a choice, VictoriaMetrics.  It has proven itself time and time again at scale, and requires a very low support investment.

---

### blueybingo

the zero injection fix for sparse counters is the most underrated part of this writeup -- injecting a synthetic zero on first flush to anchor the cumulative baseline is actaully a pretty elegant solution to a problem that bites almost every team migrating from delta-based systems to prometheus, and the fact that they centralized it in the aggregation tier rather than pushing the fix to every instrumentation callsite is exactly the right call.

---

### jameson

Curious why the team choose Grafana Mirmir over VM cluster?

> **esafak**: How are these substitutes? Mimir is a time series database.

---

### zbentley

> Initially, we anticipated that the edge case would have minimal impact, given Prometheus’s widespread adoption and proven reliability in diverse environments. However, as we migrated more users, we started seeing this issue more frequently, and it stalled migration.

That's a very professional way of saying "Wait, everyone just lives with this? What the fuck?!"

Many such cases in the Prometheus ecosystem.

---

### awoimbee

Directly emitting metrics using OTLP instead of having the OTel receiver scrape the metrics endpoint is interesting.
I never made that move because the Prometheus metrics endpoint works and is so simple, and it's what most projects (eg kubernetes) use.

---
