class HERO: #class = template
    pass


hero1 = HERO() #object/instance (instantiate)
hero2 = HERO()
hero3 = HERO();

hero1.name = "sniper"
hero1.health = 100

hero2.name = "sven"
hero2.health = 200

hero3.name = "ucup"
hero3.name = 1000

print(hero1)
print(hero1.__dict__) #dict = dictionary
print(hero1.name)