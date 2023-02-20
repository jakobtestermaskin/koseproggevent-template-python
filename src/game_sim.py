from move import Move

EMPTY = " "
HORIZONTAL = "-"
VERTICAL = "|" 
FULL = "+"

class GameSim:
    def __init__(self, board: list[list[str]], current_player: str, history: list[Move]):
        self.board = board
        self.history: list[Move] = history
        self.current_player: str = current_player

    @classmethod
    def create_empty(cls, current_player: str):
        """Create a new GameSim with an empty board and history. This is the same as starting a new game.

        Args:
            current_player (str): "|" or "-"

        Returns:
            GameSim: The GameSim
        """
        return cls([[" " for y in range(3)]for x in range(3)], current_player, [])
     
    def do_move(self, move: Move):
        """Does a move, modifying the state of the simulator

        Args:
            move (Move): The move to do
        """
        prev_value = self.board[move.x][move.y]
        if prev_value != self.current_player and prev_value != " ":
            self.board[move.x][move.y] = FULL
        else:
            self.board[move.x][move.y]

        self.current_player = VERTICAL if self.current_player == HORIZONTAL else HORIZONTAL
        self.history.append(move)

    def get_cell(self, x:int, y:int) -> str:
        """Get the value of the cell at the given position.

        Args:
            x (int): x coordinate, left to right
            y (int): y coordinate, top to bottom

        Returns:
            str (" ", "|", "-" or "+"): The value of the cell
        """
        return self.board[x][y]

    def get_winner(self):
        """Get the winner of the board, or None if no winner.

        Returns:
            (str | None): The winner
        """
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

    def move_is_legal(self, move: Move) -> bool:
        """Check if a move is legal in the current state

        Args:
            move (Move): The move to check

        Returns:
            bool: True if the move is legal
        """
        if self.get_winner() != None:
            return False
        old_value = self.get_cell(move.x, move.y)
        already_placed = old_value == FULL or old_value == move.player
        last_move = self.history[-1]
        placed_last_move = last_move.x == move.x and last_move.y == move.y
        return not already_placed and not placed_last_move

    def get_legal_moves(self) -> list[Move]:
        """Get a list of all the legal moves in the current state

        Returns:
            list[Move]: A list of the legal moves
        """
        all_moves = [Move(i % 3, i // 3, self.current_player) for i in range(9)]
        return list(filter(self.move_is_legal, all_moves))