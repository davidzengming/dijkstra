import heapq

class Graph:
    def __init__(self, v):
        self.adj = [set() for _ in range(v)]
        
    
    def addEdge(self, v1, v2, w):
        self.adj[v1].add((w, v2))
                
    def relax(self, v, distTo, edgeTo, marked, pq):
        
        marked[v] = True
        
        for node in self.adj[v]:
            weight, w = node[0], node[1]
            
            if distTo[w] > distTo[v] + weight:
                distTo[w] = distTo[v] + weight
                edgeTo[w] = v
                heapq.heappush(pq, (distTo[v] + weight, w, v))
    
    def dijkstra(self):
        
        marked = [0] * len(self.adj)
        distTo = [float("inf")] * len(self.adj)
        edgeTo = [-1] * len(self.adj)
        pq = []
        
        distTo[0] = 0
        self.relax(0, distTo, edgeTo, marked, pq)
        
        while pq:
            node = heapq.heappop(pq)
            w = node[1]
            
            if not marked[w]:
                self.relax(w, distTo, edgeTo, marked, pq)
        
        print(distTo)
        print(edgeTo)

g = Graph(5)
g.addEdge(0, 2, 2)
g.addEdge(0, 3, 3)
g.addEdge(0, 4, 5)
g.addEdge(2, 3, 4)
g.addEdge(2, 1, 10)
g.addEdge(1, 3, 2)
g.addEdge(4, 1, 1)

g.dijkstra()

