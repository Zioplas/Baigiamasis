from tkinter import Label, W, E


class WinDisplay:
    def __init__(self, bet_display):
        self.bet_display = bet_display

        self.win_text_label = Label(bet_display.bet_frame, text="laimejimai", bg="darkgreen", fg="yellow")
        self.win_text_label.grid(row=3, column=0, sticky=E)

        self.win_amount_label = Label(bet_display.bet_frame, text="0", bg="darkgreen", fg="white")
        self.win_amount_label.grid(row=3, column=1, sticky=W)
