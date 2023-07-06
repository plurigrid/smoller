```python
import chyp
import hypergraphx as hx
from hypergraph_environment import HypergraphEnvironment

class DiagramGenerator:
    def __init__(self, environment):
        self.environment = environment

    def generate_diagram(self):
        hypergraph = self.environment.get_hypergraph()
        diagram = chyp.Diagram(hypergraph)
        return diagram

    def display_diagram(self, diagram):
        diagram.show()

if __name__ == "__main__":
    environment = HypergraphEnvironment()
    generator = DiagramGenerator(environment)
    diagram = generator.generate_diagram()
    generator.display_diagram(diagram)
```