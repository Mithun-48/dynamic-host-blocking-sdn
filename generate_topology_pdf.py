from topology.topo import DynamicBlockTopo
import networkx as nx
import matplotlib.pyplot as plt

topo = DynamicBlockTopo()
G = nx.Graph()

for h in topo.hosts():
    G.add_node(h)

for s in topo.switches():
    G.add_node(s)

for link in topo.links():
    G.add_edge(link[0], link[1])

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000)

plt.savefig("topology.pdf")
print("PDF created")
