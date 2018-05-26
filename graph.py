import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import glob
import graph_node

key = "N"
path = './log/*'
files = glob.glob(path)
nodes = []
node_list = []
edge_list = []
G = nx.MultiDiGraph()

for file in files:
    nodeId = ""
    f = open(file, 'r')

    for line in f:
        values = line.split(' ')
        values[0] = values[0].replace('\r', '')
        values[-1] = values[-1].replace('\n', '')

        if values[0] == key:
            neighbour = values[2]

            if not nodeId:
                nodeId = values[1]

                # if the read node has not been read yet
                if not any(node.id == nodeId for node in nodes):
                    node = graph_node.Node(nodeId)
                    nodes.append(node)

            # find the node from node list
            node = filter(lambda node: node.id == nodeId, nodes)[0]

            if neighbour not in node.neighbours:
                node.add_neighbour(neighbour)

    f.close()

for node in nodes:
    node_list.append(node.id)
    for neighbour in node.neighbours:
        node_list.append(neighbour)
        edge_list.append((node.id, neighbour))

node_list = list(set(node_list))

G.add_nodes_from(node_list)
G.add_edges_from(edge_list)

pos = nx.spring_layout(G, k=7*1/np.sqrt(len(G.nodes())), iterations=50)

nx.draw(G, pos,
        with_labels=True, font_size=10,
        node_size=1000, node_color='#bcfcb8',
        linewidths=0,
        edge_color='#474747', edge_alpha=0.1)

plt.show()
