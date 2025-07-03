import sys
from tictactoe_console import TicTacToeConsole
from tictactoe_gui import TicTacToeGUI
from tictactoe_web import run as run_web

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [console|gui|web]")
        return
    mode = sys.argv[1].lower()
    if mode == 'console':
        TicTacToeConsole().play()
    elif mode == 'gui':
        TicTacToeGUI().play()
    elif mode == 'web':
        run_web()
    else:
        print("Unknown mode. Use 'console', 'gui', or 'web'.")

if __name__ == "__main__":
    main()
