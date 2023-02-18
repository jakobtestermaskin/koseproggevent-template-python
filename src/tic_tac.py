"""
Jobb i denne filen for å gjøre endringer på algoritmen så du slår de andre!!
"""

from move import Move
from game_sim import GameSim

# De fire verdiene en rute kan ha
EMPTY = " "
HORIZONTAL = "─"
VERTICAL = "│" 
FULL = "🞡"

def next_move(board: list[list[str]], legal_moves: list[Move], current_player: str, history: list[Move]) -> Move:
    """

    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    the entries in this list will map to the game board in the following way: 
    1 | 2 | 3
    ---------
    4 | 5 | 6
    ---------
    7 | 8 | 9

    Things to know:
    - moves always use the Move class: Move(x = x, y = y, player = "│" or "─")
    - board is mapped with board[y][x] so in the example above, board[0][2] = O, in the upper right corner

    legal_moves = [Move()...]
    history = [Move()...]

    if history is empty, first move is expected
    if legal_moves is empty, board is full and game is already finished (you don't need to take care of this state)
    """

    # You can use the provided game simulator to simulate future game states
    simulator = GameSim(board, current_player, history)

    # First available Move
    move = legal_moves[0]

    # move is of type Move(x = x, y = y, player = "│" or "─"), but we know we will be player "current_player"
    return Move(x=move.x, y=move.y, player=current_player)
