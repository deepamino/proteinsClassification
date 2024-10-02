
from datacollector import DataCollector

class FileDataCollector(DataCollector):

    def collect(self, *args):
        with open(args, 'r') as file:
            return file.read()