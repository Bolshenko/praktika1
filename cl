import socket
import numpy as np
import random
import pickle

# Константы
NUM_VERTICES = 20
SERVER_1_ADDRESS = ('floyd-service1', 5001)
SERVER_2_ADDRESS = ('floyd-service2', 5002)


def generate_graph(num_vertices):
    graph = np.random.randint(1, 100, size=(num_vertices, num_vertices))
    graph = np.triu(graph, 1)
    graph += graph.T
    np.fill_diagonal(graph, 0)
    return graph

def send_graph_to_server(graph, server_address):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(server_address)
        s.sendall(pickle.dumps(graph))
        result = b""
        while True:
            packet = s.recv(4096)
            if not packet:
                break
            result += packet

    return pickle.loads(result)


def gather_results(graph):
    result_1 = send_graph_to_server(graph, SERVER_1_ADDRESS)
    result_2 = send_graph_to_server(graph, SERVER_2_ADDRESS)
    final_result = np.minimum(result_1[0], result_2[0])
    predecessors = result_1[1]
    return final_result, predecessors


def get_path(predecessors, start_vertex, end_vertex):
    path = []
    current = end_vertex

    while current != -1:
        path.append(current)
        current = predecessors[start_vertex][current]

    path.reverse()
    return path


if __name__ == "__main__":
    graph = generate_graph(NUM_VERTICES)
    print("Сгенерированная матрица графа:")
    print(graph)

    result, predecessors = gather_results(graph)
    print("Отработанная матрица:")
    print(result)
    path = get_path(predecessors, 0, 19)
    print("Минимальный путь из вершины 1 в вершину 19:")
    normal_list = list(map(int, path))
    print(normal_list)  
