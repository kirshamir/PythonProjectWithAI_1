import pytest
from tictactoe_base import TicTacToeBase

class DummyTicTacToe(TicTacToeBase):
    def play(self):
        pass

def test_check_winner_rows():
    game = DummyTicTacToe()
    game.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
    assert game.check_winner('X')
    game.board = [' ', ' ', ' ', 'O', 'O', 'O', ' ', ' ', ' ']
    assert game.check_winner('O')

def test_check_winner_columns():
    game = DummyTicTacToe()
    game.board = ['X', ' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ']
    assert game.check_winner('X')
    game.board = [' ', 'O', ' ', ' ', 'O', ' ', ' ', 'O', ' ']
    assert game.check_winner('O')

def test_check_winner_diagonals():
    game = DummyTicTacToe()
    game.board = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
    assert game.check_winner('X')
    game.board = [' ', ' ', 'O', ' ', 'O', ' ', ' ', ' ', 'O']  # No win for 'O'
    assert not game.check_winner('O')
    game.board = [' ', ' ', 'O', ' ', 'O', ' ', 'O', ' ', ' ']
    assert not game.check_winner('X')
    game.board = [' ', ' ', 'O', ' ', 'O', ' ', 'X', ' ', 'O']
    assert not game.check_winner('O')

def test_is_draw():
    game = DummyTicTacToe()
    game.board = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
    assert game.is_draw()
    game.board = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', ' ']
    assert not game.is_draw()
