import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Διαβάζουμε το αρχείο και κρατάμε τις πρώτες 50,000 γραμμές
file_path = "./sx-stackoverflow-a2q.txt"
data = pd.read_csv(file_path, delimiter=' ', header=None, nrows=50000)

# Μετονομάζουμε τις στήλες για ευκολία
data.columns = ['source', 'target', 'timestamp']

# Χωρίζουμε τον χρόνο σε 5 ίσα διαστήματα
time_intervals = np.linspace(data['timestamp'].min(), data['timestamp'].max(), 6)  # 5 intervals + 1 endpoint

# Κατάτμηση των δεδομένων σε 5 διαστήματα
intervals_data = []
for i in range(len(time_intervals) - 1):
    interval_data = data[(data['timestamp'] >= time_intervals[i]) & (data['timestamp'] < time_intervals[i+1])]
    intervals_data.append(interval_data)

# Δημιουργία γράφων για κάθε διάστημα
graphs = []
nodes_edges_info = []

for i, interval_data in enumerate(intervals_data):
    G = nx.from_pandas_edgelist(interval_data, 'source', 'target', create_using=nx.DiGraph())
    graphs.append(G)
    nodes_edges_info.append((G.number_of_nodes(), G.number_of_edges()))

# Απεικόνιση του αριθμού των κόμβων και των ακμών για κάθε διάστημα
intervals = [f"Interval {i+1}" for i in range(len(intervals_data))]
nodes_counts = [info[0] for info in nodes_edges_info]
edges_counts = [info[1] for info in nodes_edges_info]

# Δημιουργία διαγράμματος
fig, ax1 = plt.subplots()

ax1.set_xlabel('Time Intervals')
ax1.set_ylabel('Number of Nodes', color='tab:blue')
ax1.plot(intervals, nodes_counts, 'o-', color='tab:blue', label='Nodes')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.set_ylabel('Number of Edges', color='tab:red')
ax2.plot(intervals, edges_counts, 'o-', color='tab:red', label='Edges')
ax2.tick_params(axis='y', labelcolor='tab:red')

fig.tight_layout()
plt.title("Evolution of Nodes and Edges over Time")
plt.show()
