class Enemy:
    def __init__(self, hp: int, speed: int, dropMoney: int):
        self.hp = hp
        self.speed = speed
        self.dropMoney = dropMoney

    def move(self, dT):
        pass

    def takeDamage(self, damage):
        self.hp -= damage