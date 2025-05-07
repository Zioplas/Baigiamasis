import random
from PIL import ImageTk, Image

class SlotMachine:
    def __init__(self, image_paths, image_size=(100, 100)):
        self.image_paths = image_paths
        self.image_size = image_size
        self.images = []
        for path in image_paths:
            self.images.append(ImageTk.PhotoImage(Image.open(path).resize(image_size)))


    def spin(self):
        result = []
        for i in range(3):
            result.append(random.choice(self.image_paths))
        return result
