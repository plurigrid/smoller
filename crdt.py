```python
class CRDT:
    def __init__(self):
        self.state = {}

    def add(self, element):
        if element not in self.state:
            self.state[element] = 1
        else:
            self.state[element] += 1

    def remove(self, element):
        if element in self.state:
            self.state[element] -= 1
            if self.state[element] == 0:
                del self.state[element]

    def query(self, element):
        return self.state.get(element, 0)

    def compare(self, crdt):
        for key, value in self.state.items():
            if crdt.query(key) != value:
                return False
        return True

    def merge(self, crdt):
        for key, value in crdt.state.items():
            if key not in self.state or self.state[key] < value:
                self.state[key] = value
```