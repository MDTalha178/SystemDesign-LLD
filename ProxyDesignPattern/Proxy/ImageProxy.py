from typing import Optional

from Interface.Interface import Image
from models.HighResolutionImage import HighResolutionImage


class HighResolutionImageProxy(Image):
    def __init__(self, file_name, file_size):
        self.file_name = file_name
        self.file_size = file_size
        self.real_image:Optional[HighResolutionImage] = None


    def get_file_name(self):
        return self.file_name

    def display(self):
        if self.real_image is None:
            print(f"ImageProxy: display() requested for {self.file_name}. Loading high-resolution image...")
            self.real_image = HighResolutionImage(self.file_name, self.file_size)
        self.real_image.display()

    def _load_image(self):
        self.display()
