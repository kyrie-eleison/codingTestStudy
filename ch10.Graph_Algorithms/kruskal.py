#Finding loop algorithm(from the disjointSet)

v = 7
root = []
for i in range(v+1):
    root.append(i)

def findRoot(root, x):
    if root[x] != x:
        root[x] = findRoot(root, root[x])
    return root[x]
    
def union(root, a, b):
    aRoot = findRoot(root, a)
    bRoot = findRoot(root, b)

    if aRoot >= bRoot:
        root[aRoot] = bRoot
    else:
        root[bRoot] = aRoot
        
edges = [(29, 1,2), (75, 1, 5), (35, 2, 3), (34, 2, 6), (7, 3, 4), (23, 4, 6), (13, 4, 7), (53, 5, 6), (25, 6, 7)]
edges.sort()

kruskal = []
total_cost = 0
for edge in edges:
    first = edge[1]
    second = edge[2]
    if findRoot(first) != findRoot(second):
        union(root, first, second)
        kruskal.append(edge)
        total_cost += edge[0]
