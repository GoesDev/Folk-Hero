from createCharacter import createCharacter
from createMonster import createMonster
import os
os.system('cls')

print("Hello! Welcome to Folk Hero!")
print("Folk Hero is a text-based RPG.\n\n")

# Criando o personagem

hero_name = input(
    "Let's make your character.\nFirst, what is your Hero name: ")
os.system('cls')

class_list = ["Warrior", "Cleric", "Thief", "Mage"]
class_option = False

while class_option is False:

    print("Folk Hero has four classes, choose one from the list below:")

    print("(0) Warrior | (1) Cleric | (2) Thief | (3) Mage")
    chosen_class = int(input("Class: "))

    if chosen_class >= 0 and chosen_class <= 3:
        new_character = createCharacter(hero_name, class_list[chosen_class])
        class_option = True
    else:
        os.system('cls')
        print("Try again!")

os.system('cls')
game_over = False

new_monster = createMonster()

while game_over is False:

    new_character.showCharacter()

    game_on = input("\nContinue to the next room? (Y/N)  ")
    if game_on.lower() == 'y':
        os.system('cls')

        print(f"A {new_monster.monster_type} appers!")
        new_monster.showMonster()
        print("[0] Fight | [1] Run")
        input()
    elif game_on.lower() == 'n':
        os.system('cls')
        game_over = True
    else:
        print("Invalid option.")
