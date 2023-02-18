from move import Move

EMPTY = " "
HORIZONTAL = "─"
VERTICAL = "│" 
FULL = "🞡"

class GameSim:
    def __init__(self, board: list[list[str]], current_player: str):
        self.board = board
        self.history: list[Move] = []
        self.current_player: str = current_player

    @classmethod
    def create_empty(cls, current_player: str):
        return cls([[" " for y in range(3)]for x in range(3)], current_player)
     
    def do_move(self, move: Move):
        prev_value = self.board[move.x][move.y]
        if prev_value != self.current_player and prev_value != " ":
            self.board[move.x][move.y] = FULL
        else:
            self.board[move.x][move.y]

        self.current_player = VERTICAL if self.current_player == HORIZONTAL else HORIZONTAL
        self.history.append(move)

    def get_cell(self, x:int, y:int):
        return self.board[x][y]

    def get_winner(self):
        winning_combinations = [
            [
                [0, 0],
                [0, 1],
                [0, 2],
            ],
            [
                [1, 0],
                [1, 1],
                [1, 2],
            ],
            [
                [2, 0],
                [2, 1],
                [2, 2],
            ],
            [
                [0, 0],
                [1, 0],
                [2, 0],
            ],
            [
                [0, 1],
                [1, 1],
                [2, 1],
            ],
            [
                [0, 2],
                [1, 2],
                [2, 2],
            ],
            [
                [0, 0],
                [1, 1],
                [2, 2],
            ],
            [
                [0, 2],
                [1, 1],
                [2, 0],
            ],
        ];
        for combination in winning_combinations:
            [a,b,c] = combination
            if self.board[a[0]][a[1]] == FULL and self.board[a[0]][a[1]] == self.board[b[0]][b[1]] and self.board[a[0]][a[1]] == self.board[c[0]][c[1]]:
                return self.history[-1].player
            return " " 

    def move_is_legal(self, move: Move):
        old_value = self.get_cell(move.x, move.y)
        already_placed = old_value == FULL or old_value == move.player
        last_move = self.history[-1]
        placed_last_move = last_move.x == move.x and last_move.y == move.y
        return not already_placed and not placed_last_move

    def get_legal_moves(self):
        all_moves = [Move(i % 3, i // 3, self.current_player) for i in range(9)]
        return list(filter(self.move_is_legal, all_moves))