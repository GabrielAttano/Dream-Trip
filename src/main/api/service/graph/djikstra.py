from Graph import Graph
from heapq import heapify, heappush,heappop

grafo = Graph(5)


grafo.add_connection(0, 1, 4)
grafo.add_connection(0, 2, 2)
grafo.add_connection(0, 3, 5)
grafo.add_connection(1, 4, 1)
grafo.add_connection(2, 1, 1)
grafo.add_connection(2, 3, 2)
grafo.add_connection(2, 4, 1)
grafo.add_connection(3, 4, 1)


grafo.show_nodes()



def djikstra(grafo: Graph , root,destination):
    grafo.nodes[root].dist = 0
    final_path = list()
    aux = root
    heap = []
    for i in grafo.nodes[aux].adj_list:
        heappush(heap, (i[0], i[1]))
    heapify(heap)
    for i in range(grafo.size-1):
        aux = heappop(heap)
        aux = aux[0]
        if grafo.nodes[aux].visited == 0:
            for j in grafo.nodes[aux].adj_list:
                cost = j[1] + grafo.nodes[aux].dist
                if cost < grafo.nodes[j[0]].dist:
                    grafo.nodes[j[0]].dist = cost
                    grafo.nodes[j[0]].menor_caminho.append(aux)
                heappush(heap, (j[0], cost))
                heapify(heap)

            grafo.nodes[aux].visited = 1

    final_path.append(root)
    for part in grafo.nodes[destination].menor_caminho:
        final_path.append(part)

    final_path.append(destination)
    print(f"menor caminho partindo de {root} e indo ao node {destination}: {final_path}")
    print(f"custo {grafo.nodes[destination].dist}")


djikstra(grafo, 0, 4)

