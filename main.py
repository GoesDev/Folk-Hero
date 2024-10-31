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
    print("\nWARRIOR:The warrior has the highest Power and Defense statistics")
    print('His Brave technique allows him to increase his physical power')
    print('in exchange for reducing his defense.')
    print('\nCLERIC: The Cleric has balanced statistics,')
    print('and his Holy Magic allows him to heal in critical moments.')
    print('\nTHIEF: The Rogue also has balanced statistics,')
    print('and his Assassinate technique')
    print('allows him to defeat enemies instantly.')
    print('\nMAGE: The Mage has low stats, but has more uses for his skills.')
    print('Your Magic Missiles spell performs three attacks.')
    chosen_class = input("\nClass: ")

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

    print(">>> LOBBY <<<")
    new_character.showCharacter()
    print()
    new_dungeon.showDungeon()

    game_on = input("\nContinue to the next room? ([ENTER] Yes | [1] No)  ")
    if game_on == '1':
        os.system('cls')
        game_over = True
        break
    os.system('cls')
    print(f"\nA {new_monster.monster_type} appers!")
    new_monster.showMonster()
    print("[ENTER] Fight | [1] Run\n")
    combat_choice = input()
    if combat_choice == '1':
        continue
    else:
        runCombat(new_character, new_monster)
        if new_character.life <= 0:
            print("\nGAME OVER!")
            game_over = True
        elif new_dungeon.actual_room >= new_dungeon.rooms_qtd:
            print(">>> Congratulations!!! <<<")
            print(">>>    YOU   WIN!!     <<<")
            game_over = True
        else:
            new_dungeon.nextRoom()
