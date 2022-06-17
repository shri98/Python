from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, src, dest):
        self.graph[src].append(dest)

    def fun_DFS(self,v, visited):

        visited.add(v)
        print(v, end = " ")

        for i in self.graph[v]:
            if i not in visited:
                self.fun_DFS(i, visited)

    def DFS(self, v):
        visited = set()

        self.fun_DFS(v, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.DFS(1)