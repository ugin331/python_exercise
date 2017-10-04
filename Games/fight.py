import random
from tadvent import checkvalid, attack
def turnbasedfighting(enemy, protag):
    while True:
        while True:
            print("A(n) " + enemy.name + " appeared!")
            print("""You have two options:
    1. Fight
    2. Run
    """)
            choice = input("What will you do? ")
            checkvalid(int(choice))
            if checkvalid(int(choice)) == True:
                break
        lel = int(choice)
        if lel == 1:
            multiplemoves(protag, enemy)
            if enemy.hp == 0:
                print("the "+ enemy.name + " was defeated!")
                break
            else:
                enemyattack = attack(enemy.attack)
                protag.hp -= enemyattack
        elif lel == 2:
            chances = random.randint(10)
            if chances >= 3:
                print("you fled!")
                break

def multiplemoves(protag, enemy):
    print("""which attack?
1. Basic Attack
2. Less Basic Attack
3. LELLLLLLLLLLLLLLL""")
    while True:
        selection = input("???")
        checkvalid(int(selection))
        if checkvalid(int(selection)) == True:
            break
    selecnum = int(selection)
    if selecnum == 1:
        print("you punched your enemy!")
        attackpower = attack(protag.attack)
        enemy.hp -= attackpower
        print(attackpower + " damage!")
    elif selecnum == 2:
        print("you attacked with a low, sweeping kick!")
        attackpower = attack(protag.attack + protag.attackmods[selecnum - 2])
        enemy.hp -= attackpower
        print(attackpower + " damage!")
    elif selecnum == 3:
        print("you attacked with the power of the lel!")
        attackpower = attack(protag.attack + protag.attackmods[selecnum - 2])
        enemy.hp -= attackpower
        print(attackpower+ " damage!")