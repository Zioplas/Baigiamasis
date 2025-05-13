from tkinter import Frame, Label, Entry, W, E

class BetDisplay:
    def __init__(self, window):
        self.bet_frame = Frame(window, bg="darkgreen")
        self.bet_frame.grid(row=2, column=0)
        self.bet_size_label = Label(self.bet_frame, text="Statymas:", bg="darkgreen", fg="white")
        self.bet_size_label.grid(row=2, column=0, sticky=W)
        self.bet_size_entry = Entry(self.bet_frame)
        self.bet_size_entry.grid(row=2, column=1, sticky=E)