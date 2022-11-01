
import json
from handle_next_move_call import handle_next_move

from move import Move
import tic_tac


def get_attributes(eventBodyString):
    body = json.loads(eventBodyString)
    board = body['board']

    legal_moves = [Move(x=it['x'], y=it['y'], player=it['player'])
                   for it in body['legalMoves']]

    current_player = body['currentPlayer']
    history = body['history']
    return (board, legal_moves, current_player, history)


def handler(event, context):

    http = event['requestContext']['http']
    method = http['method']
    print("Received event with method: %s" % method)

    if (method == "POST"):  # then we want to find out what is next move
        try:
            (board, legal_moves, current_player,
             history) = get_attributes(event['body'])

            response = handle_next_move(
                board, legal_moves, current_player, history)

            return {"statusCode": 200, "body": json.dumps(response)}
        except:
            return {"statusCode": 500, "body": json.dumps({"error": "Seems to be error with setup."})}
