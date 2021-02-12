#BFS
def solution(x):
    answer = 0
    BFS = [x]

    while BFS:
        breadthLen = len(BFS)
        for _ in range(breadthLen):
            node = BFS.pop(0)
            if node == 1:
                return answer

            if node%5 == 0:
                BFS.append(int(node/5))
            if node%3 == 0:
                BFS.append(int(node/3))
            if node%2 == 0:
                BFS.append(int(node/2))
            BFS.append(node - 1)
        print(BFS)
        print("###")
        answer += 1

#DP
d = [0]*100
def solution2(n):

    if n == 1:
        d[0] = 0
        return 0

    x = 2
    while x <= n:
        a_2, a_3, a_5, a_minus = 0,0,0,0
        
        if x%2 == 0:
            a_2 = d[int(x/2)-1]
        if x%3 == 0:
            a_3 = d[int(x/3)-1]
        if x%5 == 0:
            a_5 = d[int(x/5)-1]
        a_minus = d[x-2]

        d[x-1] = min(a_2, a_3, a_5, a_minus) + 1

    return d[n-1]

            
        