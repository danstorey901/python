import random

def B():
    a = random.randrange (2)
    if(a == 1):
        print ("BABY SHARK")
    if(a == 0):
        print ("doo, doo, doo, doo, doo, doo")
    if(a == 2):
        print ("CRIT")
    input("press enter to repeat")
    B()

B()
