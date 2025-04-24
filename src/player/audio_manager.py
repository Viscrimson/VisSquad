import sounddevice as sd

class AudioManager:
    def __init__(self, settings):
        self.settings = settings

    def list_input_devices(self):
        devices = sd.query_devices()
        return [d['name'] for d in devices if d['max_input_channels'] > 0]

    def list_output_devices(self):
        devices = sd.query_devices()
        return [d['name'] for d in devices if d['max_output_channels'] > 0]