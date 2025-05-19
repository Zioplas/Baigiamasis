from tkinter import Label, W


class ErrorDisplay:
    def __init__(self, bet_display):
        self.bet_display = bet_display
        self.error_label = Label(bet_display.bet_frame, bg="darkgreen", fg="red")
        self.error_label.grid(row=4, column=0, columnspan=2, sticky=W)
