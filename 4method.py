class Hero: # template
    jumlahHero = 0 # <-- class variable

    def __init__(self, inputName, inputHealth, inputAttack, inputArmour):
        self.name = inputName # <-- object/instance variable
        self.health = inputHealth
        self.attack = inputAttack
        self.armour = inputArmour
        Hero.jumlahHero += 1

    # 1-method = void function; method tanpa return dan tanpa argumen
    def siapa(self):
        print("namaku adalah "+ self.name)

    # 2-method dengan argumen, tanpa return
    def healthUp(self, Up):
        self.health += Up

    # 3-method dengan return
    def getHealth(self):
        return self.health

hero1 = Hero("sniper", 100, 10, 5)
hero2 = Hero("mario bros", 90, 5, 10)

hero1.siapa() # 1

hero1.healthUp(20) # 2
print(hero1.health) # 2

print(hero1.getHealth()) # 3