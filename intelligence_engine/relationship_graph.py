import networkx as nx

def build_relationship(numbers):

    G = nx.Graph()

    for i in range(len(numbers)-1):
        G.add_edge(numbers[i], numbers[i+1])

    return G
