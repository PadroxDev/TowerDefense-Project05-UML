from pygame.math import Vector2
from models.Map import Path

CHECKPOINT_PROXIMITY_VALIDATION = 50

class Enemy:
    def __init__(self, pos: Vector2, hp: int, speed: int, dropMoney: int, difficultyScalar: float):
        self.position = pos
        self.hp = hp * difficultyScalar
        self.speed = speed
        self.dropMoney = dropMoney
        self.currentWaypoint = 0

    def moveTowardsWaypoint(self, dT: float):
        waypoint: Vector2 = Path[self.currentWaypoint]
        dir: Vector2 = (waypoint - self.position)
        if(dir!=Vector2(0,0)): dir = dir.normalize()
        self.position += dir * self.speed * dT

        distance = (waypoint - self.position).magnitude()
        if (distance > CHECKPOINT_PROXIMITY_VALIDATION):
            return False
        
        # Increment waypoint index
        self.currentWaypoint += 1
        if(self.currentWaypoint == len(Path)-1): # Path completed
            return True # Means this unit has to be removed from the list and destroyed

    def takeDamage(self, damage):
        self.hp -= damage
