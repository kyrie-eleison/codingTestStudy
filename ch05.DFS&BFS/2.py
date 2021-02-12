from collections import deque

def solution(lab):
    start = (0,0)
    queue = deque([start])
    answer = 0

    while queue:

        answer += 1
        breadthLen = len(queue)
        print(list(queue))

        for _ in range(breadthLen):
            node = queue.popleft()
            x,y = node[0], node[1]
            lab[x][y] = 0
            if (x,y) == (len(lab)-1, len(lab[0])-1):
                return answer

            if ((x+1) < len(lab)) and lab[x+1][y] == 1:
                queue.append((x+1,y))
                
            if (y+1) < len(lab[0]) and lab[x][y+1] == 1:
                queue.append((x,y+1))
