import random
N = 20
position = 0
for t in range(1e5):
	if random.uniform(0.0,1.0) < 0.5:
		position = (position + 1) % N
	else:
		position = (position - 1) % N
