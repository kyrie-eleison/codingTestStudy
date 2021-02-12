orders = [(0,1,3), (1,1,7), (0,7,6), (1,7,1), (0,3,7), (0,4,2), (0,1,1), (1,1,1)]

v = 7
roots = [0]*(v+1)
for i in range(v):
    roots[i+1] = i+1

def rootFinder(node):
    if roots[node] != node:
        roots[node] = rootFinder(roots[node])
    
    return roots[node]

def union(a, b):
    aroot = rootFinder(a)
    broot = rootFinder(b)

    if aroot <= broot:
        roots[broot] = aroot
    else:
        roots[aroot] = broot

for order in orders:
    realOrder, a, b = order
    if realOrder == 0:
        union(a, b)
    else:
        aroot = rootFinder(a)
        broot = rootFinder(b)

        if aroot == broot:
            print('yes')
        else:
            print('no')

