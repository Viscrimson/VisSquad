import sounddevice as sd

class AudioCapture:
    def __init__(self, settings):
        self.settings = settings

    def start_stream(self, callback):
        # TODO: open input stream and call callback on audio chunks
        pass