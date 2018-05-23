import networkx as nx
import matplotlib.pyplot as plt
import glob
import graph_node

key = "N"
path = './log/*'
files = glob.glob(path)
nodes = []
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

                if not any(node.id == nodeId for node in nodes):
                    node = graph_node.Node(nodeId)
                    nodes.append(node)

            node = filter(lambda node: node.id == nodeId, nodes)[0]

            if neighbour not in node.neighbours:
                node.add_neighbour(neighbour)

    f.close()

for node in nodes:
    for neighbour in node.neighbours:
        G.add_edge(node.id, neighbour)

nx.draw(G, with_labels=True, font_size=10, node_size=1000, linewidths=0)

plt.show()
