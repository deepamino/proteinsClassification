from encoder.bow_variation import BOWVariation

class EncoderFactory:

    _encoders = {
        'BOWVariation': BOWVariation
    }

    @staticmethod
    def initialize_encoder(key):
        encoder_class = EncoderFactory._encoders.get(key)
        if encoder_class:
            return encoder_class()
        else:
            raise ValueError(f"Invalid reader key: {key}")