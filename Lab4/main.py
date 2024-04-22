import heapq
import random
import time
import matplotlib.pyplot as plt


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def floyd_warshall(weights, num_vertices):
    dist = [[float('infinity')] * num_vertices for _ in range(num_vertices)]

    for v in range(num_vertices):
        dist[v][v] = 0

    for v1, v2, weight in weights:
        dist[v1][v2] = weight

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


def generate_graph(n, edge_prob=0.1):
    graph = {i: {} for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < edge_prob:
                weight = random.randint(1, 10)
                graph[i][j] = weight
                graph[j][i] = weight
    return graph


def measure_time(graph, algorithm):
    start = time.time()
    if algorithm == "dijkstra":
        for node in graph:
            dijkstra(graph, node)
    elif algorithm == "floyd_warshall":
        num_vertices = len(graph)
        edge_list = [(i, j, graph[i][j]) for i in graph for j in graph[i]]
        floyd_warshall(edge_list, num_vertices)
    end = time.time()
    return end - start


def plot_data(sizes, times, title):
    plt.figure(figsize=(10, 5))
    for algorithm in times:
        plt.plot(sizes, times[algorithm], label=algorithm)
    plt.xlabel('Number of Nodes')
    plt.ylabel('Time (s)')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

sizes = [10, 20, 30, 40, 50]
times_sparse = {"dijkstra": [], "floyd_warshall": []}
times_dense = {"dijkstra": [], "floyd_warshall": []}

for size in sizes:
    sparse_graph = generate_graph(size, 0.1)
    dense_graph = generate_graph(size, 0.5)

    times_sparse["dijkstra"].append(measure_time(sparse_graph, "dijkstra"))
    times_sparse["floyd_warshall"].append(measure_time(sparse_graph, "floyd_warshall"))

    times_dense["dijkstra"].append(measure_time(dense_graph, "dijkstra"))
    times_dense["floyd_warshall"].append(measure_time(dense_graph, "floyd_warshall"))

plot_data(sizes, times_sparse, "Sparse Graphs")
plot_data(sizes, times_dense, "Dense Graphs")
