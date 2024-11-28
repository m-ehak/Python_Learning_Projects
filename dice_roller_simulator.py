import random

dice = int(input("Enter the number of dice: "))
if dice <= 0:
    print("Must have atleast one dice!")
    quit()
    
sides =  int(input("Enter the number of sides: "))
if sides <= 0:
    print("Must have atleast one sides!")
    quit()
    
roll = []

for i in range(0 , dice):
    face = random.randint(1 , sides)
    roll.append(face)
   
print(roll)   