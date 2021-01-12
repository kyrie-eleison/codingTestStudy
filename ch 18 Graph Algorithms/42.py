def solution(g, planes):

  answer = 0
  airport = [0]*(g+1)

  for plane in planes:

    g_i = plane
    while True:
      if airport[g_i] == 0:
        airport[g_i] = 1
        break
      else:
        g_i -= 1

    if g_i == 0:
      break
  
  for i in range(g):
      answer += airport[i+1]

  return answer

g1 = 4
planes1 = [4, 1, 1]
g2 = 6
planes2 = [2, 2, 3, 3, 4, 4]

print(solution(g1, planes1))
print(solution(g2, planes2))