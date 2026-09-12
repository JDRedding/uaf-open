# **UAF‑Open ID Contract (v0.1)**  
**Purpose:** Ensure every element in the architecture has a stable, portable, machine‑friendly identifier.

---

## **1. ID Format**
Every ID MUST follow this exact pattern:

```
<type>.<slug>
```

Where:

- **type** = one of the metamodel types  
  (Capability, OperationalActivity, Resource, Service, Constraint, Project, ActualResource, etc.)
- **slug** = lowercase, hyphen‑separated, ASCII‑only semantic name

### Examples
```
cap.reduce-case-resolution-time
op.manage-case
res.api-container
svc.case-management-api
con.data-retention-7y
proj.case-system-modernization
ar.api-container-prod-1
```

---

## **2. Allowed Characters**
The slug may contain ONLY:

- `a–z`  
- `0–9`  
- `-` (hyphen)

No underscores.  
No spaces.  
No uppercase.  
No special characters.

This ensures portability across:

- Mermaid  
- JSON  
- YAML  
- file systems  
- URLs  
- RDG operators  
- future SysML‑v2 adapters

---

## **3. Stability Rules**
IDs MUST be **stable across time**.

You may NOT change an ID unless:

- the element’s meaning changes  
- the element is deleted  
- the element is split into multiple new elements  
- the element is merged into another element  

Otherwise, IDs persist forever.

This ensures:

- diffs remain meaningful  
- diagrams remain stable  
- validation remains consistent  
- references never break

---

## **4. Versioning**
IDs do **not** contain version numbers.

Versioning is handled at the **model level**, not the ID level.

If a capability evolves, you update its **name**, **description**, or **relations**, but **not its ID**.

If a capability is replaced, you create a new ID:

```
cap.new-incident-response
```

And deprecate the old one.

---

## **5. Names vs IDs**
The **name** field is human‑readable.  
The **ID** field is machine‑readable.

Names may change.  
IDs may not.

Example:

```
id: cap.reduce-case-resolution-time
name: Reduce case resolution time
```

If the name changes:

```
name: Improve case throughput
```

The ID stays the same.

---

## **6. Uniqueness**
All IDs MUST be globally unique across the entire repository.

The validator enforces this.

---

## **7. Namespace Rules**
The `<type>` prefix is the namespace.

You may NOT create nested namespaces:

❌ `cap.gov.reduce-case-time`  
❌ `op.case.manage.lifecycle`  

Only one level:

✔ `cap.reduce-case-resolution-time`  
✔ `op.manage-case`

This keeps IDs short and diff‑friendly.

---

## **8. Lifecycle Rules**
When deleting an element:

- remove its ID from the model  
- remove all relations referencing it  
- do NOT reuse the ID for a different meaning

When splitting an element:

- create new IDs  
- deprecate the old one  
- do not reuse the old ID

When merging elements:

- pick one ID to keep  
- deprecate the others

---

## **9. File Naming**
Example directories MUST use the same slug as the primary capability or system.

Example:

```
examples/goat/
examples/digital-service/
```

