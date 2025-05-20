import random
from PIL import ImageTk, Image


class SlotMachine:
    def __init__(self, full_image_paths, image_size=(100, 100)):
        self.full_image_paths = full_image_paths
        self.image_size = image_size
        self.images = []
        self.weights = [1, 2, 5, 8, 0.5, 10]

        for path in full_image_paths:
            image = Image.open(path).resize(image_size)
            self.images.append(ImageTk.PhotoImage(image))

    def spin(self):
        return random.choices(self.full_image_paths, weights=self.weights, k=3)
