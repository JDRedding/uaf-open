## 🔧 How to run it
From the repo root:

```
python render/mermaid/render.py examples/goat/elements.yaml examples/goat/relations.yaml > goat.mmd
```

This produces a Mermaid diagram like:

```
graph TD
    cap.protect-garden["Protect garden productivity\n(Capability)"]
    op.prevent-goat-entry["Prevent goat entry into garden\n(OperationalActivity)"]
    perf.gardener["Gardener\n(OperationalPerformer)"]
    ex.goat-detection["Goat detection alert\n(Exchange)"]
    res.fence["Perimeter fence\n(Resource)"]
    svc.boundary-protection["Boundary protection service\n(Service)"]
    con.boundary-strength["Boundary must resist ordinary goat access\n(Constraint)"]
    ar.fence-west-plot["West plot fence installation\n(ActualResource)"]

    op.prevent-goat-entry -- supports --> cap.protect-garden
    op.prevent-goat-entry -- performedBy --> perf.gardener
    perf.gardener -- exchanges --> perf.gardener
    res.fence -- provides --> svc.boundary-protection
    svc.boundary-protection -- realizes --> op.prevent-goat-entry
    res.fence -- constrainedBy --> con.boundary-strength
    ar.fence-west-plot -- instantiates --> res.fence
```
---

## 🔷 Why this renderer is “minimal but real”
- **ASCII‑stable**  
- **Tool‑neutral**  
- **No vendor lock‑in**  
- **Works with any YAML model**  
- **Supports causal closure visualization**  
- **Easy to extend** (colors, shapes, grouping, subgraphs)  

It’s the smallest renderer that still behaves like a real architecture visualization pipeline.

---

