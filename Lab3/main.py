import time
from collections import deque
import matplotlib.pyplot as plt
import random

# Implement DFS
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)
    return visited

# Implement BFS
def bfs(graph, start):
    visited, queue = set(), deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return visited

# Generate a random graph
def generate_graph(num_nodes):
    graph = {i: set(random.sample(range(num_nodes), 4)) for i in range(num_nodes)}
    for k, v in graph.items():
        for i in v:
            graph[i].add(k)
    return graph

# Metrics collections
dfs_time = []
bfs_time = []
nodes = range(100, 1001, 100)

for n in nodes:
    graph = generate_graph(n)

    start_time = time.time()
    dfs(graph, 0)
    dfs_time.append(time.time() - start_time)

    start_time = time.time()
    bfs(graph, 0)
    bfs_time.append(time.time() - start_time)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(nodes, dfs_time, label='DFS Time', marker='o')
plt.plot(nodes, bfs_time, label='BFS Time', marker='x')
plt.xlabel('Number of Nodes')
plt.ylabel('Time (seconds)')
plt.title('DFS vs BFS Execution Time')
plt.legend()
plt.grid(True)
plt.show()

