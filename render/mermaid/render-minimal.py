import yaml
import sys

def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def render_mermaid(elements, relations):
    print("graph TD")

    # Nodes
    for e in elements["elements"]:
        print(f'    {e["id"]}["{e["name"]}\\n({e["type"]})"]')

    # Edges
    for r in relations["relations"]:
        src = r["source"]
        tgt = r["target"]
        op  = r["operator"]
        print(f"    {src} -- {op} --> {tgt}")

if __name__ == "__main__":
    elements = load_yaml(sys.argv[1])
    relations = load_yaml(sys.argv[2])
    render_mermaid(elements, relations)
