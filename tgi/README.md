# Topological General Intelligence (TGI) v1.1
### The Algebraic & Symbolic Mind

TGI is a cognitive architecture built on the **Fiber-Stratified Optimization (FSO)** framework. It replaces probabilistic, high-power-consumption neural weights with exact topological invariants and $O(1)$ hardware-native algebraic logic.

## Core Components
- **Cognitive Manifold (`core.py`):** Represents knowledge as a multi-dimensional torus. Uses Short Exact Sequences (SES) to reduce complex problems into solvable base spaces.
- **Inference Engine (`deduction.py`):** Performs O(1) logical jumps using the **Universal Spike Function**. No neural search required. Supports parity-aligned $k=2, 4$ and $k=3$ odd manifolds.
- **Truth Oracle (`verification.py`):** Verifies the mathematical truth of a logical chain. Uses **H^2 Parity Obstructions** to detect internal contradictions (paradoxes) and reports coverage of the state space.
- **Symbolic Mapper (`mind.py`):** Translates symbolic concepts (e.g., "Ethics", "Liar Paradox") into manifold coordinates.

## Key Concepts
1. **O(1) Deduction:** Complex logical chains are traversed at the speed of logic gates.
2. **Topological Truth:** A hypothesis is "True" if its reasoning chain closes a Hamiltonian cycle on the manifold.
3. **Parity Harmony:** A fundamental requirement for logical consistency in even manifolds. Even $m$ requires even $k$.

## Usage
```python
from tgi.mind import TopologicalGeneralIntelligence

# Initialize TGI for a 3x3x3 cognitive space
mind = TopologicalGeneralIntelligence(m=3, k=3)

# Map symbolic concepts to coordinates
mind.mapper.map_concept("Universal Ethics", (0, 0, 0))

# Process a hypothesis from a symbolic premise
result = mind.process_hypothesis("Universal Ethics")
print(result['report']['status']) # ABSOLUTE_TRUTH
```
