from random import randint

dungeon_type = ['Temple', 'Ruins', 'Underground']


class createDungeon():

    def __init__(self):
        self.name = 'Catacombs of the Conquered Warrior'
        self.rooms_qtd = randint(10, 20)
        self.type = dungeon_type[randint(0, 2)]
        self.actual_room = 1

    def showDungeon(self):
        print(f"{self.name.title()}")
        print(f"Dungeon Type: {self.type}")
        print(f"Room #{self.actual_room}/{self.rooms_qtd}")

    def nextRoom(self):
        self.actual_room += 1
