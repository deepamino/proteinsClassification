from writer.file_writer import FileWriter

class WriterFactory:

    _writers = {
        'FileWriter': FileWriter,
    }

    @staticmethod
    def initialize_writer(key):
        collector_class = WriterFactory._writers.get(key)
        if collector_class:
            return collector_class()
        else:
            raise ValueError(f"Invalid writer key: {key}")
