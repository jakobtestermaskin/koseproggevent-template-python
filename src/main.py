
from move import Move
import tic_tac

def handler(event, context):
    
    body = event['body']
    response = {}
    if (len(legal_moves) != 0):

        board = body['board']

        legal_moves = [Move(x=it['x'], y=it['y'], player=it['player'])
                    for it in body['legalMoves']]

        current_player = body['currentPlayer']
        history = body['history']

        try: 
            move = tic_tac.next_move(board, legal_moves, current_player, history)
            response = {"move": move.serialize()}
        except:
            reponse = {"error": "Applicaiton catched an error"}

    else:
        response = {
            "error": "Did not find any legal moves"
        }

    return {"statusCode": 200, "body": response}