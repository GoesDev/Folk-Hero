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
            print(f"\nYou roll a {attack_roll}. ", end="")
            if attack_roll >= monster.status:
                print(f"You did {damage} damage.")
                monster.takeDamage(damage)
                if monster.life <= 0:
                    print("Monster Die!")
                    input("End combat")
                    os.system('cls')
                    combat_cond = False
                    continue
            else:
                print("You miss.")

            monster_attack_roll, monster_damage = monster.attackCharacter()
            print(f"\n{monster.monster_type} roll a {monster_attack_roll}. ",
                  end="")
            if monster_attack_roll >= character.defense:
                print(f"You took {monster_damage}.")
                character.takeDamage(monster_damage)
                if character.life <= 0:
                    print("You died")
                    input("End combat")
                    os.system("cls")
                    combat_cond = False
                    continue
            else:
                print(f"{monster.monster_type} miss.")

            input("\nNext turn")
