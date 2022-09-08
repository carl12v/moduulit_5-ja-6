import random

counts = [0] * 6
for i in range(10):
    roll = random.randint(1,6)
    print("roll number" , i, ":" , roll)
    counts[roll-1] += 1

for side, count in enumerate(counts):
    print(side+1, "was rolled", count, "amount of times")