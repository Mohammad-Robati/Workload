import random

maxI = int(random.uniform(500, 1000))
print(maxI)
for i in range(maxI):
    print(int(random.uniform(0, 50.)), end=' ')
    print(int(random.uniform(1, 50)), end=' ')
    print(int(random.uniform(1, 50)), end=' ')
    print(int(random.uniform(1, 50)))
