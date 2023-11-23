from models.Wave import Waves
from models.Enemies.Piggy import Piggy
from models.Enemies.PigKnight import PigKnight
from models.Enemies.Iris import Iris
from models.Money import Money
from models.Map import Path
from pygame import Surface

TIME_BEFORE_STARTING = 3
TIME_BETWEEN_SPAWNS = 2

class EventManager:
    def __init__(self, moulaga):
        self.waveIndex = 0
        self.mobIndex = 0
        self.enemiesAlive = []
        self.moulaga = moulaga
        self.waitingTime = TIME_BEFORE_STARTING
        self.doneSpawningWaves = False

    def update(self, dT: float):
        self.updateWaves(dT)
        self.updateEnemies(dT)

    def updateWaves(self, dT: float):
        if(self.doneSpawningWaves): return

        self.waitingTime -= dT
        if(self.waitingTime > 0): return

        # Check if there are still mobs to spawn in the current wave
        wave: str = Waves[self.waveIndex]
        if(self.mobIndex < len(wave)):
            mobChar = wave[self.mobIndex]
            self.spawnEnemyFromChar(mobChar)
            self.mobIndex += 1
            self.waitingTime = TIME_BETWEEN_SPAWNS
        elif(len(self.enemiesAlive) == 0):
            self.waveIndex += 1

            # Check if it was the last wave
            if(self.waveIndex == len(Waves)):
                self.doneSpawningWaves = True

    def updateEnemies(self, dT: float):
        for enemy in self.enemiesAlive:
            reachedEndOfPath = enemy.moveTowardsWaypoint(dT)
            if(reachedEndOfPath or enemy.dead):
                self.enemiesAlive.remove(enemy)
                self.moulaga.addMoney(50)

    def spawnEnemyFromChar(self, char):
        if(char == 'P'):
            spawnPoint = Path[0].copy()
            piggy = Piggy(spawnPoint)
            self.enemiesAlive.append(piggy)
        if(char == 'K'):
            spawnPoint = Path[0].copy()
            pigknight = PigKnight(spawnPoint)
            self.enemiesAlive.append(pigknight)
        if(char == 'I'):
            spawnPoint = Path[0].copy()
            iris = Iris(spawnPoint)
            self.enemiesAlive.append(iris)

    def render(self, surf: Surface):
        for enemy in self.enemiesAlive:
            enemy.render(surf)

    def skipWave(self):
        pass