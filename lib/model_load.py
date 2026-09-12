import yaml
from collections import defaultdict

class Model:
    def __init__(self, elements_path, relations_path):
        self.elements = self._load_yaml(elements_path).get("elements", [])
        self.relations = self._load_yaml(relations_path).get("relations", [])

        # Indexes
        self.by_id = {e["id"]: e for e in self.elements}
        self.by_type = defaultdict(list)
        for e in self.elements:
            self.by_type[e["type"]].append(e)

        # Relation indexes
        self.outgoing = defaultdict(list)
        self.incoming = defaultdict(list)
        for r in self.relations:
            self.outgoing[r["source"]].append(r)
            self.incoming[r["target"]].append(r)

    def _load_yaml(self, path):
        with open(path, "r") as f:
            return yaml.safe_load(f)

    # Convenience helpers
    def get(self, element_id):
        return self.by_id.get(element_id)

    def get_type(self, type_name):
        return self.by_type.get(type_name, [])

    def get_outgoing(self, element_id):
        return self.outgoing.get(element_id, [])

    def get_incoming(self, element_id):
        return self.incoming.get(element_id, [])

    def get_targets(self, element_id, operator=None):
        """Return all targets of outgoing relations, optionally filtered by operator."""
        results = []
        for r in self.get_outgoing(element_id):
            if operator is None or r["operator"] == operator:
                results.append(self.by_id.get(r["target"]))
        return results

    def get_sources(self, element_id, operator=None):
        """Return all sources of incoming relations, optionally filtered by operator."""
        results = []
        for r in self.get_incoming(element_id):
            if operator is None or r["operator"] == operator:
                results.append(self.by_id.get(r["source"]))
        return results
