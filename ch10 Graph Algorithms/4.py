v = 5
graph = [[] for _ in range(v+1)]
indegree = [0]*(v+1)
weight = [0]*(v+1)

for i in range(v):
    timeList =  list(map(int, input().split()))
    weight[i+1] = timeList.pop(0)

    for j in timeList:
        if j != -1:
            graph[j].append(i+1)
            indegree[i+1] += 1


heap = []
for i in range(v):
    if indegree[i+1] == 0:
        heap.append(i+1)

incoming = [set({i}) for i in range(v+1)]
answer = [0]*(v+1)
print(incoming)
while heap:
    currentNode = heap.pop(0)
    answer[currentNode] = sum([weight[i] for i in incoming[currentNode]])
    
    for node in graph[currentNode]:
        indegree[node] -= 1
        incoming[node] = incoming[node].union(incoming[currentNode])
        if indegree[node] == 0:
            heap.append(node)
    

for ans in answer:
    print(ans)




