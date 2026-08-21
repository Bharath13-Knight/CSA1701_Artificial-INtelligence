def minimax(depth, maximizing):
    if depth == 0: return 0
    values = [minimax(depth - 1, not maximizing) + (1 if maximizing else -1) for _ in range(2)]
    return max(values) if maximizing else min(values)
print("Best value:", minimax(3, True))
