from random import randint

monster_type = ["Goblin", "Kobold", "Skeleton"]


class createMonster():

    def __init__(self) -> None:
        self.monster_type = monster_type[randint(0, 2)]
        self.m_level = randint(1, 3)
        self.life = self.m_level * 5

    def showMonster(self):
        print(f"Monster: {self.monster_type}")
        print(f"Level: {self.m_level} | Life: {self.life}")
