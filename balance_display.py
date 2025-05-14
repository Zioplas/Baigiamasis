from tkinter import Label, Frame, W

class BalanceDisplay:
    def __init__(self, window):
        self.frame = Frame(window, bg="darkgreen")
        self.frame.grid(row=0, column=0, sticky=W)

        self.balance_label = Label(self.frame, text="Balansas:", bg="darkgreen", fg="white")
        self.balance_label.grid(row=0, column=0)

        self.balance_amount_label = Label(self.frame, text="0", bg="darkgreen", fg="white")
        self.balance_amount_label.grid(row=0, column=1, sticky=W)

    def set_balance(self, value):
        self.balance_amount_label.config(text=str(value))

    def get_balance(self):
        return float(self.balance_amount_label["text"])