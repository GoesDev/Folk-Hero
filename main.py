from createCharacter import createCharacter
from createMonster import createMonster
from createDungeon import createDungeon
from functionsCombat import runCombat

import os
os.system('cls')

new_dungeon = createDungeon()

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
    chosen_class = input("Class: ")

    if chosen_class in ['0', '1', '2', '3']:
        new_character = createCharacter(
            hero_name, class_list[int(chosen_class)])
        class_option = True
    else:
        os.system('cls')
        print("Try again!")

os.system('cls')
game_over = False


while game_over is False:

    new_monster = createMonster()

    new_character.showCharacter()
    print()
    new_dungeon.showDungeon()

    game_on = input("\nContinue to the next room? (Y/N)  ")
    if game_on.lower() == 'y':
        pass
    elif game_on.lower() == 'n':
        os.system('cls')
        game_over = True
        break
    else:
        os.system('cls')
        print("Invalid option. Try Again!\n")
        continue

    print(f"\nA {new_monster.monster_type} appers!")
    new_monster.showMonster()
    print("[0] Fight | [1] Run\n")
    combat_choice = input()
    if combat_choice == '0':
        runCombat(new_character, new_monster)
        if new_character.life <= 0:
            print("\nGamer Over!")
            game_over = True

    new_dungeon.nextRoom()
