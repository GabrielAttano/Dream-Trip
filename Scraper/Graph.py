class Node:
    def __init__(self, id_node):
        self.visited = 0
        self.adj_list = []
        self.id = id_node

    def add_adjacency(self, connection):
        self.adj_list.append(connection)

    def adj_length(self):
        return len(self.adj_list)

    def adj_list_isEmpty(self):
        if len(self.adj_list) == 0:
            return True
        else:
            return False

class Graph:
    def __init__(self, size):
        self.nodes = []

        for i in range(size):
            self.nodes.append(Node(i))

    def show_nodes(self):
        for i in range(len(self.nodes)):
            if not self.nodes[i].adj_list_isEmpty:
                print(f"{self.nodes[i].id} -> {self.nodes[i].adj_list}\n")
            else:
                print(f"{self.nodes[i].id} -> {self.nodes[i].adj_list}\n")

    def add_connection(self, node1, node2, distance):
        self.nodes[node1].add_adjacency([node2, distance])
        self.nodes[node2].add_adjacency([node1,distance])

graph = Graph(5)

for i in range(4):
    node1, node2 = input("informe os nodes a serem adicionados\n").split()
    distance = int(input("informe a distancia\n"))
    graph.add_connection(int(node1), int(node2), distance)

graph.show_nodes()
