class Move:
    def __init__(self, x, y, player):
        self.x = x
        self.y = y
        self.player = player

    def serialize(self):
        return {
            "x": self.x,
            "y": self.y,
            "player": self.player
        }