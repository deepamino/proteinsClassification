from file_data_collector import FileDataCollector
from api_data_collector import ApiDataCollector

class CollectorFactory:

    _collectors = {
        'Files': FileDataCollector,
        'APIncbi': ApiDataCollector
    }

    @staticmethod
    def initialize_collector(key):
        collector_class = CollectorFactory._collectors.get(key)
        if collector_class:
            return collector_class()
        else:
            raise ValueError(f"Invalid collector key: {key}")
