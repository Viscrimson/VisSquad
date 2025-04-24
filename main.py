from PyQt6.QtCore import Qt
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtWidgets import QApplication
from player.audio_manager import AudioManager
from player.audio_capture import AudioCapture
from player.audio_filter import AudioFilter
from player.transcription import Transcription
from player.ui_controller import UIController
from ai.core.squad import SquadManager
from tts.tts_adapter import TTSAdapter
from osc.osc_manager import OSCManager
from player.settings_manager import SettingsManager

# High DPI policy
QGuiApplication.setHighDpiScaleFactorRoundingPolicy(
    Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
)

def main():
    app = QApplication([])
    settings = SettingsManager('config/settings.ini')

    audio_mgr = AudioManager(settings)
    capture = AudioCapture(settings)
    filter_  = AudioFilter(settings)
    transcription = Transcription(settings)
    osc_mgr = OSCManager(settings)
    tts      = TTSAdapter(settings)
    ui = UIController(settings, tts, audio_mgr, transcription)

    squad = SquadManager([
        'config/lyra.ini','config/xyla.ini',
        'config/ayda.ini','config/tyfa.ini'
    ])

    ui.run()
    app.exec()

if __name__=='__main__':
    main()