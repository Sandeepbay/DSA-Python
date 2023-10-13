# A Single Source Problem is about finding a path between a given vertex (source) to all the other bertices in a graph such that the total distance between them is the minimum.

# Breadth First Search Method works in unweighted Graph only. It doesnt work for weighted Graph.
# DFS doesnt work in finding the Single Source Shortest Path.


class Graph:
    def __init__(self, gDict = None):
        if gDict is None:
            gDict = {}
        self.gDict = gDict

    def bfs(self , start , end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.gDict.get(node , []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)

customDict = {
    "a" : ["b" , "c"],
    "b" : ["d" , "g"],
    "c" : ["d" , "e"],
    "d" : ["f"],
    "g" : ["f"],
    "e" : ["f"],
}
new_dict = Graph(customDict)
print(new_dict.bfs("a" , "f"))