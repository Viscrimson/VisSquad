import sqlite3

class ConvoLogger:
    def __init__(self, db_path='logs/convo.db'):
        self.conn = sqlite3.connect(db_path)

    def append(self, speaker, text):
        # TODO: insert timestamped record
        pass