# Minimal UAF-Open Makefile (v0.1)

PYTHON = python3

# Paths
GOAT_E = examples/goat/elements.yaml
GOAT_R = examples/goat/relations.yaml
GOAT_M = examples/goat/goat.mmd

DIG_E = examples/digital-service/elements.yaml
DIG_R = examples/digital-service/relations.yaml
DIG_M = examples/digital-service/service.mmd

# Renderers
RENDER_MIN = render/mermaid/render-minimal.py
RENDER_SS  = render/mermaid/render-ss.py
VALIDATOR  = validation/validator.py

# Default target
all: goat digital

# Goat example
goat:
    $(PYTHON) $(RENDER_SS) $(GOAT_E) $(GOAT_R) $(GOAT_M)
    @echo "Generated goat.mmd"

validate-goat:
    $(PYTHON) $(VALIDATOR) $(GOAT_E) $(GOAT_R)

# Digital service example
digital:
    $(PYTHON) $(RENDER_SS) $(DIG_E) $(DIG_R) $(DIG_M)
    @echo "Generated service.mmd"

validate-digital:
    $(PYTHON) $(VALIDATOR) $(DIG_E) $(DIG_R)

# Clean generated diagrams
clean:
    rm -f $(GOAT_M) $(DIG_M)
    @echo "Cleaned generated Mermaid files"
