import networkx as nx
import matplotlib.pyplot as plt

# Create a directed acyclic graph (DAG)
graph = {5: [2, 0], 4: [0, 1], 2: [3], 3: [1]}
G = nx.DiGraph(graph)

# Perform topological sort
topological_order = list(nx.topological_sort(G))
print("Topological Sort:", topological_order)

# Draw the graph with node labels and edge directions
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # Position the nodes using spring layout
nx.draw(G, pos = pos, ax = None, with_labels = True, font_size = 20, node_size = 2000,)

# Display the graph
plt.title("Topological Sort Visualization")
plt.show()
