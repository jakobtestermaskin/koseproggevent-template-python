from move import Move


def next_move(board, legal_moves, current_player, history):

    # First available Move
    move = legal_moves[0]

    # move is of type Move (x: int, y: int, player: "X|Y"), but we know we will be player "current_player"
    return Move(x=move.x, y=move.y, player=current_player)
