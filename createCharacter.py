from random import randint
import os


class createCharacter():

    def __init__(self, character_name, character_class) -> None:
        self.character_name = character_name.title()
        self.character_class = character_class
        self.level = 1
        self.life = 10
        self.power = randint(6, 10)
        self.defense = randint(6, 10)
        self.life_max = self.life
        self.xp_points = 0
        self.xp_to_next_level = 100

    def showCharacter(self):
        print(f"Character: {self.character_name} | Level: {self.level}")
        print(f"Class: {self.character_class}")
        print(f"Life Poins: {self.life}/{self.life_max}")
        print(f"Power: {self.power} | Defense: {self.defense}")
        print(f"XP: {self.xp_points}/{self.xp_to_next_level}")

    def levelUp(self):
        self.level += 1
        self.power += randint(1, 3)
        self.defense += randint(1, 3)
        self.life_max += 5
        self.xp_to_next_level *= 2

    def gainXP(self, xp_earned):
        os.system('cls')
        self.xp_points += xp_earned
        print(f"You received {xp_earned}\n")
        if self.xp_points > self.xp_to_next_level:
            print("Congratulations! You earned a level!\n")
            self.levelUp()
        self.showCharacter()
