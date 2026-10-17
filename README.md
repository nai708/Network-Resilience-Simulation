# Network-Resilience-Simulation
Investigating the ability of a network to stay connected when individual nodes fail.
## Overview

Using Python and NetworkX, I created three types of networks: a chain, a cycle, and a mesh-like network. Then simulated individual node failures to observe how each structure responds.

This is an introductory computational modeling project exploring network resilience and the effects of component failures on connected systems.

## Networks

The simulation compares three network structures, each containing six nodes.

- **Chain:** Nodes are connected in a line, with no alternative routes between the ends.
- **Cycle:** Nodes form a loop, providing an alternative route around the network.
- **Mesh:** Nodes have additional connections that create multiple possible routes between parts of the network.

## Methodology

1. Construct the three networks using NetworkX.
2. Save images of each original network.
3. Create a fresh copy of each network for every failure test.
4. Remove one node from the copy to simulate a component failure.
5. Save an image showing the resulting network.
6. Compare how the network structures respond to individual failures.

Each node is tested separately, so the original network remains unchanged between experiments.

## Tools and Technologies

- Python
- NetworkX
- Matplotlib

## Future Improvements
- Measure the number of connected components after each failure.
- Compare resilience across network structures.
- Introduce probabilistic failures and repeated trials.
