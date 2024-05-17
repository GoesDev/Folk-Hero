from random import randint

monster_type = ["Goblin", "Kobold", "Skeleton"]


class createMonster():

    def __init__(self) -> None:
        self.monster_type = monster_type[randint(0, 2)]
        self.m_level = randint(1, 3)
        self.life = self.m_level * 5
        self.life_max = self.life
        self.status = randint(1, 3) * self.m_level

    def showMonster(self):
        print(f"Monster: {self.monster_type} | Level: {self.m_level}")
        print(f"Life: {self.life}/{self.life_max}")

    def attackCharacter(self):
        attack_roll = randint(1, 12) + (self.status // 3)
        damage = randint(1, 8) + self.m_level
        return attack_roll, damage

    def takeDamage(self, damage):
        self.life -= damage
