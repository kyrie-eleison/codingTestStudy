#!usr/bin/python3

orders = [(1, 5), (3, 4), (4, 2), (4, 6), (5, 2), (5, 4)]
n = 6

def solution(orders, n):
    INFTY = int(10e9)
    graph = [[INFTY] * n for _ in range(n)]

    for (node1, node2) in orders:
        graph[node1 - 1][node2 - 1] = 1

    # FW Algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])
    
    # Change INFTY into zeros
    for i in range(n):
        for j in range(n):
            if graph[i][j] == INFTY:
                graph[i][j] = 0

    # Find the answer: the count of nonzero elements of a row and a column must be 5
    answer = []

    for i in range(n):
        row = graph[i]
        column = [graph[x][i] for x in range(n)]
        count = 0
        for element in row:
            if element > 0:
                count += 1
        for element in column:
            if element > 0:
                count += 1
        
        if count == 5:
            answer.append(i+1)
    
    return answer

if __name__ == "__main__":
    print(solution(orders, n))
