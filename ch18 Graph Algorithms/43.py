def root_finder(graph, parent, node):
if parent[node] != node:
    parent[node] = root_finder(graph, parent, parent[node])
  return parent[node]

def union(graph, parent, a, b):
  rootA = root_finder(graph, parent, a)
  rootB = root_finder(graph, parent, b)

  if rootA <= rootB:
    parent[rootB] = rootA
  else:
    parent[rootA] = rootB
  
def is_cycle(graph, parent, a, b):
  rootA = root_finder(graph, parent, a)
  rootB = root_finder(graph, parent, b)

  if rootA == rootB:
    return True
  else:
    return False


from heapq import *

def solution(graph, n):

  answer = 0
  
  heap = []
  for i in range(n):
    connected_nodes = graph[i]
    
    for (j, w) in connected_nodes:
      heappush(heap, (w, i, j))
      answer += w

  parent = [0]*(n)
  for i in range(n):
    parent[i] = i

  while heap:

    next_least_edge = heappop(heap)
    w, i, j = next_least_edge

    if not is_cycle(graph, parent, i, j):
      union(graph, parent, i, j)
      answer -= w
    else:
      continue

  return answer

graph = [[(1, 7), (3, 5)], [(2, 8), (3, 9), (4, 7)], [(4, 5)], [(4, 15), (5, 6)], [(5, 8), (6, 9)], [(6, 11)], []]
n = 7

print(solution(graph, n))