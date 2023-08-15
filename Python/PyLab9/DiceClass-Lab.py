from abc import ABC
import random
class Dice(ABC):
    def __init__(self,noOfSides):
        self.noOfSides = noOfSides
class D2(Dice):
    def roll(self):
        rolledNumberD2 = random.randint(1,2)
        return(rolledNumberD2)
class D4(Dice):
    def roll(self):
        rolledNumberD4 = random.randint(1,4)
        return(rolledNumberD4)
class D6(Dice):
    def roll(self):
        rolledNumberD6 = random.randint(1,6)
        return(rolledNumberD6)
class D20(Dice):
    def roll(self):
        rolledNumberD20 = random.randint(1,20)
        return(rolledNumberD20)
def calculateScore():
        Roll1 = D6.roll(D6)
        Roll2 = D6.roll(D6)
        Roll3 = D6.roll(D6)
        Roll4 = D6.roll(D6)
        sortedRolls = [Roll1,Roll2,Roll3,Roll4]
        sortedRolls.sort()
        removeLowest = sortedRolls.remove(sortedRolls[0])
        Score = sum(sortedRolls)
        return Score
getStartedInput = input("""
---------------------------------------------------------------------------------------
| DnD 5th edition: Roll a character sheet for a Swashbuckler Rogue? (y/n)|
---------------------------------------------------------------------------------------             
""")
if getStartedInput == "y" or getStartedInput == "Y":
    print("Generating Ability Scores...")
    Score1 = calculateScore()
    Score2 = calculateScore()
    Score3 = calculateScore()
    Score4 = calculateScore()
    Score5 = calculateScore()
    Score6 = calculateScore()
    listOfScores = [Score1, Score2, Score3, Score4, Score5, Score6]
    
    print("Class: Swashbuckler Rogue \nName: Earl Grey") 
    print("Strength:",Score1 +4)
    print("Dexterity:",Score2 +2)
    print("Constitution:",Score3 +2)
    print("Intelligence:",Score4)
    print("Wisdom:",Score5 -1)
    print("Charisma:", Score6 +1)

else:
    exit
    """
    called 
    How do you Roll for Stats in 5e?
1 Roll 4 x 6 sided dice.
2 Remove the lowest dice result.
3 Add up the remaining numbers to get an ability score.
4 Write down this ability score on note paper.
5 Repeat these steps until you have 6 ability scores.
6 Assign a score to each attribute on your character sheet.
    """
    """
inputDie = input("
----------------------------------
| Which die do you wish to roll? |
| 1 - d2 = Dice(2)               |
| 2 - d4 = Dice(4)               |
| 3 - d6 = Dice(6)               |
| 4 - d20 = Dice(20)             |
|                                |
----------------------------------

Enter an option:              
")
if inputDie == "1":
    d2Roll = D2.roll(D2)
elif inputDie == "2":
    d4Roll = D4.roll(D4)
elif inputDie == "3":
    d6Roll = D6.roll(D6)
elif inputDie == "4":
    d20Roll = D20.roll(D20)
else:
    exit
    """
