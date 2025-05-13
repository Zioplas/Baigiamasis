from tkinter import *
from slot_machine import SlotMachine
from menu_display import MenuDisplay
from slot_machine_display import SlotMachineDisplay
from balance_display import BalanceDisplay
from bet_display import BetDisplay
from win_display import WinDisplay
from error_display import ErrorDisplay
from button_display import ButtonDisplay
from payout import Payout
import os

window = Tk()
window.title("Baigiamoji kazinke")
window.geometry("500x500")
window.configure(bg="darkgreen")

window.grid_rowconfigure(0, weight=0)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

base_dir = os.path.dirname(__file__)
symbols = [
    "dollar.png",
    "bar.png",
    "cherries.png",
    "lemon.png",
    "seven.png",
    "watermelon.png",
]
full_image_paths = [os.path.join(base_dir, "pictures", filename) for filename in symbols]
machine = SlotMachine(full_image_paths)

payouts = {
    os.path.join(base_dir, "pictures", "dollar.png"): 10,
    os.path.join(base_dir, "pictures", "bar.png"): 8,
    os.path.join(base_dir, "pictures", "cherries.png"): 6,
    os.path.join(base_dir, "pictures", "lemon.png"): 5,
    os.path.join(base_dir, "pictures", "seven.png"): 20,
    os.path.join(base_dir, "pictures", "watermelon.png"): 4,
}

payout = Payout(payouts)

balance_display = BalanceDisplay(window)

menu_display = MenuDisplay(window, balance_display)

bet_display = BetDisplay(window)

win_display = WinDisplay(bet_display)

error_display = ErrorDisplay(bet_display)

slot_display = SlotMachineDisplay(window, full_image_paths[0])

def spin_slots():
    error_display.error_label.config(text="")

    try:
        bet = float(bet_display.bet_size_entry.get())
        balance = float(balance_display.balance_amount_label["text"])

        if bet <= 0 or bet > balance:
            error_display.error_label.config(text="Invalid bet amount")
            return

        new_symbols = machine.spin()
        slot_display.update_slots(new_symbols)

        balance -= bet
        winnings = payout.check_for_payout(bet, new_symbols)
        balance += winnings

        balance_display.balance_amount_label.config(text=str(balance))
        win_display.win_amount_label.config(text=str(winnings))

    except ValueError:
        error_display.error_label.config(text="Enter a number in bet size")

button_display = ButtonDisplay(window,spin_slots, base_dir)

window.mainloop()
