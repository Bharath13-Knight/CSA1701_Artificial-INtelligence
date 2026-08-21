from math import gcd

a, b, target = map(int, input("Enter jug1, jug2, target: ").split())
possible = target <= max(a, b) and target % gcd(a, b) == 0
print("Target possible:", possible)
