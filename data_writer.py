from abc import ABC, abstractmethod

class DataWriter(ABC):
    def set_path(self, path):
        self.path = path

    @abstractmethod
    def write(self, *args):
        pass