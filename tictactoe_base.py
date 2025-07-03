from abc import ABC, abstractmethod

class TicTacToeBase(ABC):
    def __init__(self):
        self.board = [' '] * 9
        self.player = 'X'

    def check_winner(self, player):
        b = self.board
        wins = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]
        return any(b[i]==b[j]==b[k]==player for i,j,k in wins)

    def is_draw(self):
        return ' ' not in self.board

    @abstractmethod
    def play(self):
        pass

