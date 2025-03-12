# Exercise 2: Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
import random
a = []
for i in range(100):
    a.append(random.randrange(1000000000,9999999999))
wineer = random.sample(a,2)
print(wineer)

