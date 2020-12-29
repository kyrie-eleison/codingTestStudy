#I think this question is rather BFS than DP

def solution(n):
    
    d = [0]*(30*10)
    d[1] = 1

    BFS = [1]
    total = 0
    while total <= n:
        BFS_len = len(BFS)
        total += BFS_len
        
        for _ in range(BFS_len):
            currentNode = BFS.pop(0)
            two = currentNode*2
            three = currentNode*3
            five = currentNode*5

            BFS += [two, three, five]
            d[two], d[three], d[five] = 1, 1, 1

    count = 0
    x = 1
    while count < n:
        if d[x] == 1:
            count += 1
        x += 1
        
    return x-1


        
        
        

    