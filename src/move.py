"""
Her kan du gjøre endringer, men det er ikke anbefalt
"""


class Move:
    def __init__(self, x:int, y:int, player:str):
        self.x = x
        self.y = y
        self.player = player

    def serialize(self):
        return {
            "x": self.x,
            "y": self.y,
        }

    def __repr__(self) -> str:
        return f"Move(x={self.x} y={self.y} player={self.player})"
