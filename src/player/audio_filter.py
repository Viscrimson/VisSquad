class AudioFilter:
    def __init__(self, settings):
        self.settings = settings

    def filter_voice(self, audio_chunk):
        # TODO: apply VAD and return voice-only chunks
        return audio_chunk