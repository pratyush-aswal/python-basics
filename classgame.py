class Room:
    itemlist = []
    name = ''

    def __init__(self, nm):
        self.north = None
        self.east = None
        self.west = None
        self.south = None
        self.name = nm

    def direction(self, n, e, w, s):
        self.north = n
        self.east = e
        self.west = w
        self.south = s

    def removeitem(self, x):
        if x < self.itemlist.__len__():
            return self.itemlist.pop(x)

    def additem(self, x):
        self.itemlist.append(x)


class Man:
    inventory = []

    def __init__(self, roomobj):
        self.current = roomobj

    def move(self):
        print("Move:--")
        if self.current.north.name != 'None':
            print('1: North - ', self.current.north.name)
        if self.current.east.name != 'None':
            print('2: East - ', self.current.east.name)
        if self.current.west.name != 'None':
            print('3: West - ', self.current.west.name)
        if self.current.south.name != 'None':
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

    def pickup(self):
        print('enter value to be picked up')
        for i in range(self.current.itemlist.__len__()):
            print((i + 1), ":", self.current.itemlist[i])
        inp = int(input())
        if inp != 0:
            self.inventory.append(self.current.itemlist[inp - 1])
            self.current.removeitem(inp - 1)

    def showinvent(self):
        for i in range(self.inventory.__len__()):
            print((i + 1), ":", self.inventory[i])

    def drop(self):
        print('enter value to be dropped')
        for i in range(self.inventory.__len__()):
            print((i + 1), ":", self.inventory[i])
        inp = int(input())
        if inp != 0:
            st = self.inventory.pop(inp - 1)
            self.current.additem(st)


road = Room('road')
road.itemlist = []

lawn = Room('lawn')
lawn.itemlist = ['grass', 'lawnmower']

garage = Room('garage')
garage.itemlist = ['jack', 'tyre']

hall = Room('hall')
hall.itemlist = ['book', 'pen']

dining = Room('dining')
dining.itemlist = ['plate', 'spoon']

bedroom = Room('bedroom')
bedroom.itemlist = ['shirt', 'wallet']

store = Room('store')
store.itemlist = ['screwdriver']

gym = Room('gym')
gym.itemlist = ['bag', 'mat']

kitchen = Room('kitchen')
kitchen.itemlist = ['knife', 'apple']

road.direction(lawn, Room('None'), Room('None'), Room('None'))
lawn.direction(hall, garage, Room('None'), road)
garage.direction(dining, Room('None'), lawn, Room('None'))
hall.direction(gym, dining, bedroom, lawn)
dining.direction(kitchen, Room('None'), hall, garage)
kitchen.direction(Room('None'), Room('None'), gym, dining)
gym.direction(Room('None'), kitchen, store, hall)
store.direction(Room('None'), gym, Room('None'), bedroom)
bedroom.direction(store, hall, Room('None'), Room('None'))

player = Man(road)
flag = 0


def view():
    global flag
    print("-------------" * 3)
    print("current position :", player.current.name)
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
