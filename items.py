from item import Item

class HealingItem(Item):
    """
    Item that restores health
    """
    heals: int

    def __init__(self, name: str, description: str, value: int, heals: int):
        super().__init__(name, description, value)
        self.heals = heals
    
    def use(self, player: 'Player'):
        """
        Heal the player
        """
        player.heal(self.heals)
        self.drop(player)

class Weapon(Item):
    """
    Item that can be used to attack others
    """
    atk: int

    def __init__(self, name: str, description: str, value: int, atk: int):
        super().__init__(name, description, value)
        self.atk = atk
    
    def use(self, player: 'Player'):
        """
        Equip the weapon
        """
        player.equip_weapon(self)
        self.drop(player)

class Armor(Item):
    """
    Used for defense against attacks
    """
    defense: int

    def __init__(self, name: str, description: str, value: int, defense: int):
        super().__init__(name, description, value)
        self.defense = defense
        
    
    def use(self, player: 'Player'):
        """
        Equip the armor
        """
        player.equip_armor(self)
        self.drop(player)


    