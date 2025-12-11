import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK =1
    PAPER=2
    SCISSORS=3


print("")
playerchoice=input("Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")


if not playerchoice.isdigit():
    sys.exit("You must enter a number(1, 2 or 3).")
    
player=int(playerchoice)

if player<1 or player>3:
    sys.exit("You must enter 1, 2, or 3.")
    
computer = random.randint(1, 3)

print("")
print("You chose " +str(RPS(player)).replace('RPS.','')+".")
print("Python chose " +str(RPS(computer)).replace('RPS.','')+".")
print("")

if player==computer:
    print("😮 Tie game!") 
elif (player==1 and computer==3) or (player==2 and computer==1) or (player==3 and computer==2):
    print("🎉 You win!")
else:
    print("🐍 Python wins!")
    