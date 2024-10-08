from reader.read_datalake import ReadDatalake

class ReaderFactory:

    _readers = {
        'ReadFilesBio': ReadDatalake
    }

    @staticmethod
    def initialize_reader(key):
        reader_class = ReaderFactory._readers.get(key)
        if reader_class:
            return reader_class()
        else:
            raise ValueError(f"Invalid reader key: {key}")

