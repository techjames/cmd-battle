import random

HEROES = ["ROGUE", "MISTY", "MAVERICK"]
VILLAINS = ["WIDOW", "GOBLIN", "HOGWISH"]
winner = ""

class Player:
    def __init__(self, name):
        self.name = name.upper()
        self.health = 100
        self.magic  = 15

actions = {
  'kick': 6,
  'punch': 9,
  'wink': 7,
  }

def battle(action_value):

    hero_epinephrine = random.randint(1,15)
    villain_epinephrine = random.randint(1,15)
    hero.magic -= random.randint(1,3)
    villain.magic -= random.randint(1,2)
    hero.health -= (action_value + villain_epinephrine)
    villain.health -= (action_value + hero_epinephrine)
    hero.health -= villain.magic
    villain.health -= hero.magic


print("#############################################")
print("############ Command Line Battle ############")
print("#############################################")
print("")

while True:
    hero = Player(input("Choose a hero {0}\n".format(HEROES)))
    if hero.name.upper() not in HEROES:
        print("Sorry, your hero can't hear you")
        continue
    else:
        break

villain = Player(random.choice(VILLAINS))

print("#############################################")
print("")
print("")
print("{0} you will fight {1}\n".format(hero.name, villain.name))



while True:
    print("{0} (Health:{1} Magic:{2})  V  {3} (Health:{4} Magic:{5})\n".format(hero.name, hero.health, hero.magic, villain.name, villain.health, villain.magic))
    action_value = input("{0} ?  ".format(list(actions.keys())))
    if action_value not in actions.keys():
        print("try again!\n")
        continue
    else:
        print("")
        print("{0} counter attacks with a {1}\n".format(villain.name, random.choice(list(actions.keys()))))
        battle(actions[action_value])
        if hero.health <= 0 or villain.health <= 0:
            if villain.health <= 0:
                winner = villain.name
            elif hero.health <= 0:
                winner = hero.name
            else:
                winner = "Gremlin"

            print("*WINNER* is {0}".format(winner))
            break
        else:
            continue



print("#############################################")