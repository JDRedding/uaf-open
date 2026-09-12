import yaml
import sys
from collections import defaultdict

def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

# Map UAF types to causal layers
LAYER_MAP = {
    "Capability": "CV",
    "OperationalActivity": "OV",
    "OperationalPerformer": "OV",
    "Exchange": "OV",
    "Constraint": "OV",
    "Service": "SV",
    "Resource": "SV",
    "Project": "SV",
    "ActualResource": "AR",
}

def render_mermaid(elements, relations):
    print("graph TD")

    # Group elements by causal layer
    layers = defaultdict(list)
    for e in elements["elements"]:
        layer = LAYER_MAP.get(e["type"], "OTHER")
        layers[layer].append(e)

    # Render super-subgraphs (CV, OV, SV, AR)
    for layer, items in layers.items():
        print(f"    subgraph {layer}")
        # Within each layer, group by type
        type_groups = defaultdict(list)
        for e in items:
            type_groups[e["type"]].append(e)

        for t, group_items in type_groups.items():
            print(f"        subgraph {t}")
            for e in group_items:
                print(f'            {e["id"]}["{e["name"]}\\n({e["type"]})"]')
            print("        end")
        print("    end")

    # Render edges
    for r in relations["relations"]:
        src = r["source"]
        tgt = r["target"]
        op  = r["operator"]
        print(f"    {src} -- {op} --> {tgt}")

if __name__ == "__main__":
    elements = load_yaml(sys.argv[1])
    relations = load_yaml(sys.argv[2])
    render_mermaid(elements, relations)
