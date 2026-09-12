# **UAF‑Open v0.1 — Minimal, Tool‑Neutral Architecture Repository**

UAF‑Open is a **tool‑neutral, ASCII‑stable reference architecture repository** for expressing, validating, and tracing enterprise architectures from **strategic intent** through **operational behavior** to **solution realization** and **actual deployed resources**.

The goal of v0.1 is simplicity: a **minimal but complete causal chain**, two **tiny examples**, and a **validator** that enforces architectural correctness.

---

## **Purpose**
UAF‑Open provides:

- A minimal **metamodel**  
- Typed **relations**  
- Small, readable **examples** (goat + digital service)  
- A machine‑checkable **causal closure**  
- Basic **validation rules**  
- Simple **Mermaid rendering** for diagrams  

It is **not** a full UAF 1.3 implementation.  
It is a **minimal, working subset** designed for clarity, portability, and correctness.

---

## **Core Principle: Causal Chain**
Every architecture model in this repository must satisfy:

```
Capability
→ OperationalActivity
→ Resource / Service (Realization)
→ ActualResource (Evidence)
```

This is enforced by the validator and expressed in the examples.

---

## **Repository Structure**
```
uaf-open/
├── README.md
├── metamodel/
│   ├── core.yaml
│   └── relations.yaml
├── examples/
│   ├── goat/
│   └── digital-service/
├── mappings/
│   └── causal-closure.yaml
├── validation/
│   └── rules.yaml
└── render/
    └── mermaid/
```

### **Metamodel**
Defines the minimal vocabulary:

- **Capability**  
- **OperationalActivity**  
- **Service**  
- **Resource**  
- **Constraint**  
- **Project**  
- **ActualResource**  

### **Relations**
Typed operators such as:

- **supports**  
- **realizes**  
- **instantiates**  
- **constrainedBy**  

### **Examples**
Two minimal end‑to‑end architectures:

- **Goat example**  
- **Digital service example**  

### **Mappings**
Causal closure rules that enforce architectural correctness.

### **Validation**
Rules that ensure:

- no dangling elements  
- typed relations  
- causal closure  
- constraints propagate  
- projects deliver realizations  

### **Render**
A minimal Mermaid renderer with type grouping.

---

## **How to Use**
1. Create a new model under `examples/`.  
2. Define elements in `elements.yaml`.  
3. Define relations in `relations.yaml`.  
4. Run the validator (external script or CI).  
5. Render diagrams using the Mermaid renderer.  

This produces a **portable, reviewable, tool‑neutral architecture**.

---

## **Design Principles**
- **ASCII‑stable**: no proprietary formats.  
- **Tool‑neutral**: SysML, UML, ArchiMate, C4 are adapters, not sources of truth.  
- **Causally complete**: every realization must justify itself.  
- **Minimal**: only the essential UAF concepts.  
- **Extensible**: Relationalism, formal methods, and adapters can be added later.

---

## **Status**
v0.1 is intentionally small.  
Future versions may add:

- RDG substrate  
- formal proofs  
- additional viewpoints  
- adapters for SysML‑v2, UML, ArchiMate  
- richer examples  

Future work: **Plan RDG for v0.2**
