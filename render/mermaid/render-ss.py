import yaml
import sys
import os

def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def render_mermaid(elements, relations):
    lines = []
    lines.append("graph TD")

    # Nodes
    for e in elements["elements"]:
        lines.append(f'    {e["id"]}["{e["name"]}\\n({e["type"]})"]')

    # Edges
    for r in relations["relations"]:
        src = r["source"]
        tgt = r["target"]
        op  = r["operator"]
        lines.append(f"    {src} -- {op} --> {tgt}")

    return "\n".join(lines)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python render-ss.py <elements.yaml> <relations.yaml> <output.mmd>")
        sys.exit(1)

    elements_path = sys.argv[1]
    relations_path = sys.argv[2]
    output_path   = sys.argv[3]

    elements = load_yaml(elements_path)
    relations = load_yaml(relations_path)

    mermaid_text = render_mermaid(elements, relations)

    with open(output_path, "w") as f:
        f.write(mermaid_text)

    print(f"Generated Mermaid diagram: {output_path}")
