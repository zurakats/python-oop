class Hero: # template
    jumlah = 0 # class variabel


    def __init__(self, inputName, inputHealth, inputAttack, inputArmour):
        # instance variabel
        self.name = inputName
        self.health = inputHealth
        self.attack = inputAttack
        self.defense = inputArmour
        Hero.jumlah += 1
        print("membuat hero dengan nama", inputName)

hero1 = Hero("sniper", 100, 10, 4)
print(Hero.jumlah)
hero2 = Hero("miranda", 100, 15, 1)
print(Hero.jumlah)
hero3 = Hero("ucup", 1000, 100, 0)
print(Hero.jumlah)