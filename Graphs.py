class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Graph:

    def __init__(self, vertex):
        self. V = vertex
        self. graph = [None] * self.V

    def addedge(self, src, dest):

        new_node = Node(dest)
        new_node.next = self.graph[src]
        self.graph[src] = new_node

        new_node = Node(src)
        new_node.next = self.graph[dest]
        self.graph[dest] = new_node

    def print_graph(self):
        for i in range(self.V):
            temp = self.graph[i]
            print(i, end="-> ")
            while temp!= None:
                print(temp.data, end="-> ")
                temp = temp.next

            print("\b\b\b", "\n")
        # print(self.graph[i], end=" ")


if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.addedge(0, 1)
    graph.addedge(0, 4)
    graph.addedge(1, 2)
    graph.addedge(1, 3)
    graph.addedge(1, 4)
    graph.addedge(2, 3)
    graph.addedge(3, 4)

    graph.print_graph()