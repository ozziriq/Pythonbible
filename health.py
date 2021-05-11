import random

health = 50

easy = 1
medium = 2
hard = 3


difficulty = hard

potion_health = int(random.randint(25,50) / difficulty)
health = health + potion_health

print(health)
print(difficulty)





