import networkx as nx
import random
import time
import matplotlib.pyplot as plt

vertex_counts = [100, 2000, 3000, 8000]
time_records = []

for vertex_count in vertex_counts:
    edge_list = [(i, j) for i in range(vertex_count) for j in range(i + 1, vertex_count)]
    random.shuffle(edge_list)

    G = nx.Graph()
    G.add_edges_from(edge_list)

    while True:
        node_to_remove = int(input(f"Введите вершину для удаления из графа с {vertex_count} вершинами в формате 'вершина': "))

        if node_to_remove in G:
            break
        else:
            print("Введенная вершина не существует. Попробуйте еще раз.")

    adj_edges = list(G.edges(node_to_remove)) # Находим ребра, смежные с вершиной, для удаления
    G.remove_edges_from(adj_edges) # Удаляем смежные ребра
    G.remove_node(node_to_remove)
    
    sorted_nodes = sorted(G.degree, key=lambda x: x[1], reverse=True) # Сортируем вершины в порядке убывания степени вершины
    print("Оставшиеся вершины, отсортированные по степени:")
    for node, degree in sorted_nodes:
        print(node, degree)

    start_time = time.time()
    end_time = time.time()
    node_removal_time = end_time - start_time

    start_time = time.time()
    sorted_vertices = sorted(G.nodes(), key=lambda x: G.degree(x), reverse=True)
    end_time = time.time()
    sorting_time = end_time - start_time
    total_time = sorting_time + node_removal_time
    time_records.append(total_time)

plt.plot(vertex_counts, time_records)
plt.xlabel('Количество вершин')
plt.ylabel('Время выполнения (с)')
plt.title('Время выполнения vs Количество вершин')
plt.show()

