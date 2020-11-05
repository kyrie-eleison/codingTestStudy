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
    a,b,c = map(int, input.slice())
    graph[a] = (b,c)

for i in range(1, m+1):
    if graph[i]:
        table[i][graph[i][0]] = graph[i][1]

for i in range(1, n+1):
    for j in range(1, n+1):
        if j != i:
            for k in range(1, n+1):
                if (k =! i) and (k != j):
                    D_jk = table[j][k]
                    D_ji, D_ik = table[j][i], table[i][k]

                    D_jk = min(D_jk, (D_ji + D_ik))







