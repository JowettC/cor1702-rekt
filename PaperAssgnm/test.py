from PaperAssgnm.GraphLab import *

g = UndirectedGraph()

nicholas = Vertex(1)
bing = Vertex(2)
joshua = Vertex(3)
john = Vertex(4)
jenny = Vertex(5)
gina = Vertex(6)
james = Vertex(7)

"""
Let's say, 

Nicholas is friends with bing, gina and joshua
Joshua is friends with Gina and Jenny
John is friends with Joshua
Jenny is friends with Bing
Jenny is friends with James
"""
g.addEdge(nicholas, bing)
g.addEdge(nicholas, joshua)
g.addEdge(john, joshua)
g.addEdge(joshua, gina)
g.addEdge(joshua, jenny)
g.addEdge(jenny, bing)
g.addEdge(nicholas, gina)
g.addEdge(jenny, james)

print(bfs_traversal(nicholas))