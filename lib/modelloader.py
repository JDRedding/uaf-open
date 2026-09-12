import yaml
import sys
from lib.model import Model

def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def fail(msg):
    return {"ok": False, "error": msg}

def pass_():
    return {"ok": True}

def validate_no_dangling(model):
    for e in model.elements:
        if not model.get_incoming(e["id"]) and not model.get_outgoing(e["id"]):
            return fail(f"Dangling element: {e['id']} ({e['type']})")
    return pass_()

def validate_unique_ids(model):
    seen = set()
    for e in model.elements:
        if e["id"] in seen:
            return fail(f"Duplicate ID: {e['id']}")
        seen.add(e["id"])
    return pass_()

def validate_causal_closure(model, closure_rules):
    for rule in closure_rules["causal_closure"]:
        applies_to = rule["applies_to"]

        for e in model.elements:
            if e["type"] not in applies_to:
                continue

            # must_exist rule
            if "must_exist" in rule:
                rel = rule["must_exist"]["relation"]
                target_type = rule["must_exist"]["target_type"]

                targets = model.get_targets(e["id"], operator=rel)
                if not targets:
                    return fail(f"{rule['id']}: {e['id']} missing required relation '{rel}'")
                if isinstance(target_type, list):
                    if not any(t["type"] in target_type for t in targets):
                        return fail(f"{rule['id']}: {e['id']} has wrong target type for '{rel}'")
                else:
                    if not any(t["type"] == target_type for t in targets):
                        return fail(f"{rule['id']}: {e['id']} must relate to {target_type}")

            # must_exist_one_of rule
            if "must_exist_one_of" in rule:
                satisfied = False
                for cond in rule["must_exist_one_of"]:
                    rel = cond["relation"]
                    target_type = cond["target_type"]
                    targets = model.get_targets(e["id"], operator=rel)
                    if any(t["type"] == target_type for t in targets):
                        satisfied = True
                if not satisfied:
                    return fail(f"{rule['id']}: {e['id']} missing one-of required relations")

            # forbidden_if_only rule
            if "forbidden_if_only" in rule:
                op = rule["forbidden_if_only"]["operator"]
                outgoing = model.get_outgoing(e["id"])
                if outgoing and all(r["operator"] == op for r in outgoing):
                    return fail(f"{rule['id']}: {e['id']} only uses forbidden operator '{op}'")

    return pass_()

def run_validator(elements_path, relations_path):
    model = Model(elements_path, relations_path)
    rules = load_yaml("validation/rules.yaml")
    closure = load_yaml("mappings/causal-closure.yaml")

    checks = [
        ("Unique IDs", validate_unique_ids(model)),
        ("No dangling elements", validate_no_dangling(model)),
        ("Causal closure", validate_causal_closure(model, closure)),
    ]

    print("Validation Report:")
    print("------------------")

    all_ok = True
    for name, result in checks:
        if result["ok"]:
            print(f"[OK] {name}")
        else:
            print(f"[FAIL] {name}: {result['error']}")
            all_ok = False

    if all_ok:
        print("\nModel is VALID.")
    else:
        print("\nModel is INVALID.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python validator.py <elements.yaml> <relations.yaml>")
        sys.exit(1)

    run_validator(sys.argv[1], sys.argv[2])
