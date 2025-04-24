class SquadManager:
    def __init__(self, ini_paths):
        self.npcs = [NPC(path) for path in ini_paths]

    def run(self):
        while True:
            for npc in self.npcs:
                npc.tick()