from flask import Flask, render_template, request, session, redirect, url_for
from tictactoe_base import TicTacToeBase
import os

class TicTacToeWeb(TicTacToeBase):
    def __init__(self):
        super().__init__()

    def to_dict(self):
        return {
            'board': self.board,
            'player': self.player
        }

    def from_dict(self, data):
        self.board = data.get('board', [' '] * 9)
        self.player = data.get('player', 'X')

    def play(self):
        # Not used in web mode, but required by abstract base class
        pass

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'devkey')

def get_game():
    game = TicTacToeWeb()
    if 'game' in session:
        game.from_dict(session['game'])
    return game

def save_game(game):
    session['game'] = game.to_dict()

@app.route('/', methods=['GET', 'POST'])
def index():
    game = get_game()
    winner = None
    draw = False
    if request.method == 'POST':
        if 'reset' in request.form:
            session.pop('game', None)
            return redirect(url_for('index'))
        move = request.form.get('move')
        if move is not None and game.board[int(move)] == ' ' and not game.check_winner('X') and not game.check_winner('O'):
            game.board[int(move)] = game.player
            if game.check_winner(game.player):
                winner = game.player
            elif game.is_draw():
                draw = True
            else:
                game.player = 'O' if game.player == 'X' else 'X'
        save_game(game)
    # Check for winner/draw after move
    if game.check_winner('X'):
        winner = 'X'
    elif game.check_winner('O'):
        winner = 'O'
    elif game.is_draw():
        draw = True
    return render_template('tictactoe.html', board=game.board, player=game.player, winner=winner, draw=draw)

def run():
    app.run(debug=True)
