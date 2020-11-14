class Item:
    """
    An item that can be used in an inventory
    """
    name: str
    description: str
    value: float

    def __init__(self, name: str, description: str, value: float):
        self.name = name
        self.description = description
        self.value = value
    
    def __repr__(self):
        return self.name

    def drop(self, player: 'Player'):
        """
        Drop the item.
        """
        player.inventory.remove(self)
    
    def use(self, player: 'Player'):
        """
        Interact with the item
        """
        raise NotImplementedError