from flask import Flask, request
from flask_cors import CORS
import sys
import json

sys.path.append("../src")

# Must be imported after module have been appended
from move import Move
import tic_tac


api = Flask(__name__)
CORS(api)


@api.route("/", methods=["POST"])
def handleTicTac():

    board = request.json['board']
    _legal_moves = request.json['legalMoves']

    if (len(_legal_moves) != 0):

        legal_moves = [Move(x=it['x'], y=it['y'], player=it['player'])
                    for it in _legal_moves]

        current_player = request.json['currentPlayer']
        history = request.json['history']

        return json.dumps({"move": tic_tac.next_move(board, legal_moves, current_player, history).serialize()})
    else:
        return json.dumps({"error": "Did not find any legal moves"})


if __name__ == '__main__':
    api.run()
