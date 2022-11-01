
import tic_tac
import traceback


def handle_next_move(board, legal_moves, current_player, history):

    if len(legal_moves) > 0:
        try:
            move = tic_tac.next_move(
                board, legal_moves, current_player, history)

            return {"move": move.serialize()}
        except Exception as e:

            exception_trace = traceback.format_exc()

            print("Caught exception: %s" % exception_trace)

            return {"error": "Applicaiton catched an error", "stackTrace": exception_trace}

    else:
        return {
            "error": "Did not find any legal moves",
            "stackTrace": None
        }
