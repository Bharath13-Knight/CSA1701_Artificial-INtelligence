from itertools import permutations
n = int(input("Enter number of cities: "))
cost = [list(map(int, input().split())) for _ in range(n)]
best = min((sum(cost[path[i]][path[i+1]] for i in range(n-1)) + cost[path[-1]][path[0]], path)
           for path in permutations(range(n)))
print("Minimum cost:", best[0], "Tour:", best[1])
