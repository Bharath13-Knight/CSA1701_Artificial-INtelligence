def alphabeta(depth, alpha, beta, maximizing):
    if depth == 0: return 0
    values = [alphabeta(depth - 1, alpha, beta, not maximizing) + (1 if maximizing else -1) for _ in range(2)]
    value = max(values) if maximizing else min(values)
    return value
print("Best value:", alphabeta(3, -999, 999, True))
