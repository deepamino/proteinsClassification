from reader.data_reader import DataReader
import os
import pandas as pd

class ReadDatalake(DataReader):

    def read(self):
        sequences = []
        for file in os.listdir(self.path):
            with open(self.path + '/' + file, 'r') as f:
                sequences.append(f.read())
        
        return pd.DataFrame(sequences, columns=['sequence'])
                




