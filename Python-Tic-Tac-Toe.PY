import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [" "]*9

        # Crear botones
        self.buttons = [tk.Button(root, text=" ", font=("Helvetica", 20), width=6, height=3,
                                  command=lambda i=i: self.make_move(i)) for i in range(9)]

        # Posicionar los botones en la cuadrícula
        for i, button in enumerate(self.buttons):
            row, col = divmod(i, 3)
            button.grid(row=row, column=col)

    def make_move(self, index):
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("¡Ganador!", f"¡El jugador {self.current_player} ha ganado!")
                self.reset_board()
            elif " " not in self.board:
                messagebox.showinfo("Empate", "¡El juego ha terminado en empate!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Verificar filas, columnas y diagonales
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != " ":
                return True
            if self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] != " ":
                return True
        if self.board[0] == self.board[4] == self.board[8] != " " or \
           self.board[2] == self.board[4] == self.board[6] != " ":
            return True
        return False

    def reset_board(self):
        # Reiniciar el tablero y los botones
        self.board = [" "]*9
        for button in self.buttons:
            button.config(text=" ")
        self.current_player = "X"


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
