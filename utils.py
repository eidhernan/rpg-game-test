from items import Item

class FixedList:
    """
    A list of fixed size
    """
    size: int
    fill: any
    items: list

    def __init__(self, size: int, fill: any):
        self.size = size
        self.fill = fill
        self.items = [fill for i in range(size+1)]
    
    def __getitem__(self, i):
        if(i in range(self.size)):
            return self.items[i]
        else:
            raise IndexError("FixedList index out of range. Range: " + str(i))
    
    def __setitem__(self, i, v):
        if(i in range(self.size)):
            self.items[i] = v
        else:
            raise IndexError("FixedList index out of range. Range: " + str(i))

    def __repr__(self):
        return repr(self.items)

    def append(self, v):
        for i in range(len(self.items)):
            if(self.items[i].name == self.fill.name):
                self.__setitem__(i, v)
                break
    
    def pop(self, i):
        self.items.pop(i)
        self.items.append(self.fill)
    
    def remove(self, v):
        self.items.remove(v)
        self.items.append(self.fill)

if __name__ == "__main__":
    inventory = FixedList(4, Item("Blank", "", 0))