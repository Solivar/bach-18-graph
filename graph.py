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
    nodeId = ""
    f = open(file, 'r')

    #nodeId = os.path.basename(f.name) # Get nodeID from log file name

    for line in f:
        #values = line.rstrip()
        #print line
        values = line.split(' ')
        values[0] = values[0].replace('\r', '')
        values[-1] = values[-1].replace('\n', '')

        if values[0] == key:
            if not nodeId:
                nodeId = values[1]
                nodes.append(nodeId)

            G.add_edge(nodeId, values[2])

    f.close()

nx.draw(G, with_labels=True)
plt.show()
