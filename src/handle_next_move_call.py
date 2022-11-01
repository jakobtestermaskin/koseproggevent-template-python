
import json
from move import Move
import tic_tac


def handle_next_move(board, legal_moves, current_player, history):

    if len(legal_moves) > 0:
        try:
            move = tic_tac.next_move(
                board, legal_moves, current_player, history)
            return {"move": move.serialize()}
        except:
            return {"error": "Applicaiton catched an error"}

    else:
        return {
            "error": "Did not find any legal moves"
        }
