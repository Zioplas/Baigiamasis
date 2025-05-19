from tkinter import Menu
from add_balance_window import AddBalanceWindow


class MenuDisplay:
    def __init__(self, window, balance_display):
        self.balance_display = balance_display
        self.menu = Menu(window)
        window.config(menu=self.menu)
        self.submenu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Meniu", menu=self.submenu)
        self.submenu.add_command(
            label="Papildyti balansą", command=lambda: AddBalanceWindow(window, balance_display))
