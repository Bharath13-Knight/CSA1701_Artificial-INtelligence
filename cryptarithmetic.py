from itertools import permutations
for digits in permutations(range(10), 3):
    a, b, c = digits
    if a and a + b == 10 * b + c:
        print(f"A={a}, B={b}, C={c}"); break

