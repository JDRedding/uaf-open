# **UAF‑Open Roadmap (v0.1 → v0.5)**  
A minimal, tool‑neutral evolution plan for the UAF‑Open architecture repository.

## **Summary**

- **v0.1** — Minimal UAF‑Open (complete)  
- **v0.2** — Relational substrate  
- **v0.3** — Formal methods  
- **v0.4** — SysML‑v2 / UML / ArchiMate adapters  
- **v0.5** — Full UAF grid

## **Roadmap Philosophy**  
UAF‑Open evolves according to three principles:

1. **Minimal first**  
   Every version adds the smallest possible feature set.

2. **ASCII‑stable**  
   No proprietary formats. Everything must be diff‑friendly.

3. **Causally complete**  
   Every new feature must preserve the CV → OV → SV → AR chain.

---


## **v0.1 — Minimal Working Subset (COMPLETE)**  
The goals of v0.1 are already achieved:

- Minimal metamodel  
- Minimal relations  
- Two complete examples  
- Causal‑closure rules  
- Validation rules  
- Mermaid renderers  
- Model loader  
- Makefile  
- Schemas  
- Governance + ID contract  

v0.1 establishes the **canonical architecture substrate**.

---

## **v0.2 — Relational Substrate Integration**  
Introduce the first layer of **Relationalism** into UAF‑Open.

### Goals
- Add Relational triads as optional overlays  
- Add Relational‑compatible notation for relations  
- Add Relational operator mapping (ASCII‑stable)  
- Add Relational causal‑flow examples  
- Add Relational validation rules (minimal)  

### Deliverables
- `Relational/` directory  
- Relational crosswalk  
- Relational example model  
- Relational‑aware Mermaid renderer  

---

## **v0.3 — Formal Methods Layer**  
Introduce minimal formal verification concepts.

### Goals
- Add simple invariants (e.g., “every capability must be realized”)  
- Add optional constraint logic (non‑boolean, graded truth)  
- Add minimal proof sketches (ASCII‑stable)  
- Add validator extensions for invariants  

### Deliverables
- `formal/` directory  
- Invariant definitions  
- Constraint logic examples  
- Extended validator  

---

## **v0.4 — SysML‑v2 / UML / ArchiMate Adapters**  
Introduce adapters that map UAF‑Open models into external modeling ecosystems.

### Goals
- SysML‑v2 export (minimal subset)  
- UML class diagram export (types + relations)  
- ArchiMate mapping (Capability, Service, Resource)  
- Adapter scripts (ASCII‑stable, YAML‑in → YAML‑out)  

### Deliverables
- `adapters/sysml-v2/`  
- `adapters/uml/`  
- `adapters/archimate/`  
- Mapping documentation  

---

## **v0.5 — Full UAF Grid (Minimal Implementation)**  
Introduce the full UAF grid structure while keeping the repo minimal.

### Goals
- Add UAF domains (Strategy, Operational, Services, Resources, Personnel, etc.)  
- Add minimal viewpoint definitions  
- Add grid‑aware Mermaid renderer  
- Add grid validation rules  

### Deliverables
- `uaf-grid/` directory  
- Domain definitions  
- Viewpoint definitions  
- Grid renderer  
- Grid validator  

---

## **Long‑Term Vision (Post‑v0.5)**  
These are optional future expansions:

- Multi‑model composition  
- Multi‑domain federation  
- Relational‑powered simulation  
- Formal proofs of causal closure  
- SysML‑v2 round‑trip support  
- Architecture diffing + change tracking  
- UAF‑Open → Digital Engineering pipeline  

---

