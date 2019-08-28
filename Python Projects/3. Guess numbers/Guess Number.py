import random
for x in range(100):
    randomNum = random.randint(0, 100)

Guess = input(" guess the number between 1 & 100")
Guess = int(Guess)
if Guess > 100:
    print("you went over 100")
    Guess = input("enter a number between 1 & 100")
else:
    print("")

if Guess == randomNum:
    print("correct the number was " + str(randomNum))
else:
    print("Incorrect the number was " + str(randomNum))