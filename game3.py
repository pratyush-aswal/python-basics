class Place:
    def __init__(self):
        self.itemlist = []
        self.neighbours = []
        self.name = None
        self.north = None
        self.east = None
        self.west = None
        self.south = None

    def setName(self, name):
        self.name = name

    def direction(self, n, e, w, s):
        self.north = n
        self.east = e
        self.west = w
        self.south = s

    def getName(self):
        return self.name

    def setNeighbour(self, place):
        self.neighbours.append(place)

    def getNeighbours(self):
        return self.neighbours

    def removeitem(self, x):
        if x < self.itemlist.__len__():
            return self.itemlist.pop(x)

    def additem(self, x):
        self.itemlist.append(x)


class Game:
    def __init__(self):
        self.places = []

    def addplace(self, place):
        self.places.append(place)

    def setPath(self, place1, place2):
        place1.setNeighbour(place2)
        place2.setNeighbour(place1)

    def explore(self):
        for i in self.places:
            print(i.getName(), '-->')
            for x in i.getNeighbours():
                print('\t', x.getName())


class Man:
    def __init__(self, placeobj):
        self.inventory = []
        self.current = placeobj

    def move(self):
        print("Move:--")
        if (self.current.north.getName() != 'None') and (self.current.north in self.current.getNeighbours()):
            print('1: North - ', self.current.north.name)
        if (self.current.east.getName() != 'None') and (self.current.east in self.current.getNeighbours()):
            print('2: East - ', self.current.east.name)
        if (self.current.west.name != 'None') and (self.current.west in self.current.getNeighbours()):
            print('3: West - ', self.current.west.name)
        if (self.current.south.name != 'None') and (self.current.south in self.current.getNeighbours()):
            print('4: South - ', self.current.south.name)
        choice = int(input('enter direction to move'))
        if choice == 1:
            self.current = self.current.north
        elif choice == 2:
            self.current = self.current.east
        elif choice == 3:
            self.current = self.current.west
        elif choice == 4:
            self.current = self.current.south

    def look(self):
        print("north=", self.current.north.name)
        print("east=", self.current.east.name)
        print("west=", self.current.west.name)
        print("south=", self.current.south.name)

        print('door:')
        for i in self.current.getNeighbours():
            print(i.getName())

        print('Items : ')
        for i in self.current.itemlist:
            print(i)

    def pickup(self):
        print('Enter value to be picked up: ')
        for i in range(self.current.itemlist.__len__()):
            print(i + 1, ':', self.current.itemlist[i])

        inp = int(input())
        if inp != 0:
            self.inventory.append(self.current.itemlist[inp - 1])
            self.current.removeitem(inp - 1)

    def showinvent(self):
        print('Inventory List : ')
        for i in range(self.inventory.__len__()):
            print(i + 1, ':', self.inventory[i])

    def drop(self):
        print('Enter value to be dropped: ')
        for i in range(self.inventory.__len__()):
            print(i + 1, ':', self.inventory[i])

        inp = int(input())
        if inp != 0:
            self.current.additem(self.inventory[inp - 1])
            self.inventory.pop(inp - 1)


bed = Place()
bed.itemlist = ['bottle', 'all out']
bath = Place()
bath.itemlist = ['soap', 'shampoo']
dine = Place()
dine.itemlist = ['plate']
kitchen = Place()
kitchen.itemlist = ['knife', 'apple']

bed.setName('Bedroom')
bath.setName('Bathroom')
dine.setName('Dining Room')
kitchen.setName('Kitchen')

bed.direction(Place(), Place(), Place(), bath)
bath.direction(bed, dine, Place(), Place())
dine.direction(kitchen, Place(), bath, Place())
kitchen.direction(Place(), Place(), Place(), dine)

g = Game()
places = [bed, bath, dine, kitchen]
for x in places:
    g.addplace(x)

g.setPath(bed, bath)
g.setPath(dine, kitchen)

g.explore()

flag = 0
player = Man(bed)


def view():
    global flag
    print("-------------" * 3)
    print("current position :", player.current.getName())
    print('1: Look')
    print('2: Move')
    print('3: Pickup')
    print('4: Drop')
    print('5: Inventory')
    print('0: Exit')

    choice = int(input('Enter your choice'))
    if choice == 1:
        player.look()
    elif choice == 2:
        player.move()
    elif choice == 3:
        player.pickup()
    elif choice == 4:
        player.drop()
    elif choice == 5:
        player.showinvent()
    elif choice == 0:
        flag = 1


while flag == 0:
    view()
