def solution(last_year, changes):

  n = len(last_year)
  indegree = [0]*(len(last_year)+1)

  graph = [set() for _ in range(n+1)]

  for i in range(n):
    node_i = last_year[i]
    indegree[node_i] = n-i-1

    for j in range(i+1, n):
      node_j = last_year[j]
      graph[node_j].add(node_i)


  for (node_i, node_j) in changes:

    j_before_i = False
    for next_node in graph[node_i]:
      if next_node == node_j:
        
        indegree[node_j] -= 1
        indegree[node_i] += 1
        
        j_before_i = True

    if not j_before_i:

      indegree[node_j] += 1
      indegree[node_i] -= 1

  for i in range(n):
    indegree[i+1] = (indegree[i+1], i+1)
  
  indegree.pop(0)
  answer = sorted(indegree, key= lambda x : x[0])

  for i in range(n):
    if answer[i][0] != i:
      return "Impossible"

  return [x[1] for x in answer][::-1]

last_year1 = [5,4,3,2,1]
changes1 = [(2,4), (3,4)]
last_year2 = [2,3,1]
changes2 = []
last_year3 = [1,2,3,4]
changes3 = [(1,2), (3,4), (2,3)]

print(solution(last_year1,changes1))
print(solution(last_year2,changes2))
print(solution(last_year3,changes3))