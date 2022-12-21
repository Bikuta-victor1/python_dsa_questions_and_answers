from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSort(self):

        # initialize my visited arary with unvisiteds
        visited = [False]* self.V

        # stack to hold fimal result
        stack = []

        for i in range(self.V):
            if visited[i] == False : 
                self.topologicalSortUtil(i, visited, stack)  

        # prints reverse array
        print(stack[::-1])      
    
    def topologicalSortUtil(self,v ,visited, stack):

        # mark vertex as visited
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False : 
                self.topologicalSortUtil(i, visited, stack)
        
        # if there are no neighboring un
        stack.append(v)

# Driver Code
if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
 
    print("Following is a Topological Sort of the given graph")
 
    # Function Call
    g.topologicalSort()
        
    