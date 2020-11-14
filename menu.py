from player import Player
from utils import FixedList
from item import Item
import PySimpleGUI as sg

FONT_SIZE = 37

sg.theme("black")
STANDARD_FONT = font=("Consolas", 37)
sg.SetOptions(button_color=('#FFFFFF', '#444444'))
sg.SetOptions(font=("Consolas", 17))
sg.SetOptions(border_width=None)

class Menu:
    """
    The menu that the player opens. Can be used to access stats and inventory.
    """
    player: Player

    def __init__(self, player: Player):
        self.player = player
    
    def open(self):
        """
        Open the menu.
        """
        in_menu: bool = True
        while(in_menu):
            hp = f"HP: {self.player.hp}/{self.player.max_hp}".ljust(10)
            lv = f"LV: {self.player.lv}".ljust(10)
            name = self.player.name
            layout = [
                    [sg.Text(name)],
                    [sg.Text(lv)],
                    [sg.Text(hp)],
                    [sg.Button("Items", key="ITEMS", size=(10, 1))],
                    [sg.Button("Stats", key="STATS", border_width=0, size=(10, 1))],
                    [sg.Button("Exit", size=(10, 1), button_color=("#edf2ce", "#444444"))]
            ]
            window = sg.Window("Menu", layout, size=(200, 300), element_justification='c')
            choice = window.read()[0]
            window.close()

            if choice == "ITEMS":
                self.open_inv()
            elif choice == "STATS":
                self.open_stat()
            else:
                return
    
    def open_stat(self):
        """
        Open the stat menu
        """
        hp = f"HP: {self.player.hp}/{self.player.max_hp}".ljust(10)
        lv = f"LV: {self.player.lv}".ljust(10)
        name = self.player.name
        layout = [
                [sg.Text(f'"{name}"')],
                [sg.Text(lv)],
                [sg.Text(hp)],
                [sg.Button("Exit", size=(10, 1), button_color=("#edf2ce", "#444444"))]
            ]
        window = sg.Window("Stats", layout, size=(250, 500), element_justification='c')
        window.read()
        window.close()

    def open_inv(self):
        """
        Open the inventory
        """
        in_menu: bool = True
        while(in_menu):
            selected_item = self.item_select()
            if selected_item != None:
                self.open_item(selected_item)
            else:
                return

    def item_select(self):
        """
        Select an item from the inventory
        """
        layout = [[sg.Text("Inventory:", border_width=0)]]
        for i, item in enumerate(self.player.inventory):
            layout.append([sg.Button(item, key=i, size=(10, 1), border_width=0)])
        layout.append([sg.Button("Exit", key="EXIT", size=(10, 1), button_color=("#edf2ce", "#444444"))])
        window = sg.Window("Inventory Viewer", layout, size=(200, 500), element_justification='c')
        choice = window.read()[0]
        window.close()
        if choice is None:
            return None
        if choice == "EXIT":
            return None
        else:
            print(choice)
            return self.player.inventory[choice]
    
    def open_item(self, item: Item):
        """
        Prompt when the player opens the inventory
        """
        choice: int
        layout = [  [sg.Text(item.name, border_width=0)],
                    [sg.Text(item.description, border_width=0)],
                    [sg.Text("Value: $" + str(item.value), border_width=0)],
                    [sg.Button("Use", key="USE", border_width=0)],
                    [sg.Button("Drop", key="DROP", border_width=0)],
                    [sg.Button("Exit", key="EXIT", border_width=0)], ]
        
        window = sg.Window("Item Viewer", layout, size=(len(item.description)*STANDARD_FONT[1]//2 + 50, 300), keep_on_top=True, element_justification='c')
        choice = window.read()[0]
        window.close()
        if(choice == "USE"):
            item.use(self.player)
        elif(choice == "DROP"):
            item.drop(player)
    
