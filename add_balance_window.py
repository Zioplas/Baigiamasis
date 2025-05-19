from tkinter import Toplevel, Label, Entry, Button


class AddBalanceWindow:
    def __init__(self, master, balance_display):
        self.balance_display = balance_display
        self.add_balance_window = Toplevel(master)
        self.add_balance_window.title("Papildyti balansą")
        self.add_balance_window.geometry("300x150")
        self.add_balance_window.configure(bg="darkgreen")

        self.balace_label = Label(self.add_balance_window, text="Įveskite sumą:", bg="darkgreen", fg="white")
        self.balace_label.pack()

        self.amount_entry = Entry(self.add_balance_window)
        self.amount_entry.pack()

        self.confirm_button = Button(self.add_balance_window, text="Patvirtinti", command=self.add_funds)
        self.confirm_button.pack()

        self.error_label = Label(self.add_balance_window, text="", fg="red", bg="darkgreen")
        self.error_label.pack()

    def add_funds(self):
        try:
            amount = float(self.amount_entry.get())
            current_balance = self.balance_display.get_balance()
            new_balance = current_balance + amount
            self.balance_display.set_balance(new_balance)
            self.add_balance_window.destroy()
        except ValueError:
            self.error_label.config(text="Įveskite teisingą sumą!")
