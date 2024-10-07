from collector.data_writer import DataWriter

class FileWriter(DataWriter):
    def write(self, filename, data):
        filename = self.normalize_name(filename)
        with open(filename, 'w') as file:
            file.write(data)

    def normalize_name(self, name):
        name = name.replace('|', '_').lower()
        return self.path + '/' + name + '.bio'