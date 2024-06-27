import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# Ερώτημα Α
file_path = "./sx-stackoverflow-a2q.txt"
data = pd.read_csv(file_path, delimiter=' ', header=None, nrows=50000)
data.columns = ['source', 'target', 'timestamp']

time_intervals = np.linspace(data['timestamp'].min(), data['timestamp'].max(), 6)  

intervals_data = []
for i in range(len(time_intervals) - 1):
    interval_data = data[(data['timestamp'] >= time_intervals[i]) & (data['timestamp'] < time_intervals[i+1])]
    intervals_data.append(interval_data)


graphs = []
nodes_edges_info = []

for i, interval_data in enumerate(intervals_data):
    G = nx.from_pandas_edgelist(interval_data, 'source', 'target', create_using=nx.DiGraph())
    graphs.append(G)
    nodes_edges_info.append((G.number_of_nodes(), G.number_of_edges()))


intervals = [f"Interval {i+1}" for i in range(len(intervals_data))]
nodes_counts = [info[0] for info in nodes_edges_info]
edges_counts = [info[1] for info in nodes_edges_info]

fig, ax1 = plt.subplots()
ax1.set_xlabel('Time Intervals')
ax1.set_ylabel('Αριθμός Κόμβων', color='tab:blue')
ax1.plot(intervals, nodes_counts, 'o-', color='tab:blue', label='Nodes')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.set_ylabel('Αριθμώς Ακμών', color='tab:red')
ax2.plot(intervals, edges_counts, 'o-', color='tab:red', label='Edges')
ax2.tick_params(axis='y', labelcolor='tab:red')

fig.tight_layout()
plt.title("Κόμβοι και Ακμές με την πάροδο του χρόνου")
plt.show()

# Ερώτημα Β
for i, G in enumerate(graphs):
    degrees = [degree for node, degree in G.degree()]
    degree_counts = Counter(degrees)
    sorted_degrees = sorted(degree_counts.items())
    x, y = zip(*sorted_degrees) if sorted_degrees else ([], [])
    
    plt.figure()
    plt.bar(x, y, width=0.80, color='b')
    plt.title(f'Κατανομή των Βαθμών για το Χρονικό Διάστημα {i+1}')
    plt.xlabel('Βαθμός')
    plt.ylabel('Πλήθος Κόμβων')
    plt.grid(True)
    plt.show()

# Ερώτημα Γ
for i, G in enumerate(graphs):
    num_components = nx.number_connected_components(G.to_undirected())
    print(f"Αριθμός Συνδεδεμένων Συνιστωσών στο Χρονικό Διάστημα {i+1}: {num_components}")

# Ερώτημα Δ
common_nodes = []
for i in range(len(graphs) - 1):
    current_nodes = set(graphs[i].nodes())
    next_nodes = set(graphs[i+1].nodes())
    common = len(current_nodes & next_nodes)
    common_nodes.append(common)
    print(f"Πλήθος Κοινών Κόμβων μεταξύ Διαστήματος {i+1} και {i+2}: {common}")


plt.figure(figsize=(12, 6))
plt.plot(range(1, len(common_nodes) + 1), common_nodes, label='Πλήθος Κοινών Κόμβων', marker='o')
plt.xlabel('Διαδοχικά Χρονικά Διαστήματα')
plt.ylabel('Πλήθος Κοινών Κόμβων')
plt.title('Πλήθος Κοινών Κόμβων μεταξύ Διαδοχικών Χρονικών Διαστημάτων')
plt.grid(True)
plt.show()
