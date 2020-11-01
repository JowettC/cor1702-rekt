from PaperAssgnm.GraphLab import *

g = UndirectedGraph()

v1 = Vertex('Bing')
g.addVertex(v1)

v2 = Vertex('Nicholas')
g.addVertex(v2)

v3 = Vertex('Josh')
g.addVertex(v3)

v4 = Vertex('Nigel')
g.addVertex(v4)

v5 = Vertex('Shathees')
g.addVertex(v5)

v6 = Vertex('Joen')
g.addVertex(v6)

v7 = Vertex('Angela')
g.addVertex(v7)

v8 = Vertex('Selena')
g.addVertex(v8)

v9 = Vertex('Sam')
g.addVertex(v9)

v10 = Vertex('Emmanuel')
g.addVertex(v10)

v11 = Vertex('Shawn')
g.addVertex(v11)

g.addEdge(v1, v4)
g.addEdge(v1, v10)
g.addEdge(v7, v4)
g.addEdge(v4, v5)
g.addEdge(v4, v2)
g.addEdge(v5, v2)
g.addEdge(v5, v6)
g.addEdge(v2, v6)
g.addEdge(v6, v3)
g.addEdge(v6, v7)
g.addEdge(v3, v7)
g.addEdge(v3, v1)
g.addEdge(v6, v9)
g.addEdge(v9, v10)
g.addEdge(v9, v11)
g.addEdge(v4, v9)
g.addEdge(v5, v10)

print(bfs_traversal(v1))