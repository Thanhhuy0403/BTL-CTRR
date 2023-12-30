import networkx as nx

def load_graph(file_path):
    """
    Load the graph from the input file.

    Parameters:
    - file_path: Path to the input file in TSV format.

    Returns:
    - graph: A NetworkX graph.
    """
    graph = nx.Graph()
    with open(file_path, 'r') as file:
        for line in file:
            # Assuming the file is in the format: source_node \t target_node \t weight
            source, target, weight = map(int, line.strip().split('\t'))
            graph.add_edge(source, target, weight=weight)

    return graph

if __name__ == "__main__":
    file_path = "test_adj.tsv"  # Replace with the path to your input file
    graph = load_graph(file_path)
    triangle_count = sum(nx.triangles(graph).values()) // 3  # Each triangle is counted three times
    print(f"The number of triangles in the graph is: {triangle_count}")
