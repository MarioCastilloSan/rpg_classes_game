#Create players
from warrior import Warrior
from mage import Mage
from thieve import Thieve
from typing import List


warrior = Warrior("Grom Hellscream", 1, 100, 0, 10, 5, 1, 0)
mage = Mage("Jaina Proudmoore", 1, 50, 100, 1, 5, 10, "Frost", 5)
thieve = Thieve("Valeera Sanguinar", 1, 75, 50, 1, 10, 5, 10)


#Attack
#Estado del mago pre ataque
print(mage.get_stats())
#guerruero ataca al mago
mage.reduce_health(warrior.attack(opponent=mage))
print(mage.get_stats())



#Estado del guerrero pre ataque
print(warrior.get_stats())
#mago ataca al guerruero
warrior.reduce_health(mage.attack(opponent=warrior))
print(warrior.get_stats())


#Estado del ladron pre ataque
print(thieve.get_stats())
#mago ataca al ladron
thieve.reduce_health(mage.attack(opponent=thieve))
print(thieve.get_stats())





