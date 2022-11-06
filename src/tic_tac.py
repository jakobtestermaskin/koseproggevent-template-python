"""
Jobb i denne filen for å gjøre endringer på algoritmen så du slår de andre!!
"""


from move import Move


def next_move(board, legal_moves, current_player, history):
    """
    Examples:
    board = [[" ", "X", "O"], ["O", "X", " "], [" ", "X", " "]]
    this board will look like: 
      | X | O
    ---------
    O | X | 
    ---------
      | X |  

    Things to know:
    - moves are always the Move class: Move(x = x, y = y, player = "X|Y")
     -board is mapped with board[x][y] so in the example above, board[0][2] = O, in the upper right corner

    legal_moves = [Move()...]
    history = [Move()...]

    if history is empty, first move is expected
    if legal_moves is empty, board is full and game is already finished (you don't need to take care of this state)
    """

    # First available Move
    move = legal_moves[0]

    # move is of type Move (x: int, y: int, player: "X|Y"), but we know we will be player "current_player"
    return Move(x=move.x, y=move.y, player=current_player)
