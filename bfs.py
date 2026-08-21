from collections import deque

graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['E'], 'D': [], 'E': []}
start = input("Enter start node: ").upper()
queue, visited = deque([start]), []
while queue:
    node = queue.popleft()
    if node not in visited:
        visited.append(node)
        queue.extend(graph[node])
print("BFS:", visited)
