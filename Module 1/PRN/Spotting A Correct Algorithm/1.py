import random
N = 20
position = 0
for t in range(1e5):
	direction = random.choice([-1,1])
	position  = (position + direction) % N
