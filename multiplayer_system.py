```python
import crdt
from utils import get_current_time

class MultiplayerSystem:
    def __init__(self):
        self.players = {}
        self.crdt = crdt.CRDT()

    def add_player(self, player_id, player_info):
        self.players[player_id] = player_info

    def remove_player(self, player_id):
        if player_id in self.players:
            del self.players[player_id]

    def update_player_info(self, player_id, player_info):
        if player_id in self.players:
            self.players[player_id] = player_info

    def get_player_info(self, player_id):
        return self.players.get(player_id, None)

    def apply_operation(self, operation):
        timestamp = get_current_time()
        self.crdt.apply_operation(operation, timestamp)

    def get_state(self):
        return self.crdt.get_state()
```