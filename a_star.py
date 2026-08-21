import heapq

graph = {'A': [('B', 1), ('C', 4)], 'B': [('D', 2)], 'C': [('D', 1)], 'D': []}
h = {'A': 3, 'B': 2, 'C': 1, 'D': 0}; goal = input("Enter goal node: ").upper()
queue, best = [(h['A'], 0, 'A')], {'A': 0}
while queue:
    _, cost, node = heapq.heappop(queue)
    if node == goal: print("Path cost:", cost); break
    for child, weight in graph[node]:
        new = cost + weight
        if new < best.get(child, 999): best[child] = new; heapq.heappush(queue, (new + h[child], new, child))

