# from createCharacter import createCharacter
# from createMonster import createMonster
import os


def xp_after_combat(character, monster):
    character.gainXP(monster.xp_value)
    input("\nPress any button to continue\n")
    os.system('cls')


def show_combat(character, monster, combat_turn):
    """Mostra as estatísticas atuais do personagem e do inimigo"""
    print(f"***__COMBAT__*** Turn #{combat_turn}\n")
    character.showCharacter()
    print("***" * 3)
    print("")
    monster.showMonster()
    print("---" * 3)
    print("")


def is_dead(character, monster,  combat_cond):
    """Checa se o personagem ou monstro está morto, caso esteja,
    devolve a condição de combate como falso, e ele é encerrado"""
    if character.life <= 0:
        print("\nYou Died!\n")
        input("End combat")
        combat_cond = False
        return combat_cond
    if monster.life <= 0:
        print("\nMonster Die!\n")
        input("End combat")
        xp_after_combat(character, monster)
        combat_cond = False
        return combat_cond
    return combat_cond


def player_attack_turn(character, monster):
    """O personagem ataca o monstro, em acerto, causa dano"""
    attack_roll, damage = character.attackMonster()
    print(f"\nYou roll a {attack_roll}. ", end="")
    if attack_roll >= monster.status:
        print(f"You did {damage} damage.")
        monster.takeDamage(damage)
    else:
        print("You miss.")


def monster_attack_turn(character, monster):
    """O monstro ataca o personagem, em acerto, causa dano"""
    monster_attack_roll, monster_damage = monster.attackCharacter()
    print(f"\n{monster.monster_type} roll a {monster_attack_roll}. ", end="")
    if monster_attack_roll >= character.defense:
        print(f"You took {monster_damage}.")
        character.takeDamage(monster_damage)
    else:
        print(f"{monster.monster_type} miss.")


def runCombat(character, monster):

    combat_cond = True
    combat_turn = 1

    while combat_cond is True:
        os.system('cls')

        show_combat(character, monster, combat_turn)

        print("[ENTER] Attack | [1] Run | [2] Potion | [3] Skill: ")
        option = input("- ")

        if option == '1':
            os.system('cls')
            input("you ran from the fight!\n")
            combat_cond = False
        elif option == '2':
            character.useHeal()
            monster_attack_turn(character, monster)
            combat_cond = is_dead(character, monster, combat_cond)
            if not combat_cond:
                continue
        elif option == '3':
            if character.character_class == 'Warrior':
                character.useSkillWarrior()
                input("\nNext turn: ")
                continue
            elif character.character_class == 'Cleric':
                character.useSkillCleric()
            elif character.character_class == 'Thief':
                if character.useSkillThief():
                    monster.takeDamage(100)
                    combat_cond = is_dead(character, monster, combat_cond)
                    if not combat_cond:
                        continue
                else:
                    print("You dont have any skill points!")
            elif character.character_class == 'Mage':
                if character.useSkillMage():
                    player_attack_turn(character, monster)
                    player_attack_turn(character, monster)
                    player_attack_turn(character, monster)
                    combat_cond = is_dead(character, monster, combat_cond)
                    if not combat_cond:
                        continue
                else:
                    print('You dont have any skill points!')
            monster_attack_turn(character, monster)
            combat_cond = is_dead(character, monster, combat_cond)
            if not combat_cond:
                continue
        else:
            player_attack_turn(character, monster)
            combat_cond = is_dead(character, monster, combat_cond)
            if not combat_cond:
                continue
            monster_attack_turn(character, monster)
            combat_cond = is_dead(character, monster, combat_cond)
            if not combat_cond:
                continue

        if combat_cond:
            input("\nNext turn: ")
        os.system('cls')
