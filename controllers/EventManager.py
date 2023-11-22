from models.Wave import Waves

class EventManager:
    def __init__(self):
        self.waveIndex = 0
        self.mobIndex = 0
        self.ennemiesAlive = []

    def spawnWave(self):
        wave: list = Waves[self.waveIndex]
        mobChar = wave[self.mobIndex]

    def skipWave(self):
        pass