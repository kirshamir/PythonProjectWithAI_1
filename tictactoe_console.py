from tictactoe_base import TicTacToeBase

class TicTacToeConsole(TicTacToeBase):
    def print_board(self):
        b = self.board
        print(f"\n {b[0]} | {b[1]} | {b[2]}")
        print("---+---+---")
        print(f" {b[3]} | {b[4]} | {b[5]}")
        print("---+---+---")
        print(f" {b[6]} | {b[7]} | {b[8]}\n")

    def play(self):
        for turn in range(9):
            self.print_board()
            while True:
                try:
                    move = int(input(f"Player {self.player}, enter 1-9: ")) - 1
                    if 0 <= move < 9 and self.board[move] == ' ':
                        self.board[move] = self.player
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Please enter a number 1-9.")
            if self.check_winner(self.player):
                self.print_board()
                print(f"Player {self.player} wins!")
                return
            self.player = 'O' if self.player == 'X' else 'X'
        self.print_board()
        print("It's a draw!")

