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
        self.heal_uses = 3
        self.skill_uses = 3

    def showCharacter(self):
        print(f"Character: {self.character_name} | Level: {self.level}")
        print(f"Class: {self.character_class}")
        print(f"Life Poins: {self.life}/{self.life_max}")
        print(f"Power: {self.power} [+{self.power // 3}] ", end="")
        print(f"| Defense: {self.defense}")
        print(f"XP: {self.xp_points}/{self.xp_to_next_level}")
        print(f"Skill Uses: {self.skill_uses} | Potion: {self.heal_uses}")

    def levelUp(self):
        self.level += 1
        self.power += randint(1, 3)
        self.defense += randint(1, 3)
        self.life_max += 5
        self.xp_to_next_level *= 2
        self.life = self.life_max
        if self.skill_uses < 3:
            self.skill_uses += 1

    def gainXP(self, xp_earned):
        os.system('cls')
        self.xp_points += xp_earned
        print(f">>> You received {xp_earned} XP <<<\n")
        if self.xp_points >= self.xp_to_next_level:
            print("Congratulations! You earned a level!\n")
            self.levelUp()

    def attackMonster(self):
        attack_roll = randint(1, 12) + (self.power // 3)
        damage = randint(1, 8) + self.level
        return attack_roll, damage

    def takeDamage(self, damage):
        self.life -= damage

    def useHeal(self):
        if self.heal_uses > 0:
            self.heal_uses -= 1
            heal = randint(1, 8) + self.level
            self.life += heal
            print(f'You restored {heal} health points!')
            if self.life > self.life_max:
                self.life = self.life_max
        else:
            print('You have no healing potion available')

    def useSkillWarrior(self):
        if self.skill_uses > 0:
            print("Using BRAVE skill!")
            self.skill_uses -= 1
            new_power = randint(1, 3)
            new_defense = randint(1, 2)
            self.power += new_power
            self.defense -= new_defense
            self.life_max += 3
            print(f'Your POWER increases by [{new_power}] !')
            print(f'Your DEFENSE has dropped by [{new_defense}] !')
            print(f'Your MAX LIFE increases by {3}')
            print('Enemy is intimidated and does not attack')
        else:
            print("You dont have any skill points!")

    def useSkillCleric(self):
        if self.skill_uses > 0:
            print("Using HOLY MAGIC skill!")
            self.skill_uses -= 1
            self.life += 10 + self.level
            print(f'You restored {10 + self.level} health points!')
            if self.life > self.life_max:
                self.life = self.life_max
        else:
            print("You dont have any skill points!")

    def useSkillThief(self):
        if self.skill_uses > 0:
            print('Using ASSASSINATE skill')
            self.skill_uses -= 1
            return True

    def useSkillMage(self):
        if self.skill_uses > 0:
            self.skill_uses -= 1
            self.life += 5
            print('Using MAGIC MISSILE skill! you gain 5 points of life')
            self.life += 5
            if self.life > self.life_max:
                self.life = self.life_max
            return True
