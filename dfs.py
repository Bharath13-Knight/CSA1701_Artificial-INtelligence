graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['E'], 'D': [], 'E': []}
start = input("Enter start node: ").upper()
visited = []

def dfs(node):
    if node not in visited:
        visited.append(node)
        for child in graph[node]:
            dfs(child)

dfs(start)
print("DFS:", visited)
