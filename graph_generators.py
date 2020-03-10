# Utility to generate connected random graphs via Networkx, https://networkx.github.io/documentation/stable/reference/generators.html

import networkx as nx
import random

# Generates a connected ER graph
def er(n, k, with_random_weights=False):
    while True:
        G = nx.erdos_renyi_graph(n, k/n)
        if nx.is_connected(G):
            if with_random_weights:
                for (u, v) in G.edges():
                    G.edges[u,v]['weight'] = random.random()
            else:
                for (u, v) in G.edges():
                    G.edges[u,v]['weight'] = 1
            break

    return G

# Generates a connected Watts-Strogatz graph
def ws(n, k, with_random_weights=False):
    while True:
        G = nx.connected_watts_strogatz_graph(n, k, 0.3)
        if nx.is_connected(G):
            if with_random_weights:
                for (u, v) in G.edges():
                    G.edges[u,v]['weight'] = random.random()
            else:
                for (u, v) in G.edges():
                    G.edges[u,v]['weight'] = 1
            break
    
    return G

# Generates a connected Barabasi-Albert graph
def ba(n, k, with_random_weights=False):
    while True:
        G = nx.barabasi_albert_graph(n, k)
        if nx.is_connected(G):
            if with_random_weights:
                for (u, v) in G.edges():
                    G.edges[u,v]['weight'] = random.random()
            else:
                for (u, v) in G.edges():
                    G.edges[u,v]['weight'] = 1
            break
    
    return G
