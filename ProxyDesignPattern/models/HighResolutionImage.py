import time

from Interface.Interface import Image


class HighResolutionImage(Image):
    def __init__(self, filename, file_size):
        self.filename = filename
        self.file_size = file_size
        self.image = self._load_image()  ## its an expensive  operation

    def _load_image(self):
        print("Loading image from disk please wait...")
        time.sleep(5)
        print("Image Loaded successfully!")
        return f"{self.filename}.{self.file_size}"

    def display(self):
        return f"{self.filename}.{self.file_size}"
    def get_file_name(self):
        return f"{self.filename}"
