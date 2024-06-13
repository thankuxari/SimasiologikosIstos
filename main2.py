import networkx as nx
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

df = pd.read_csv('./ego.csv')

edge_list = df.values.tolist()

G = nx.from_edgelist(edge_list)

degree = G.degree()

#Ερωτημα Γ

#Μέσος Βαθμός
degree_num = [item[1] for item in degree]
degrees = [degree for node, degree in G.degree()]
mean_degree = np.mean(degree_num)
print(f'Μέσος βαθμός : {mean_degree}')


#Μέσο συντελεστή συσταδοποίησης
average_clustering = nx.average_clustering(G)
print(f'Μέσος Συντελεστή Συσταδοποίησης: {average_clustering}')

#Χαρακτηριστικό μήκος μονοπατιού
if nx.is_connected(G):
    characteristic_path_length = nx.average_shortest_path_length(G)
    print(f'Χαρακτηριστικό Μήκος Μονοπατιού : {characteristic_path_length}')
else :
    print('Ο γράφος δεν είναι συνδεμένος')

#Ερώτημα Β
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
print(f"Αριθμός των κόμβων: {num_nodes}")
print(f"Αριθμός των ακμών: {num_edges}")

#Ερώτημα Δ
degree_counts = Counter(degrees)

sorted_degrees = sorted(degree_counts.items())

x,y = zip(*sorted_degrees)

plt.figure()
plt.bar(x, y, width=2.80, color='b')
plt.title("Κατανομή των Βαθμών")
plt.xlabel("Βαθμός")
plt.ylabel("Πλήθος Κόμβων")
plt.grid(True)
plt.show()

#Ερώτημα Α
pos = nx.spring_layout(G)

plt.figure()
nodes = nx.draw_networkx_nodes(G, pos, alpha=0.8)
nodes.set_edgecolor('k') 
nx.draw_networkx_labels(G, pos, font_size=8)
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.2)

plt.show()

