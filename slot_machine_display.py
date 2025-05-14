from tkinter import Frame, Label
from PIL import Image, ImageTk

class SlotMachineDisplay:
    def __init__(self, window, initial_image_path):
        self.frame = Frame(window, bg="darkgreen")
        self.frame.grid(row=1, column=0, columnspan=3)

        self.images = []
        self.labels = []

        for i in range(3):
            image = self.load_image(initial_image_path)
            self.images.append(image)

        for i in range(3):
            label = Label(self.frame, image=self.images[i], relief="sunken", bg="purple")
            self.labels.append(label)

        for i, label in enumerate(self.labels):
            label.grid(row=0, column=i)

    def load_image(self, path):
        return ImageTk.PhotoImage(Image.open(path).resize((100, 100)))

    def update_slots(self, image_paths):
        for i, path in enumerate(image_paths):
            new_image = self.load_image(path)
            self.images[i] = new_image
            self.labels[i].configure(image=new_image)
