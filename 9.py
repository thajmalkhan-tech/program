import heapq

def dijkstra(graph,start):
    distances ={node:float('inf') for node in graph}
    distances[start] = 0
    pq=[(0,start)]
    while pq:
       current_dist,current_node = heapq.heappop(pq)
       for neighbor,weight in graph[current_node]:
         distance = current_dist + weight
         if distance < distances[neighbor]:
            distances[neighbor] = distance
            heapq.heappush(pq,(distance,neighbor))

    return distances
#Example
graph={
    'A':[('B',1),('C',4)],
    'B':[('C',2),('D',5)],
    'C':[('D',1)],
    'D':[]
}
print(dijkstra(graph,'A'))