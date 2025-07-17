from abc import ABC, abstractmethod


class Image(ABC):

    @abstractmethod
    def _load_image(self):
        raise NotImplemented('Subclass should have to implement')
    @abstractmethod
    def display(self):
        raise NotImplemented('Subclass should have to implement')

    @abstractmethod
    def get_file_name(self):
        raise NotImplemented('Subclass should have to implement')