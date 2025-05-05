from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.geometry("500x500")

window.configure(bg="darkgreen")
window.grid_rowconfigure(0, weight=0)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

# menu --------------------------------------------
menu = Menu(window)
window.config(menu=menu)
submenu = Menu(menu, tearoff=0)

menu.add_cascade(label="Meniu", menu=submenu)
submenu.add_command(label="papildyti balansa")

# balance -----------------------------------------
balance_frame = Frame(window)
balance_amount_label = Label(balance_frame, text="0", bg="darkgreen")
balance_label = Label(balance_frame, text="Balansas:", bg="darkgreen")
balance_frame.grid(row=0,column=0, sticky=W)
balance_label.grid(row=0, column=0)
balance_amount_label.grid(row=0, column=1, sticky=W)

# slots -----------------------------------------
slot_image_1 = ImageTk.PhotoImage(Image.open(r"D:\Python mokslai\BaigiamasisRepo\Baigiamasis\pictures\dollar.png").resize((100,100)))
slot_image_2 = ImageTk.PhotoImage(Image.open(r"D:\Python mokslai\BaigiamasisRepo\Baigiamasis\pictures\dollar.png").resize((100,100)))
slot_image_3 = ImageTk.PhotoImage(Image.open(r"D:\Python mokslai\BaigiamasisRepo\Baigiamasis\pictures\dollar.png").resize((100,100)))

slot_frame = Frame(window)
slot_frame.grid(row=1, column=0, columnspan=3)

slot_1 = Label(slot_frame, image=slot_image_1, relief="sunken", bg="red")
slot_2 = Label(slot_frame, image=slot_image_2, relief="sunken", bg="red")
slot_3 = Label(slot_frame, image=slot_image_3, relief="sunken", bg="red")

slot_1.grid(row=0, column=0)
slot_2.grid(row=0, column=1)
slot_3.grid(row=0, column=2)

# button -----------------------------------------
button_image_on = ImageTk.PhotoImage(Image.open(r"D:\Python mokslai\BaigiamasisRepo\Baigiamasis\pictures\switch-on.png").resize((50,50)))
button_image_off = ImageTk.PhotoImage(Image.open(r"D:\Python mokslai\BaigiamasisRepo\Baigiamasis\pictures\switch-off.png").resize((50,50)))

button = Button(window, image=button_image_off, relief="flat", bg="darkgreen")
button.grid(row=2, column=2, sticky=W)

# bet size ----------------------------------------
bet_size_label = Label(window, text="Bet size:", relief="flat", bg="darkgreen")
bet_size_entry = Entry(window)

bet_size_label.grid(row=2, column=0, sticky=E)
bet_size_entry.grid(row=2, column=1, sticky=W)

window.mainloop()
