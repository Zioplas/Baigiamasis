import os
import random
from PIL import ImageTk, Image


class SlotMachine:
    def __init__(self, image_filenames, base_dir, image_size=(100, 100)):
        self.base_dir = base_dir
        self.image_paths = []
        self.image_size = image_size
        self.images = []
        self.weights = [1, 2, 5, 8, 0.5, 10]

        for filename in image_filenames:
            self.image_paths.append(os.path.join(base_dir, "pictures", filename))

        for path in self.image_paths:
            image = Image.open(path).resize(image_size)
            self.images.append(ImageTk.PhotoImage(image))

    def spin(self):
        return random.choices(self.image_paths, weights=self.weights, k=3)
