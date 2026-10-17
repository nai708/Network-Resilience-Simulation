import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()  # G is currently an empty graph for the chain network

chain = [("A","B",),
         ("B","C"),
         ("C","D"),
         ("D","E"),
         ("E","F")] # List of edges in network

cycle = [("A","B",),
         ("B","C"),
         ("C","D"),
         ("D","E"),
         ("E","F"),
         ("A","F")]

mesh = [
    ("A", "B"),
    ("B", "C"),
    ("C", "D"),
    ("D", "E"),
    ("E", "F"),
    ("A", "F"),
    ("B", "E"),
    ("A", "D"),
    ("C", "F")
]

G.add_edges_from(chain) # Adds chain connections to graph G
nx.draw(G, with_labels=True, font_weight="bold", node_color="lightblue", font_color="white")
plt.savefig("chain_before.png", dpi=300, bbox_inches="tight") # Image of graph prior to removing any nodes
plt.show()


H = nx.Graph() # H is currently an empty graph for the cycle network
H.add_edges_from(cycle)
nx.draw(H, with_labels=True, font_weight="bold", node_color="lightblue", font_color="white")
plt.savefig("cycle_before.png", dpi=300, bbox_inches="tight")
plt.show()

I = nx.Graph()  # I is currently an empty graph for the mesh network
I.add_edges_from(mesh)
nx.draw(I, with_labels=True, font_weight="bold", node_color="lightblue", font_color="white")
plt.savefig("mesh_before.png", dpi=300, bbox_inches="tight")
plt.show()

