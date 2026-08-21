import heapq

graph = {'A': [('B', 1), ('C', 4)], 'B': [('D', 2)], 'C': [('D', 1)], 'D': []}
goal = input("Enter goal node: ").upper()
queue, seen = [(0, 'A')], set()
while queue:
    cost, node = heapq.heappop(queue)
    if node in seen: continue
    seen.add(node)
    if node == goal: print("Found:", node, "Cost:", cost); break
    for child, weight in graph[node]: heapq.heappush(queue, (weight, child))

