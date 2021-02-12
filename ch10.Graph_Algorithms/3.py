v, n = 7, 12

roots = [0]*(v+1)
for i in range(v):
    roots[i+1] = i+1

edges = []
for _ in range(n):
    a, b, w = map(int, input().split())
    edges.append((w, a, b))

def rootFinder(node):
    if roots[node] != node:
        roots[node] = rootFinder(roots[node])
    return roots[node]

def union(a, b):
    aRoot, bRoot = rootFinder(a), rootFinder(b)
    
    if aRoot < bRoot:
        roots[bRoot] = aRoot
    else:
        roots[aRoot] = bRoot

total = []
from heapq import *
heapify(edges)

while edges:
    currentNode = heappop(edges)
    w, a, b = currentNode

    aRoot, bRoot = rootFinder(a), rootFinder(b)

    if aRoot != bRoot:
        union(a, b)
        total.append(w)

total.pop()
print(sum(total))
    
    