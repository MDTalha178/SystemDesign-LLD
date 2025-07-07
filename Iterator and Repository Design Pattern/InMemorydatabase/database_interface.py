from abc import ABC


class DatabaseInterface(ABC):

    def create_connection(self):
        return self
