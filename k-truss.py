import networkx as nx

def load_graph_from_file(file_path):
    G = nx.Graph()
    with open(file_path, 'r') as file:
        for line in file:
            # Assuming the file is in the format: node1\tnode2\n
            edge = line.strip().split('\t')
            G.add_edge(edge[0], edge[1])
    return G

def k_truss(graph, k):
    # NetworkX does not have a built-in k-truss algorithm, so we'll implement it ourselves
    subgraph = graph.copy()
    edges_removed = True

    while edges_removed:
        edges_removed = False
        for edge in list(subgraph.edges()):
            common_neighbors = set(subgraph.neighbors(edge[0])) & set(subgraph.neighbors(edge[1]))
            if len(common_neighbors) < (k - 2):
                subgraph.remove_edge(*edge)
                edges_removed = True

    return subgraph

def main():
    # Load the graph from the file
    file_path = 'simulated_adj.tsv'
    G = load_graph_from_file(file_path)

    # Set the desired k value
    k_value = 4  # You can adjust this based on your requirements

    # Find k-truss subgraph
    k_truss_subgraph = k_truss(G, k_value)

    # Print nodes and edges of the k-truss subgraph
    print("Nodes in the k-truss subgraph:")
    print(k_truss_subgraph.nodes())
    print("\nEdges in the k-truss subgraph:")
    print(k_truss_subgraph.edges())

    # Optionally, you can visualize the k-truss subgraph
    try:
        import matplotlib.pyplot as plt

        nx.draw(k_truss_subgraph, with_labels=True, font_weight='bold')
        plt.show()
    except ImportError:
        print("Matplotlib not installed. Unable to visualize the graph.")

if __name__ == "__main__":
    main()
