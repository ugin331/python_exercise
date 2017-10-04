#import items as items
# y dis no work??
#import itemsuperclass as item
"""

READ THIS: CTRL-SHIFT-F10 to run BUTTON NO WORK FOR SOME REASON

TO DO LIST:
1. Add items, and implement an item dictionary as well as stats
    1a. IMPLEMENT TURN-BASED BATTLING
2. more enemies. a simple example enemy won't cut it.
3. more items, such as potions.
4. A class system?
5. more locations(finish tavern, etc.)
6. ways to spend gold.
7. stop being a lazy bum
8. make a real time tracker of all the armor and equipment you have on.
9. ducks :) <-- Faye
10. move everything to items, then begin the torturous process of converting everything into items.xxxx :\ rip
:( :( :( :( :(
"""

import random
import sys
import multiprocessing
#possible location class
class Place:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def texties(self):
        raise NotImplementedError
    def modchar(self):
        raise NotImplementedError

class Testroom(Place):
    def texties(self):
        print("you are in a room. This is a test.")
    def modchar(self):
        pass
#player class
class Player:
    hp = 100
    armor = 0
    atk = 2
    cash = 0
    speed = 10
    mana = 0
    inventory = []
    equipment = [0, 0, 0, 0], [0, 0]
    moves = ["basic attack", "other attack", "lol"]
    attackmods = [1, 2]
    def ded(self):
        while True:
            if self.hp <= 0:
                sys.exit(1)
player = Player

#enemy classes
class Enemy:
    name = "enemy"
    hp = 99999999999999999999999999
    armor = 99999999999999999999999
    attack = 9999999999999999999999
    speed = 99999999999999999999999
    drops = 0
    dropchance = 0
    def dropitem(self):
        dropcounter = random.randint(1, 100)
        if self.hp<=0:
            if dropcounter <= self.dropchance:
                print("the defeated " + self.name + " dropped an item! added to your inventory!")
                player.inventory.append(self.drops)
    fleechance = 999999999999999999 #value from 0 - 20 that shows whether or not the enemy flees from battle, where 20 is almost always
#basic example enemy
enemy = Enemy
enemy.hp = 10
enemy.armor = 0
enemy.attack = 1
enemy.speed = 0 #value not implemented
enemy.drops = 1
enemy.dropchance = 20 #value out of 100 tells you how often the item can drop
enemy.name = "example enemy"
enemy.fleechance = 5
#shadytrader(not added)
shadydealer = Enemy
enemy.hp = 70
enemy.armor = 5
enemy.attack = 5
enemy.speed = 2
enemy.name = "Shady Trader"
enemy.fleechance = 0

#item classes
class weapon:
    atkboost = 0
    speed = 0
    cost = 0
    sell = 0
    durability = 0
#trollsword
leethaxxorpwnersword = weapon
leethaxxorpwnersword.atkboost = -2
#basicsword
basicsword = weapon
basicsword.atkboost = 3
basicsword.cost = 30
basicsword.sell = 15
basicsword.durability = 250
class potion:
    hpboost = 0
    cost = 0
    sell = 0
'''weaponlist = {"a": "1337 h@Xx0R Sw0Rd", "b": "none", "c": "BSwordII", "d": "adventurer's staff"}
armorlist = {0 : "none", 1: "cloth tunic", 2: "padded cloth armor", 9999999: "oily toupee"}'''
equipment:{
    "weapons":{-1: "1337 h@Xx0R Sw0Rd", 0: "none", 1: "BSwordII", 2: "adventurer's staff"},
    "armor":{0 : "none", 1: "cloth tunic", 2: "padded cloth armor", 9999999: "oily toupee"}
}
"""
this is the equipment of the character: [0, 0, 0, 0], [0, 0]
first bar shows armor, with the slots being head, chest, legs, and feet respectively.
the second bar is weapons, and the slots are weapon and shields, respectively.
the numbers represent what item it is, based on a dictionary
    NOTE: NUMBERS ARE ARMOR PIECES, LETTERS ARE WEAPONS
"""
#-----------------------------------------------------------------------------------------------------------------------
#other defs
def checkvalid(num):
    if num.isdigit():
        nummer = int(num)
        if 4 >= nummer >= 1:
            return True
    else:
        if num == "e":
            accessinv(player)
        else:
            print("i dont understand that command...")
def checkifdead(unit):
    if unit.hp == 0:
        print("GAME OVER... YOU DIED")
        sys.exit(0)
def buythings(gold, cost):
    gold -= cost
def checkamount():
    print("you have " +str(player.hp)+ " hp left!")
    print("you have " + str(player.cash) + " gold left!")

#battle definitions
def attack(atk):
    updown = random.randint(1,3)
    if updown == 1:
        return round(atk + 0.2*atk)
    elif updown == 2:
        return round(atk - 0.2*atk)
    else:
        return atk
def battlescene(enemy):
    print("a wild "+enemy.name+" appeared!")
    print('''*************************
*         FIGHT         *
*************************''')
    while True:
        flee = random.randint(1, 20)
        if player.hp>0 and enemy.hp>0:
            playerattack = attack(player.atk)
            enemyattack = attack(enemy.attack)
            print("\nplayer attacked for " + str(playerattack) + " damage!")
            enemy.hp -= playerattack
            print("\nenemy has " + str(enemy.hp) + " health left!")
            print("\nenemy attacked for " + str(enemyattack) + " damage!")
            player.hp -= enemyattack
            print("\nplayer has " + str(player.hp) + " health left!")
            if flee < enemy.fleechance:
                print("the "+enemy.name+" fled!")
                break
        elif enemy.hp <= 0:
            print("you win!")
            break
        elif player.hp<=0:
            print("GAME OVER")
            break
def checkforenemy(chance, enemy): #chance is the 1 out of chance chance <-- lel that an enemy will spawn.
    enemyappear = random.randint(1, chance)
    if enemyappear == chance:
        battlescene(enemy)
def accessinv(player):
    while True:
        print(player.inventory)
        invact = input("to equip equipment, type e! to leave, type b! response: ")
        if "e" in invact:
            while True:
                equipstuff = input("which item would you like to equip? ")
                if equipstuff in player.inventory:
                    break
                else:
                    print("you do not own that item")
            if equipstuff.isdigit:
                player.equipment[0][0] = equipstuff
            else:
                player.equipment[1][0] = equipstuff
            player.inventory.remove(equipstuff)
        elif "b" in invact:
            break
#location functions
#this one is the example location function
def exampleplace():
    print('''exampletext exampletext exampletext exampletext exampletext exampletext
    exampletext exampletext exampletext
    Will you:
    1. exampletext.
    2. exampletext.
    3. exampletext.
    4. exampletext.''')
    while True:
        inp = input("what will you do? ")
        checkvalid(inp)
        if checkvalid(inp) == True:
            break
    print(inp)
    inper = int(inp)
    if inper == 1:
        print("exampletext")
        #some place here
    elif inper == 2:
        print("exampletext")
        #some place here
    elif inper == 3:
        print("exampletext")
        #some place here
    elif inper == 4:
        print("exampletext")
        #some place here
def htown():
    print('''you are in a small town. there is a path leading to the left and right,
and there is a tavern ahead and behind you. there is a weapons shop as well.
    Will you:
    1. go down the left path.
    2. go down the right path.
    3. go into the tavern.
    4. go into the weapons shop.''')
    while True:
        inp = input("what will you do? ")
        checkvalid(inp)
        if checkvalid(inp) == True:
            break
    print(inp)
    inper = int(inp)
    if inper == 1:
        print("you head down the left path.")
        leftpath()
    elif inper == 2:
        print("you head down the right path.")
        rightpath()
    elif inper == 3:
        print("this does nothing for now...")
        #tavern()
    elif inper == 4:
        print("you enter the shop.")
        weaponshop()
def rightpath():
    print('''you are on the right path. by now, the town is far behind you.
the grass rustles with the wind. In the distance, rocky bluffs can be seen. Something shines on
the horizon.
    Will you:
    1. continue onto the bluffs.
    2. explore the grass.
    3. go towards the shining object.
    4. go back to the town.''')
    while True:
        inp = input("what will you do? ")
        checkvalid(inp)
        if checkvalid(inp) == True:
            break
    print(inp)
    inper = int(inp)
    if inper == 1:
        print("you continue down the path. suddenly, you hear a rumbling, and\n you look up just in time to be crushed by a rock.")
        #some place here
    elif inper == 2:
        print("you head out into the grass.")
        checkforenemy(20, enemy)
    elif inper == 3:
        print("exampletext")
        #some place here
    elif inper == 4:
        print("you go back to the town, wasting even more time in \nyour already short existence. good job.")
        htown()
def weaponshop():
    print('''you enter the shady weapons shop. swords of various kinds are on the wall.
you notice a back door behind the owner, who eyes your money greedily.
    Will you:
    1. buy items
    2. sell items
    3. examine the back room
    4. leave''')
    while True:
        inp = input("what will you do? ")
        checkvalid(inp)
        if checkvalid(inp) == True:
            break
    print(inp)
    inper = int(inp)
    if inper == 1:
        print("you approach the dealer, and ask for his wares.")
        print('''his wares are as follows:
        1. nothing - 0 gold
        2. nothing - 0 gold
        3. nothing - 0 gold
        4. 1337_h@Xx0r_PwNr_Sw0rd - 0 gold''')
        while True:
            inpw = input("what will you buy? ")
            checkvalid(inpw)
            if checkvalid(inpw) == True:
                break
        inpwer = int(inpw)
        if inpwer == 1:
            print("you bought 1x item!")
            #buythings(player.cash, 50)
            checkamount()
            weaponshop()
        elif inpwer == 2:
            print("nothing happens. then, you realize that you are missing all your cash!")
            #buythings(player.cash, 50)
            checkamount()
            weaponshop()
        elif inpwer == 3:
            print("nothing happens. then, you realize that you are missing all your cash!")
            #buythings(player.cash, 50)
            checkamount()
            weaponshop()
        elif inpwer == 4:
            buythings(player.cash, leethaxxorpwnersword.cost)
            print('''
░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░
░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░
░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░
░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░
░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░
█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█
█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█
░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░
░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░
░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░
░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░
░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░
░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░
░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░
░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░
            ''')
            sys.exit(0)
    elif inper == 2:
        print('''
        The programmer is too lazy to add this right now.
        Z z
           Z z
              Z''')
        #some place here
    elif inper == 3:
        print("the shady guy stops you, and sends you out the door.\nsomething tells you that he is hiding something.")
        htown()
    elif inper == 4:
        print("you walk outside. the trader looks dissappointed.")
        htown()
def leftpath():
    print('''you are on a small path. the town is behind you. there may be monsters here...
the path continues towards the horizon. there is tall grass on either side.
    Will you:
    1. keep going down the left path.
    2. go down the right path, back to the town.
    3. go into the wilds.
    4. go to the forest.''')
    while True:
        inp = input("what will you do? ")
        checkvalid(inp)
        if checkvalid(inp) == True:
            break
    print(inp)
    inper = int(inp)
    checkforenemy(30, enemy)
    if inper == 1:
        print("you don't go very far before coming to an impassable ravine. you head back.")
        leftpath()
    elif inper == 2:
        print("you head back, and wonder why you even bothered to to the path.")
        htown()
    elif inper == 3:
        print("you head on towards the wilds, stepping carefully to not fall into holes.")
        wilds()
    elif inper == 4:
        if equip[0][0] != 0:
            print("it really isn't a good idea to go there without a weapon!")
            leftpath()
        else:
            print('''there is a sign at the edge of the forest. It says:
    ****************************
    **   The developer hasn't **
    ** implemented this yet,  **
    **     the lazy bum!      **
    ****************************
              ********
              ********
    you head back to the path.


    ... time passes ...''')
            leftpath()
            #forest()
def wilds():
    print('''you are surrounded with tall grasses. it ripples with the wind.
    Will you:
    1. walk around
    2. enjoy the sun
    3. do nothing
    4. go back to the path''')
    while True:
        inp = input("what will you do? ")
        checkvalid(inp)
        if checkvalid(inp) == True:
            break
    print(inp)
    inper = int(inp)
    if inper == 1:
        print("you walk around, noting the many claw marks in the ground.")
        checkforenemy(3, enemy)
    elif inper == 2:
        print("you enjoy the sun. it is warm on your skin, and you fall asleep. you wake up, and realize this all was a dream.")
    elif inper == 3:
        print("this really is a waste of time, isn't it? you think, and walk back to the path.")
        leftpath()
    elif inper == 4:
        print("you attempt to find the path again, but to your dismay, you cannot find it anymore! you starve and die in the wild.")
        player.hp = 0

print('''*********
*Welcome*
*********
a text adventure coded by WHOA
________BETA VERSION________
a lot of things don't exactly work, so kind of poke around.
If you come to a dead end, restart the game.
Things that do not work:
1. HomeTown:
    a. Right Path --> unimplemented
    b. Tavern --> unimplemented
    c. Weaponshop --> Currently under reconstruction
2. Left Path:
    a. Forest --> unimplemented
    b. Left Path(cont.) --> dead end
3. Wilds:
    a. sleeping --> kills you
    b. wandering around --> kills you

________CHANGELOG________
7/12/17: v0.0.15 implemented
    - item system changed
        - use a superclass instead
        - for easier coding
    - added MOAR bugs
''')
#the multirunning to check if the game is over or not and if you are D-E-D ded!
if __name__ == '__main__':
    p1 = multiprocessing.Process(name='p1', target=htown())
    p = multiprocessing.Process(name='p', target=checkifdead(player))
    p1.start()
    p.start()