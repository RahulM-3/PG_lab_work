import networkx as nx
import matplotlib.pyplot as plt

# Define infinity (INF) for unreachable paths
INF = float('inf')

def floyd_warshall(graph):
    V = len(graph)
    dist = [[INF for _ in range(V)] for _ in range(V)]
    
    for u in range(V):
        for v in range(V):
            dist[u][v] = graph[u][v]
    
    for i in range(V):
        dist[i][i] = 0
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

# Example graph as an adjacency matrix
graph = [
    [0, 3, INF, -4],
    [INF, 0, INF, 7],
    [INF, 4, 0, INF],
    [INF, INF, 2, 0]
]

# Run Floyd-Warshall Algorithm
shortest_paths = floyd_warshall(graph)
print(shortest_paths)
# Create a directed graph in networkx
G = nx.DiGraph()

# Add nodes and edges from the distance matrix (shortest_paths)
V = len(shortest_paths)
for i in range(V):
    for j in range(V):
        if shortest_paths[i][j] != INF and i != j:
            G.add_edge(i, j, weight=shortest_paths[i][j])

# Visualize the graph with edge labels representing shortest path weights
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # Layout for visualization
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=15, font_weight='bold', arrows=True)

# Add edge labels for weights (shortest paths)
edge_labels = {(u, v): f'{d["weight"]}' for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("All-Pairs Shortest Path (Floyd-Warshall) Visualization")
plt.show()
