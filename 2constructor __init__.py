class Hero:
    #__init__ = initialitation
    def __init__(self, inputName, inputHealth, inputPower, inputArmour): #self = hero1/hero2/hero3
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armour = inputArmour

hero1 = Hero("sniper", 100, 10, 4)
hero2 = Hero("miranda", 100, 15, 1)
hero3 = Hero("sniper", 1000, 100, 0)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
    