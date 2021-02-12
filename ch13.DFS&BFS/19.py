#bfs

def solution(array, operations):

    first = array[0]
    BFS = [(first, operations)]
    max_num, min_num = 0,0
    
    for i in range(1, len(array)):
        next_num = array[i]
        len_bfs = len(BFS)

        for _ in range(len_bfs):
            current_num, current_op = BFS.pop(0)
            [p, m, t, d] = current_op

            if p > 0:
                BFS.append((current_num+next_num, [p-1, m, t, d]))
            if m > 0:
                BFS.append((current_num-next_num, [p, m-1, t, d]))
            if t > 0:
                BFS.append((current_num*next_num, [p, m, t-1, d]))
            if d > 0:
                BFS.append((div(current_num, next_num), [p, m, t, d-1]))

        BFS_num = [x[0] for x in BFS]

        max_num = max(BFS_num)
        min_num = min(BFS_num)

    return (max_num, min_num)
        


def div(num, n):
    if num >= 0:
        return num//n
    else:
        return -((-num)//n)

array = [1,2,3,4,5, 6]
operations = [2,1,1,1]

print(solution(array, operations))