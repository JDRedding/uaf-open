import yaml
import sys
from collections import defaultdict

def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def render_mermaid(elements, relations):
    print("graph TD")

    # Group elements by type
    groups = defaultdict(list)
    for e in elements["elements"]:
        groups[e["type"]].append(e)

    # Render subgraphs by type
    for t, items in groups.items():
        print(f"    subgraph {t}")
        for e in items:
            print(f'        {e["id"]}["{e["name"]}\\n({e["type"]})"]')
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
