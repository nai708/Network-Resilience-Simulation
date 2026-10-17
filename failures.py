import networkx as nx
from main import G, chain, H, cycle, I, mesh
import matplotlib.pyplot as plt

for nodes in G.nodes:
    failed_Ggraph = G.copy() # Makes copy of original graph before changes are made
    failed_Ggraph.remove_node(nodes) # Remove current node in the loop
    nx.draw(failed_Ggraph, with_labels=True, font_weight="bold", node_color="lightblue", font_color="white") # Create graph with the removed node
    plt.savefig(f"chain_after{nodes}.png", dpi=300, bbox_inches="tight") # Saves image in folder after each changes. 6 Images per graph
    plt.close() # Close window to free up memory


for nodes in H.nodes:
    failed_Hgraph = H.copy()
    failed_Hgraph.remove_node(nodes)
    nx.draw(failed_Hgraph, with_labels=True, font_weight="bold", node_color="lightblue", font_color="white")
    plt.savefig(f"cycle_after{nodes}.png", dpi=300, bbox_inches="tight")
    plt.close()


for nodes in I.nodes:
    failed_Igraph = I.copy()
    failed_Igraph.remove_node(nodes)
    nx.draw(failed_Igraph, with_labels=True, font_weight="bold", node_color="lightblue", font_color="white")
    plt.savefig(f"mesh_after{nodes}.png", dpi=300, bbox_inches="tight")
    plt.close()
