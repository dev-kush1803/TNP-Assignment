import random

print(random.random())
print(random.randint(1,10))
print(random.randrange(1,10,3))
print(random.uniform(10.2,12.8))

team = [1,2,43,5,7,9,87,56,45,23]
print(random.choices(team,k=5))
te = random.sample(team,10)
random.shuffle(te)
print(te)
print(team)
