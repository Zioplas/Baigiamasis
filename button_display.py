from tkinter import Button, W
from PIL import ImageTk, Image
import os

class ButtonDisplay:
    def __init__(self, window, spin_slots, base_dir):
        self.window = window
        self.spin_slots = spin_slots
        self.base_dir = base_dir
        self.button_image = ImageTk.PhotoImage(
            Image.open(os.path.join(base_dir, "pictures", "spin_button.png")).resize((75, 75)))
        self.spin_button = Button(window, command=spin_slots, image=self.button_image, relief="flat", bg="darkgreen")
        self.spin_button.grid(row=2,column=2, sticky=W)