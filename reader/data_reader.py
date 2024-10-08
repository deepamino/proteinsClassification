from abc import ABC, abstractmethod

class DataReader(ABC):
    def set_path(self, path):
        self.path = path

    @abstractmethod
    def read(self, *args):
        pass