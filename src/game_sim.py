from move import Move

EMPTY = " "
HORIZONTAL = "─"
VERTICAL = "│" 
FULL = "🞡"

class GameSim:
    def __init__(self, board: list[list[str]], currentPlayer: str):
        self.board = board
        self.history: list[Move] = []
        self.currentPlayer: str = currentPlayer

    @classmethod
    def createEmpty(cls, currentPlayer):
        return cls([[" " for y in range(3)]for x in range(3)], currentPlayer)
     
    def doMove(self, move: Move):
        prevValue = self.board[move.x][move.y]
        if prevValue != self.currentPlayer and prevValue != " ":
            self.board[move.x][move.y] = FULL
        else:
            self.board[move.x][move.y]

        self.currentPlayer = VERTICAL if self.currentPlayer == HORIZONTAL else HORIZONTAL
        self.history.append(move)

    def getCell(self, x:int, y:int):
        return self.board[x][y]

    def getWinner(self):
        winningCombinations = [
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
        for combination in winningCombinations:
            [a,b,c] = combination
            if self.board[a[0]][a[1]] == FULL and self.board[a[0]][a[1]] == self.board[b[0]][b[1]] and self.board[a[0]][a[1]] == self.board[c[0]][c[1]]:
                return self.history[-1].player
            return " " 

    def moveIsLegal(self, move: Move):
        oldValue = self.getCell(move.x, move.y)
        alreadyPlaced = oldValue == FULL or oldValue == move.player
        lastMove = self.history[-1]
        placedLastMove = lastMove.x == move.x and lastMove.y == move.y
        return not alreadyPlaced and not placedLastMove

    def getLegalMoves(self):
        allMoves = [Move(i % 3, i // 3, self.currentPlayer) for i in range(9)]
        return list(filter(self.moveIsLegal, allMoves))