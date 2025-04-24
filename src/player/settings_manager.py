import configparser, os

class SettingsManager:
    def __init__(self, path):
        self.path = path
        self.config = configparser.ConfigParser()
        self.load()

    def load(self):
        if not os.path.exists(self.path) or os.path.getsize(self.path) == 0:
            self.create_defaults()
        else:
            self.config.read(self.path)
        self.save()

    def create_defaults(self):
        # populate default sections: Audio, OSC, TTS, Names, Defaults
        pass

    def save(self):
        with open(self.path, 'w') as f:
            self.config.write(f)

    def get(self, section, option, fallback=None):
        return self.config.get(section, option, fallback=fallback)

    def set(self, section, option, value):
        if section not in self.config:
            self.config.add_section(section)
        self.config.set(section, option, str(value))
        self.save()