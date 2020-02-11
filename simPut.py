import random
diceRoll = int(input("How many times will you roll?: "))

num = (random.randint(1,6))
i = 0

while(i < diceRoll):
    num = random.randint(1,6)
    print(num)
    i += 1

