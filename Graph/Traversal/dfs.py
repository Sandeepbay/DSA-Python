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
    
    def dfs(self , vertex):
        visited = set()
        stack = [vertex]
        while stack:
            currentVertex = stack.pop()
            if currentVertex not in visited:
                print(currentVertex)
                visited.add(currentVertex)
            for other_vertex in self.gList[currentVertex]:
                if other_vertex not in visited:
                    stack.append(other_vertex)


# All Operatins carried out
customGraph = Graph()
customGraph.addVertex("A")
customGraph.addVertex("B")
customGraph.addVertex("C")
customGraph.addVertex("D")
customGraph.addVertex("E")
customGraph.addEdge("A","B")
customGraph.addEdge("A","C")
customGraph.addEdge("B","A")
customGraph.addEdge("B","E")
customGraph.addEdge("C","A")
customGraph.addEdge("C","D")
customGraph.addEdge("D","C")
customGraph.addEdge("D","E")
customGraph.addEdge("E","B")
customGraph.addEdge("E","D")
customGraph.printGraph()
customGraph.dfs("A")