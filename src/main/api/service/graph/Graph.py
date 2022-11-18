class Node:
    def __init__(self, id_node: int, name:str):
        self.visited = 0
        self.adj_list = list()
        self.id = id_node
        self.dist = 9999999
        self.menor_caminho = list()
        self.name = name

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
        self.size = size

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
