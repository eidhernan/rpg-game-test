from item import Item
from items import Weapon, Armor, HealingItem
from player import Player
from utils import FixedList
from menu import Menu

def main():
    blank_item = Item(name="Empty", description="", value=0)
    apple = HealingItem(name="Apple", description="Restores 7 HP", value=10, heals=7)
    old_dagger = Weapon(name="Old Dagger", description="Deals 9 damage", value=14, atk=9)
    pow_glove = Weapon(name="POW Glove", description="Deals 3 damage", value=6, atk=3)
    shield = Armor(name="Shield", description="Adds 7 DEF", value=10, defense=7)
    old_jacket = Armor(name="Old Jacket", description="It's just a jacket", value=3, defense=0)

    inventory = FixedList(size=8, fill=blank_item)
    player = Player(name="David", hp=20, xp=20, lv=1, atk=3, defense=0, weapon=pow_glove, armor=old_jacket, inventory=inventory)
    menu = Menu(player)
    player.inventory.append(apple)
    player.inventory.append(old_jacket)

    menu.open()

main()
