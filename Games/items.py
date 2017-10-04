#player class
class Player:
    hp = 100
    armor = 0
    atk = 2
    cash = 50
    speed = 10
    mana = 0
    inventory = ["nothing in here!"]
player = Player

#enemy classes
class Enemy:
    name = "enemy"
    hp = 99999999999999999999999999
    armor = 99999999999999999999999
    attack = 9999999999999999999999
    speed = 99999999999999999999999
    drops = "nothing for now"
    fleechance = 999999999999999999 #value from 0 - 20 that shows whether or not the enemy flees from battle, where 20 is almost always
#basic example enemy
enemy = Enemy
enemy.hp = 10
enemy.armor = 0
enemy.attack = 1
enemy.speed = 0 #value not implemented
enemy.drops = "nothing"
enemy.name = "example enemy"
enemy.fleechance = 5
#enemy 2
shadydealer = Enemy
enemy.hp = 70
enemy.armor = 5
enemy.attack = 5
enemy.speed = 2
#enemy drops oily toupee 9999999
enemy.name = "Shady Trader"
enemy.fleechance = 0
class lel:
    lel = "lel"
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