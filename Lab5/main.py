import heapq
import matplotlib.pyplot as plt
import random
import time


# Prim
def prim(graph, start_vertex):
    visited = set([start_vertex])
    edges = [(cost, start_vertex, to) for to, cost in graph[start_vertex].items()]
    heapq.heapify(edges)
    mst_cost = 0
    mst_edges = []

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst_cost += cost
            mst_edges.append((frm, to, cost))

            for next_to, next_cost in graph[to].items():
                if next_to not in visited:
                    heapq.heappush(edges, (next_cost, to, next_to))

    return mst_cost, mst_edges


# Kruskal
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(graph, vertices):
    result = []
    i, e = 0, 0
    graph = sorted(graph, key=lambda item: item[2])
    parent = [node for node in range(vertices)]
    rank = [0 for _ in range(vertices)]

    while e < vertices - 1 and i < len(graph):  # Check to ensure index is within the bounds of the graph list
        u, v, w = graph[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            e += 1
            result.append((u, v, w))
            union(parent, rank, x, y)

    return result



# Function to generate a random graph represented as an adjacency list
def generate_random_graph(num_vertices):
    graph = {i: {} for i in range(num_vertices)}
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if random.random() > 0.5:  # Randomly deciding whether to connect vertices
                weight = random.randint(1, 100)
                graph[i][j] = weight
                graph[j][i] = weight
    return graph


# Function to prepare a graph suitable for Kruskal's algorithm
def prepare_edges(graph):
    edges = []
    for u in graph:
        for v, weight in graph[u].items():
            if u < v:
                edges.append((u, v, weight))
    return edges


sizes = [10, 50, 100, 250, 500, 750]  # Example sizes of graphs
prim_times = []
kruskal_times = []

for size in sizes:
    # Generate a random graph
    graph = generate_random_graph(size)
    edges = prepare_edges(graph)

    # Measure Prim's algorithm time
    start_time = time.time()
    prim(graph, 0)
    end_time = time.time()
    prim_times.append(end_time - start_time)

    # Measure Kruskal's algorithm time
    start_time = time.time()
    kruskal(edges, size)
    end_time = time.time()
    kruskal_times.append(end_time - start_time)

# Plotting the results
plt.plot(sizes, prim_times, label='Prim\'s Algorithm')
plt.plot(sizes, kruskal_times, label='Kruskal\'s Algorithm')
plt.xlabel('Number of Nodes')
plt.ylabel('Execution Time (s)')
plt.title('Performance Analysis')
plt.legend()
plt.show()



