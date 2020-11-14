from time import sleep
from random import randint

class Entity:
    """
    An entity has a name as well as the base materials for any RPG character or enemy. 
    """
    name: str
    hp: int
    xp: int
    lv: int
    max_hp: int
    max_xp: int
    atk: int
    defense: int

    def __init__(self, name: str, hp: int, xp: int, lv: int, atk: int, defense: int):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.xp = 0
        self.max_xp = xp
        self.lv = lv
        self.atk = atk
        self.defense = defense
    
    def kill(self):
        """
        Kills the entity
        """
        print("Entity {} has died!".format(self.name))

    def heal(self, amt: int):
        """
        Heals the entity with the specified amount of points
        """
        if(self.hp + amt < self.max_hp):
            self.hp += amt
        else:
            self.hp += self.max_hp
    
    def full_heal(self):
        """
        Fully maxes out the entity's health
        """
        self.hp = self.max_hp
    
    def take_damage(self, amt: int):
        """
        Deals the specified amount of damage to the entity's health
        """
        if(self.hp - amt > 0):
            self.hp -= amt
        else:
            self.kill()
    
    def attack(self, target: 'Entity'):
        """
        Deal damage to another entity based roughly off the ATK variable.
        """
        damage = randint(self.hp // 2, self.hp)
        target.take_damage(damage)

    
    def level_up(self):
        """
        Increases the entity's level by one point
        """
        self.lv += 1
        self.max_hp += 1
        self.atk += 1
        self.defense += 1
        self.full_heal()
    
    def add_xp(self, amt: int):
        """
        Increases the entity's XP by the amount specified. If the entity's XP is maxed out, the entity will level up
        """
        amount: int = amt
        isFinished: bool = False
        while(not isFinished):
            if(self.xp + amount < self.max_xp):
                self.xp += amount
                isFinished = True
            else:
                self.xp = 0
                amount -= self.max_xp
                self.level_up()


if __name__ == "__main__":
    player = Entity(name="Y/N", hp=20, xp=20, lv=1, atk=3)
    player.add_xp(100)
    print(player.lv)
    print(player.hp)
    sleep(5)
