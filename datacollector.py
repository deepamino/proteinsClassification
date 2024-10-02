from abc import ABC, abstractmethod

class DataCollector(ABC):

    
    @abstractmethod
    def collect(self):
        pass