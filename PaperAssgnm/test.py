from PaperAssgnm.GraphLab import *

g = UndirectedGraph()

nicholas = Vertex(1)
bing = Vertex(2)
joshua = Vertex(3)
john = Vertex(4)
jenny = Vertex(5)
gina = Vertex(6)

"""
Let's say, 

Nicholas is friends with bing and joshua
John is friends with Joshua
Joshua is friends with Gina and Jenny
"""
g.addEdge(nicholas, bing)
g.addEdge(nicholas, joshua)
g.addEdge(john, joshua)
g.addEdge(joshua, gina)
g.addEdge(joshua, jenny)
g.addEdge(jenny, bing)
g.addEdge(nicholas, gina)

print(bfs_traversal(nicholas))