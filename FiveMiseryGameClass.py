from src.board5MiseryClass import Board5Misery
from src.gameClass import Game

class FiveMisery:
    
    def __init__(self, count=1, k=5):
        self.k = k
        self.count = count
        self.initial = Board5Misery(to_move="X")
        print(self.initial)

    def actions(self,state):
        return [1,2,3]
    
    def result(self, board, call):
        player = board.to_move
        board = board.new(('O' if player == 'X' else 'X'), call)
        win = (True if board.counter >= 5 else False)
        board.utility = 0
        board.utility = (0 if not win else -1 if player == 'X' else +1)
        return board
    
    def utility(self, board, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        return board.utility if player == 'X' else -board.utility
    
    def is_terminal(self, board):
        """A board is a terminal state if it is won or there are no empty squares."""
        return board.utility != 0 or board.counter >= 5
    
    def display(self,board):
        print(board.counter)