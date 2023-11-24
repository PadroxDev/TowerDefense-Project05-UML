from pygame.math import Vector2
from models.Map import Path
from pygame import Surface
from enum import Enum
from view.HealthBar import HealthBar

CHECKPOINT_PROXIMITY_VALIDATION = 1.5

class State(Enum):
    UpdateWaypoint = 0
    MoveToWaypoint = 1
    ReachedEndOfPath = 2
    Dead = 3

class Enemy:
    def __init__(self, pos: Vector2, hp: int, speed: int, dropMoney: int, difficultyScalar: float):
        self.position = pos
        self.maxHp = hp * difficultyScalar
        self.hp = self.maxHp
        self.speed = speed
        self.dropMoney = dropMoney
        self.currentWaypoint = 0
        self.dead = False
        self.reachedEndOfPath = False
        self.currentState = State.UpdateWaypoint
        self.healthBar = HealthBar(Vector2(self.position.x - 100, self.position.y - 150), Vector2(120, 40), 4)

    def setHealthBarRect(self):
        self.healthBar.position = self.position.x - 60, self.position.y - 150

    def update(self, dT: float):
        self.setHealthBarRect()
        self.healthBar.update(self.hp, self.maxHp)
        match(self.currentState):
            case State.UpdateWaypoint:
                self.handleUpdateWaypoint()
            case State.MoveToWaypoint:
                self.handleMoveToWaypoint(dT)
            case State.ReachedEndOfPath:
                self.handleReachEndOfPath()
            case State.Dead:
                self.handleDead()

    def handleUpdateWaypoint(self):
        self.currentWaypoint += 1
        if(self.currentWaypoint == len(Path)): # Path complete
            self.currentState = State.ReachedEndOfPath
        else:
            self.currentState = State.MoveToWaypoint

    def handleMoveToWaypoint(self, dT):
        waypoint: Vector2 = Path[self.currentWaypoint].copy()
        dir: Vector2 = (waypoint - self.position)
        if(dir!=Vector2(0,0)): dir = dir.normalize()
        self.position += dir * self.speed * dT

        distance = (waypoint - self.position).magnitude()
        if (distance <= CHECKPOINT_PROXIMITY_VALIDATION):
            self.currentState = State.UpdateWaypoint

    def handleReachEndOfPath(self):
        self.reachedEndOfPath = True

    def handleDead(self):
        self.dead = True # Wait to be dispawned automatically

    def takeDamage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.currentState = State.Dead

    def render(self, surf: Surface):
        self.healthBar.render(surf)