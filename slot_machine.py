import os
import random
from PIL import ImageTk, Image

class SlotMachine:
    def __init__(self, image_filenames, image_size=(100, 100)):
        self.base_dir = os.path.dirname(__file__)
        self.image_paths = []
        self.image_size = image_size
        self.images = []

        for filename in image_filenames:
            self.image_paths.append(os.path.join(self.base_dir, "pictures", filename))

        for path in self.image_paths:
            image = Image.open(path).resize(image_size)
            self.images.append(ImageTk.PhotoImage(image))

    def spin(self):
        result = []
        for i in range(3):
            result.append(random.choice(self.image_paths))
        return result







