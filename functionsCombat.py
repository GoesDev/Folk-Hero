# from createCharacter import createCharacter
# from createMonster import createMonster
import os


def runCombat(character, monster):

    combat_cond = True
    # combat_log = []
    combat_turn = 1

    while combat_cond is True:
        os.system('cls')

        print(f"***__COMBAT__*** Turn #{combat_turn}")
        character.showCharacter()
        print("***" * 3)
        monster.showMonster()
        print("---" * 3)

        option = input("Attack [0] | Run [1]")

        if option == '0':
            attack_roll, damage = character.attackMonster()
            if attack_roll >= monster.status:
                print(f"\nYou did {damage} damage.")
                monster.takeDamage(damage)
                if monster.life <= 0:
                    print("Monster Die!")
                    input("End combat")
                    os.system('cls')
                    combat_cond = False
                    continue
                input("\nNext turn")
            else:
                print("You miss.")
                input("\nNext turn")
