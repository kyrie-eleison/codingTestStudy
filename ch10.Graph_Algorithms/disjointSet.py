#Different from the textbook(using class)

class TreeNode:
    parent = None
    value = None
    def __init__(self, value):
        self.value = value


data = [0]*7
for i in range(1, 7):
    node_i = TreeNode(value = i)
    node_i.parent = node_i
    data[i] = node_i


#Finding parent nodes recursively(O(V*operation numbers))
    
def rootFinder(TreeNode):
    if TreeNode.parent == TreeNode:
        return TreeNode
    
    return rootFinder(TreeNode.parent)

unions = [(1,4), (2,3), (2,4), (5,6)]

for op in unions:
    first, second = data[op[0]], data[op[1]]
    first_root = rootFinder(first)
    second_root = rootFinder(second)
    
    if first_root.value <= second_root.value:
        second_root.parent = first_root
    else:
        first_root.parent = second_root
            
for i in range(1, 7):
    print(rootFinder(data[i]).value)

#Path compression
#Just change the parent => root, and:

def rootFinder(TreeNode):
    if TreeNode.root != TreeNode:
        TreeNode.root = rootFinder(TreeNode.root)
    
    return TreeNode.root

#Implementation as the text:
v = 6
root = []
for i in range(7):
    root.append(i)

def findRoot(root, x):
    if root[x] != x:
        root[x] = findRoot(root, root[x])
    return root[x]
    
def union(root, a, b):
    aRoot = findRoot(root, a)
    bRoot = findRoot(root, b)

    if aRoot >= bRoot:
        root[aRoot] = root[bRoot]
    else:
        root[bRoot] = root[aRoot]
        
unions = [(1,4), (2,3), (2,4), (5,6)]

for op in unions:
    first, second = op[0], op[1]
    
    union(root, first, second)

print(root)


#Application: Figuring out the loops

v = 3
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
        
unions = [(1,2), (1,3), (2,3)]

for op in unions:
    first, second = op[0], op[1]
    if rootFinder(first) != rootFinder(second):
        union(root, first, second)
    else:
        print(first, second, rootFinder(root), " is a loop")

