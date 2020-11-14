from entity import Entity
from items import Armor, Weapon
from utils import FixedList
class Player(Entity):
    """
    The main character of the game
    Inherited Fields:
    name: str
    hp: int
    xp: int
    lv: int
    atk: int
    max_hp: int
    max_xp: int
    """
    weapon: Weapon
    armor: Armor
    inventory: FixedList

    def __init__(self, name: str, hp: int, xp: int, lv: int, atk: int, defense: int, weapon: Weapon, armor: Armor, inventory: FixedList):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.xp = 0
        self.max_xp = xp
        self.lv = lv
        self.atk = atk
        self.defense = defense
        self.weapon = weapon
        self.armor = armor
        self.inventory = inventory


    def equip_weapon(self, weapon: Weapon):
        """
        Equip a weapon
        """
        self.atk -= self.weapon.atk
        self.inventory.append(self.weapon)
        self.weapon = weapon
        self.atk += weapon.atk
    
    def equip_armor(self, armor: Armor):
        """
        Equip armor
        """
        self.defense -= self.armor.defense
        self.inventory.append(self.armor)
        self.armor = armor
        self.defense += armor.defense