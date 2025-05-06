from tkinter import Toplevel, Label, Entry, Button

class AddBalanceWindow:
    def __init__(self, master, balance_label):
        self.balance_label = balance_label

        self.popup = Toplevel(master)
        self.popup.title("Papildyti balansą")
        self.popup.geometry("300x150")
        self.popup.configure(bg="darkgreen")

        Label(self.popup, text="Įveskite sumą:", bg="darkgreen", fg="white").pack()

        self.amount_entry = Entry(self.popup)
        self.amount_entry.pack()

        Button(self.popup, text="Patvirtinti", command=self.add_funds).pack()

    def add_funds(self):
        try:
            amount = float(self.amount_entry.get())
            current_balance = float(self.balance_label["text"])
            new_balance = current_balance + amount
            self.balance_label.config(text=str(new_balance))
            self.popup.destroy()
        except ValueError:
            error_label = Label(self.popup, text="Įveskite teisingą sumą!", fg="red", bg="darkgreen")
            error_label.pack()












