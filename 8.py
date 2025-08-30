from collections import deque
graph={
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
def bfs(start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex,end='')
            visited.add(vertex)
            queue.extend(graph[vertex])
def dfs(start,visited=None):
    if visited is None:
        visited = set()
    print(start,end='')
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(neighbor,visited)
print("BFS:")
bfs('A')
print("\nDFS:")
dfs('A')