#Script description: Roll dice
# function without return and without params
from random import randint, uniform
import os

def rollDice():
    die1= randint(1,6)
    die2= randint(1,6)
    print(f"DIE1:{die1}")
    print(f"DIE2:{die2}")
#Main
rollDice()