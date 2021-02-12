#Simple Dijkstra 

n = 6
graph = [[] for _ in range(n+1)]

for _ in range(11):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

    infty = int(1e9)
distance = [infty]*(n+1)
visited = [False]*(n+1)

def get_smallest_node():
    indices = [i for i in range(1,n+1) if visited[i] == False]
    if indices:
        idx = indices[0]
        for i in indices:
            if distance[i] < distance[idx]:
                idx = i
        return idx

def dijkstra(start):

    current = start
    distance[start] = 0

    for _ in range(n):
        print(current)
        visited[current] = True
        if graph[current]:
            relations = graph[current]
            for rel in relations:
                print(rel)
                distance[rel[0]] = min(distance[rel[0]], distance[current] + rel[1])
        print(distance)
        
        current = get_smallest_node()
        print("####")

#Using Set Data Structure

infty = int(10e9)

def dijkstra(graph, start):
  n = len(graph)-1
  table = [infty]*(n+1)
  not_visited = set([i+1 for i in range(n)])

  for (next_node, weight) in graph[start]:
    table[next_node] = weight

  not_visited = not_visited - {start}

  while not_visited:
    next_node = find_min(table, not_visited)
    print(next_node)

    to_add = table[next_node]
    not_visited = not_visited - {next_node}

    for (other_node, weight) in graph[next_node]:
      table[other_node] = min(table[other_node], to_add + weight)
  
  return table
    
  

def find_min(array, index):
  n = len(array)

  min_number = int(10e9)
  min_index = -1
  for i in index:
    if array[i] < min_number:
      min_number = array[i]
      min_index = i

  return min_index

graph = [[], [(2, 2), (3, 5), (4, 1)], [(3, 3), (4, 2)], [(2, 3), (6, 5)], [(3, 3), (5, 1)], [(3, 1), (6, 2)], []]
start = 1

print(dijkstra(graph, start))
    
#Revised Dijkstra

from heapq import *
distance = [infty]*(n+1)

def dijkstra_revised(start):

    distance[start] = 0
    pqueue = [(0,start)]
    
    while pqueue:
        dist, current = heappop(pqueue)
        if dist > distance[current]:
            continue
        
        if graph[current]:
            relations = graph[current]
            for rel in relations:
                cost = dist + rel[1]
                if cost < distance[rel[0]]:
                    distance[rel[0]] = cost
                    heappush(pqueue, (cost, rel[0]))
        print(distance)
        print("####")

#FM

Infty = int(10e9)
n, m = 4, 7
table = [[Infty]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    table[i][i] = 0

for _ in range(m):
    a,b,c = map(int, input().slice())
    graph[a] = (b,c)

for i in range(1, m+1):
    if graph[i]:
        table[i][graph[i][0]] = graph[i][1]

for i in range(1, n+1):
    for j in range(1, n+1):
        if j != i:
            for k in range(1, n+1):
                if (k != i) and (k != j):
                    D_jk = table[j][k]
                    D_ji, D_ik = table[j][i], table[i][k]

                    D_jk = min(D_jk, (D_ji + D_ik))







