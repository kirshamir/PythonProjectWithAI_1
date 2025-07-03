import sys
from tictactoe_console import TicTacToeConsole
from tictactoe_gui import TicTacToeGUI

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [console|gui]")
        return
    mode = sys.argv[1].lower()
    if mode == 'console':
        TicTacToeConsole().play()
    elif mode == 'gui':
        TicTacToeGUI().play()
    else:
        print("Unknown mode. Use 'console' or 'gui'.")

if __name__ == "__main__":
    main()
