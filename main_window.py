from tkinter import *
from PIL import ImageTk, Image
from slot_machine import SlotMachine
from add_balance_window import AddBalanceWindow
from slot_machine_display import SlotMachineDisplay

# window -----------------------------------------------
window = Tk()
window.title("Baigiamoji kazinke")
window.geometry("500x500")
window.configure(bg="darkgreen")

window.grid_rowconfigure(0, weight=0)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

# slot machine -----------------------------------------------
symbols = [
    r"D:\Python mokslai\BaigiamasisRepo\Baigiamasis\pictures\dollar.png",
    r"D:\Python mokslai\BaigiamasisRepo\Baigiamasis\pictures\bar.png",
    r"D:\Python mokslai\BaigiamasisRepo\Baigiamasis\pictures\cherries.png",
    r"D:\Python mokslai\BaigiamasisRepo\Baigiamasis\pictures\lemon.png",
    r"D:\Python mokslai\BaigiamasisRepo\Baigiamasis\pictures\seven.png",
    r"D:\Python mokslai\BaigiamasisRepo\Baigiamasis\pictures\watermelon.png",
]
machine = SlotMachine(symbols)

# balance display -----------------------------------------------
balance_frame = Frame(window, bg="darkgreen")
balance_frame.grid(row=0, column=0, sticky=W)

balance_label = Label(balance_frame, text="Balansas:", bg="darkgreen", fg="white")
balance_label.grid(row=0, column=0)

balance_amount_label = Label(balance_frame, text="0", bg="darkgreen", fg="white")
balance_amount_label.grid(row=0, column=1, sticky=W)

# menu -----------------------------------------------
menu = Menu(window)
window.config(menu=menu)
submenu = Menu(menu, tearoff=0)

menu.add_cascade(label="Meniu", menu=submenu)
submenu.add_command(label="Papildyti balansą", command=lambda: AddBalanceWindow(window, balance_amount_label))

# bet size  -----------------------------------------------
bet_size_label = Label(window, text="Bet size:", bg="darkgreen", fg="white")
bet_size_label.grid(row=2, column=0, sticky=E)

bet_size_entry = Entry(window)
bet_size_entry.grid(row=2, column=1, sticky=W)

# slot machine display -----------------------------------------------
slot_display = SlotMachineDisplay(window, symbols[0])

# spin button -----------------------------------------------
def spin_slots():
    try:
        bet = float(bet_size_entry.get())
        balance = float(balance_amount_label["text"])

        if bet <= 0 or bet > balance:
            print("Invalid bet amount.")
            return

        new_paths = machine.spin()
        slot_display.update_slots(new_paths)

        new_balance = balance - bet
        balance_amount_label.config(text=str(new_balance))

    except ValueError:
        print("Enter a valid number in bet size.")

button_image = ImageTk.PhotoImage(Image.open(
    r"D:\Python mokslai\BaigiamasisRepo\Baigiamasis\pictures\switch-on.png").resize((50, 50)))

spin_button = Button(window, command=spin_slots, image=button_image, relief="flat", bg="darkgreen")
spin_button.grid(row=2, column=2, sticky=W)

window.mainloop()
