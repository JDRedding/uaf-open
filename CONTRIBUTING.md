# **UAF‑Open CONTRIBUTING Guide (v0.1)**  
A minimal, tool‑neutral contribution guide for the UAF‑Open architecture repository.

---

## **Purpose**
This document explains how to:

- add new architecture examples  
- add new elements or relations  
- maintain ID stability  
- run validation and rendering  
- keep the repository consistent and ASCII‑stable  

UAF‑Open is intentionally minimal. Contributions must preserve this simplicity.

---

## **1. Repository Principles**
All contributions MUST follow these principles:

- **ASCII‑stable** (no proprietary formats)  
- **Tool‑neutral** (YAML is the source of truth)  
- **Causally complete** (CV → OV → SV → AR)  
- **ID‑stable** (IDs never change once created)  
- **Schema‑valid** (elements.yaml + relations.yaml must pass schemas)  
- **Validator‑clean** (no dangling elements, no broken relations)  

---

## **2. Adding a New Example**
Examples live under:

```
examples/<slug>/
```

Each example MUST contain:

```
elements.yaml
relations.yaml
README.md (optional but encouraged)
```

### Steps

1. Create a new directory:
   ```
   examples/<slug>/
   ```

2. Add `elements.yaml` with:
   - `id`
   - `type`
   - `name`
   - optional `description`

3. Add `relations.yaml` with:
   - `source`
   - `operator`
   - `target`
   - optional `evidence`

4. Run validation:
   ```
   make validate-<slug>
   ```

5. Generate Mermaid diagram:
   ```
   make <slug>
   ```

If validation fails, fix the model before submitting.

---

## **3. Adding Elements**
Elements MUST follow the schema:

- required fields: `id`, `type`, `name`
- type MUST be one of the allowed metamodel types
- ID MUST follow the ID contract

Example:

```yaml
- id: cap.reduce-case-resolution-time
  type: Capability
  name: Reduce case resolution time
```

---

## **4. Adding Relations**
Relations MUST follow the schema:

- required fields: `source`, `operator`, `target`
- operator MUST be one of the allowed operators
- source/target MUST exist in `elements.yaml`

Example:

```yaml
- source: op.manage-case
  operator: supports
  target: cap.reduce-case-resolution-time
```

---

## **5. Running Validation**
Validation ensures:

- no dangling elements  
- correct types  
- correct operators  
- causal closure  
- ID uniqueness  
- schema compliance  

Run:

```
make validate-goat
make validate-digital
make validate-<slug>
```

Or directly:

```
python validation/validator.py <elements.yaml> <relations.yaml>
```

---

## **6. Rendering Diagrams**
Renderers live under:

```
render/mermaid/
```

Use the single‑shot renderer:

```
make <slug>
```

Or directly:

```
python render/mermaid/render-ss.py <elements.yaml> <relations.yaml> <output.mmd>
```

---

## **7. ID Stability**
IDs MUST NOT change once created.

Allowed changes:

- update `name`
- update `description`
- update relations

NOT allowed:

- changing the ID  
- reusing an ID for a different meaning  
- adding nested namespaces  

If an element is replaced, create a new ID and deprecate the old one.

---

## **8. Metamodel Changes**
Changes to the metamodel MUST:

- be discussed in an issue  
- include a justification  
- include schema updates  
- include validator updates  
- include example updates  

Metamodel changes are rare and should be minimal.

---

## **9. Governance**
All contributions MUST follow:

- ID contract  
- schemas  
- validator rules  
- causal closure rules  

Breaking changes require a version bump (v0.2, v0.3, etc.).

---

## **10. Pull Request Requirements**
Every PR MUST include:

- passing validation  
- passing schema checks  
- updated diagrams  
- clear commit messages  
- no broken IDs  
- no dangling elements  

Optional but encouraged:

- updated README for the example  
- diagrams in `.mmd` format  

---

# **Summary**
This CONTRIBUTING guide ensures:

- consistency  
- stability  
- correctness  
- portability  
- causal completeness  
