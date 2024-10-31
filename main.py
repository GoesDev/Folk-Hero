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
    os.system('cls')
    print("Folk Hero has four classes, choose one from the list below:")

    print("(0) Warrior | (1) Cleric | (2) Thief | (3) Mage")
    print('\nWARRIOR: Brave skill allows you to increase your Power ', end="")
    print('in exchange for your Defense. You 3 Max Life.')
    print('You intimidate your opponents and they lose their turn')
    print('\nCLERIC: Holy Magic skill allows you to heal ', end="")
    print("yourself in critical moments. The amount of healing is 10 + level.")
    print('\nTHIEF: Assassinate skill allows you to instantly kill enemies.')
    print('\nMAGE: Magic Missiles skill allows you to make 3 attacks ', end="")
    print('e gain 5 points of life.')
    chosen_class = input("\nClass: ")

    if chosen_class in ['0', '1', '2', '3']:
        new_character = createCharacter(
            hero_name, class_list[int(chosen_class)])
        class_option = True
    else:
        os.system('cls')
        input("Try again! ")

os.system('cls')
game_over = False


while game_over is False:

    new_monster = createMonster()

    print(">>> LOBBY <<<")
    new_character.showCharacter()
    print()
    new_dungeon.showDungeon()

    print("\nContinue to the next room? ([ENTER] Yes | [1] No | [2] Potion)  ")
    game_on = input('- ')
    if game_on == '1':
        os.system('cls')
        game_over = True
        break
    elif game_on == '2':
        os.system('cls')
        new_character.useHeal()
        input("- ")
        os.system('cls')
        continue

    os.system('cls')
    if new_dungeon.actual_room < new_dungeon.rooms_qtd:
        print(f"\nA {new_monster.monster_type} appers!")
        new_monster.showMonster()
        print("[ENTER] Fight | [1] Run\n")
        combat_choice = input()
        if combat_choice == '1':
            continue
        else:
            runCombat(new_character, new_monster)
            if new_character.life <= 0:
                os.system('cls')
                print("\nGAME OVER!")
                game_over = True
            else:
                new_dungeon.nextRoom()
    else:
        new_monster.iamBoss()
        print("Careful! You have entered the last room of the dungeon", end="")
        print(", get ready to face the Boss!")
        input('- ')
        print(f"\nA {new_monster.monster_type} appers!")
        new_monster.showMonster()
        input("[ENTER] Fight\n")
        runCombat(new_character, new_monster)
        if new_character.life <= 0:
            print("\nGAME OVER!")
            game_over = True
        else:
            print(">>> Congratulations!!! <<<")
            print(">>>    YOU   WIN!!     <<<")
            game_over = True
