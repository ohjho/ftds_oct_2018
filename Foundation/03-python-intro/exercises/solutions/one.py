import random

class Monster:

    def __init__(self,name):
        #initialize your stuff here
        self.health = 100
        self.name = name


    def wound(self,damage):
        #Here is where you can damage the monster
        self.health -= damage
        
        
def strike():
    return random.randint(5,21)

monster = Monster("Bob")
while monster.health > 0:
    print(f"{monster.name} health is {monster.health}")
    monster.wound(strike())
    if monster.health < 0:
        print(f"{monster.name} is dead")
    