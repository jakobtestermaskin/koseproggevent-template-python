from flask import Flask, request
from flask_cors import CORS
import sys

sys.path.append("../src")

# Must be imported after module have been appended
from config import get_config
from move import Move
from handle_next_move_call import handle_next_move

api = Flask(__name__)
CORS(api)


@api.route("/", methods=["POST"])
def handleTicTac():
    board = request.json['board']
    legal_moves = [Move(x=it['x'], y=it['y'], player=it['player'])
                   for it in request.json['legalMoves']]

    current_player = request.json['currentPlayer']
    history = request.json['history']
    return handle_next_move(board, legal_moves, current_player, history)


@api.route("/", methods=["GET"])
def handleConfig():
    return get_config()


if __name__ == '__main__':
    api.run(host="localhost", port=8000)
