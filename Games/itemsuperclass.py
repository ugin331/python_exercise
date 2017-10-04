from tadvent import player
class item:
    def __init__(self, name, cost, id):
        self.name = name
        self.cost = cost
        self.id = id

class Weapon(item):
    def __init__(self, name, cost, atkbonus):
        item.__init__(self, name, cost)
        self.atkbonus = atkbonus

    def desc(self):
        print("name: "+ self.name + ", cost: " + self.cost + ", Stat boost: +" + self.atkbonus + " ATK")

    def equip(self, atkbonus):
        print("you pick up the sword, ready to destroy.")
        player.atk += atkbonus

class Armor(item):
    def __init__(self, name, cost, defbonus):
        item.__init__(self, name, cost)
        self.defbonus = defbonus

    def desc(self):
        print("name: "+ self.name + ", cost: " + self.cost + ", Stat boost: +" + self.defbonus + " DEF")

    def equip(self, defbonus):
        print("you equipped the armor. you feel stronger now.")
        player.armor += defbonus

class Potion(item):
    def __init__(self, name, cost, effect, str):
        item.__init__(self, name, cost)
        self.effect = effect
        self.str = str

    def desc(self):
        print("name: "+ self.name + ", cost: " + self.cost + ", Stat boost: +" + self.effect + " +" + self.str + " points")

    def use(self, effect, str):
        if effect == "ATK":
            player.atk += str
        elif effect == "DEF":
            player.armor +=str
        elif effect == "DED":
            player.hp -= str
            player.atk += str
            player.armor += str


testarmor = Armor("Dev Armor", 999999999999, 9001)
testweapon = Weapon("Dev Sword", 999999999999, 9001)
testatkpotion = Potion("ATK-9001 Dev Booster", 999999999999, "ATK", 9001)
testdefpotion = Potion("ULTDEF Dev Booster", 999999999999, "DEF", 9001)
testdedpotion = Potion("DED-Approved Dev Pill", 999999999999, "DED", 9001)