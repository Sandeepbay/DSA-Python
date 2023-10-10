# Graph consists of a finite set of vertices or nodes and a set of edges which connect a pair of nodes.

# Vertices - Vertices are the nodes of the graph.
#Edge - The Edge is the line that connect pair of vertices.
#Unweighted Graph - A Graph which does not have a weight associated with any graph.
#Weighted Graph - A Graph which has a weight associated with any edge.
#Undirected Graph - In case the edges of the graph do not have a direction associated with them.
#Directed Graph - If the edges has a direction associated with them.
#Cyclic Graph - A Graph which has at least one loop.
# Acyclic Graph - A Graph with no loop
# Tree - It is a special case of directed Acyclic graph.

# We can represent Graph in two ways - 
# 1. Adjacency Matrix - It is stored in a 2D Matrix.
# 2. Adjacency List - It is stored in the form of a Linked List , where the nodes are stored in the form of the list , while the edges are stored to the respective nodes.

# OLd form of representing a Graph
# class Graph:
#     def __init__(self , gDict=None):
#         if gDict == None:
#             gDict = {}
#         self.gDict = gDict

#     def addEdge(self,vertex,edge):
#         self.gDict[vertex].append(edge)

# customGraph = {
#     "a" : ["b" , "c"],
#     "b" : ["d" , "e"],
#     "c" : ["a" , "e"],
#     "d" : ["b" , "f" , "e"],
#     "e" : ["b" , "d" , "f"],
#     "f" : ["d" , "e"],
# }

# newGraph = Graph(customGraph)
# newGraph.addEdge("b" , "a")
# print(newGraph.gDict)

# New form of representing a graph
class Graph:
    def __init__(self):
        self.gList = {}

    def addVertex(self , vertex):
        if vertex not in self.gList.keys():
            self.gList[vertex] = []
            return True
        return False

    def printGraph(self):
        for vertex in self.gList:
            print(vertex,":",self.gList[vertex])

    def addEdge(self,vertex,edge):
        if vertex in self.gList.keys():
            self.gList[vertex].append(edge)
            return True
        return False

    def removeEdge(self , vertex , edge):
        if vertex in self.gList.keys():
            self.gList[vertex].remove(edge)
            return True
        return False
    
    def removeVertex(self,vertex):
        if vertex in self.gList.keys():
            for other_vertex in self.gList[vertex]:
                self.gList[other_vertex].remove(vertex)
            del self.gList[vertex]
            return True
        return False


customList = Graph()
customList.addVertex("A")
customList.addVertex("B")
customList.addVertex("C")
customList.addEdge("A" , "B")
customList.addEdge("A" , "C")
customList.addEdge("B" , "A")
customList.addEdge("B" , "C")
customList.addEdge("C" , "B")
customList.addEdge("C" , "A")
customList.printGraph()
print("After removing the Edge")
# customList.removeEdge("A" , "B")
#customList.removeVertex("B")
customList.printGraph()

