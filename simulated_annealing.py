import random, math
value = int(input("Enter starting value: "))
temperature = 10
for _ in range(100):
    candidate = value + random.choice((-1, 1))
    if candidate > value or random.random() < math.exp((candidate-value)/temperature): value = candidate
    temperature *= .95
print("Final value:", value)
