from ai.communication.whisper_client import WhisperClient

class Transcription:
    def __init__(self, settings):
        self.whisper = WhisperClient(settings.get('TTS', 'engine', fallback='EdgeTTS'))

    def transcribe(self, audio_chunk):
        # TODO: call WhisperClient.transcribe_stream
        return ""