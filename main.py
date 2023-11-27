import networkx as nx
import numpy as np

def is_subgraph_isomorphic(adj_matrix_H, adj_matrix_G):
    # Tạo đồ thị từ ma trận kề
    G1 = nx.Graph(adj_matrix_H)
    G2 = nx.Graph(adj_matrix_G)

    # Kiểm tra đồ thị con đẳng cấu
    return nx.is_isomorphic(G1, G2)

#========================== Đọc file amazon0302_adj.tsv ==========================#
with open('test_adj.tsv', 'r') as tsvfile:
    # Đọc dữ liệu từ file TSV và chuyển thành ma trận numpy
    matrix_adj = np.loadtxt(tsvfile, delimiter='\t', dtype=int)

max_size = matrix_adj[matrix_adj.shape[0]-1][0]+1

# Tạo một ma trận toàn số 0
adjacency_matrix = np.zeros((max_size, max_size), dtype=int)

# Xử lý ma trận
for i in matrix_adj:
    adjacency_matrix[int(i[0])][int(i[1])] = 1

adj_matrix_H = np.array(adjacency_matrix)

#========================== End Đọc file test_adj.tsv ==========================#


#========================== Đọc file _inc.tsv ==========================#
with open('test_inc.tsv', 'r') as tsvfile:
    # Đọc dữ liệu từ file TSV và chuyển thành ma trận numpy
    matrix_inc = np.loadtxt(tsvfile, delimiter='\t', dtype=int)

# Tạo một ma trận toàn số 0
incidence_matrix = np.zeros((max_size, max_size), dtype=int)

# Xử lý ma trận
for i in matrix_inc:
    incidence_matrix[int(i[0])][int(i[1])] = 1

adj_matrix_G = np.array(incidence_matrix)
#========================== End Đọc file _inc.tsv ==========================#


# Xác định xem H có phải là đồ thị con đẳng cấu của G hay không
result = is_subgraph_isomorphic(adj_matrix_H, adj_matrix_G)
print(result)

