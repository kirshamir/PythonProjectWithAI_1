import tkinter as tk
import tkinter.messagebox
from tictactoe_base import TicTacToeBase

class TicTacToeGUI(TicTacToeBase):
    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.buttons = []
        self.player_var = tk.StringVar(value=self.player)

    def on_click(self, i):
        if self.board[i] == ' ':
            self.board[i] = self.player
            self.buttons[i]["text"] = self.player
            if self.check_winner(self.player):
                for btn in self.buttons:
                    btn["state"] = "disabled"
                tk.messagebox.showinfo("Game Over", f"Player {self.player} wins!")
            elif self.is_draw():
                tk.messagebox.showinfo("Game Over", "It's a draw!")
            else:
                self.player = 'O' if self.player == 'X' else 'X'
                self.player_var.set(self.player)

    def play(self):
        for i in range(9):
            btn = tk.Button(self.root, text=' ', width=5, height=2, font=('Arial', 24),
                            command=lambda i=i: self.on_click(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)
        self.root.mainloop()

