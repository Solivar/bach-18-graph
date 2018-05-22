import networkx as nx
import matplotlib.pyplot as plt
import glob
import os

key = "N"

path = './log/*'
files = glob.glob(path)
nodes = []
G = nx.DiGraph()

for file in files:
    f = open(file, 'r')

    nodeId = os.path.basename(f.name) # Get nodeID from log file name
    nodes.append(nodeId)

    for line in f:
        values = line.split(' ')
        values = map(str.rstrip, values)

        if line[0] == key:
            G.add_edge(nodeId, values[1]),

    f.close()

nx.draw(G, with_labels=True)
plt.show()
