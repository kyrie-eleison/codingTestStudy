#!usr/bin/python3

from heapq import *
space = [[9,0,5,1,1,5,3], [4,1,2,1,6,5,3], [0,7,6,1,6,8,5], [1,1,7,8,3,2,3], [9,4,0,7,6,4,1], [5,8,3,2,4,8,3],[7,4,8,4,8,3,4]]

def solution(space):
    n = len(space)
    graph = [[[] for _ in range(n)] for _ in range(n)]

    moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for x in range(n):
        for y in range(n):
            for (dx, dy) in moves:
                next_x, next_y = x + dx, y + dy
                if (0 <= next_x <= (n - 1)) and (0 <= next_y <= (n - 1)):
                    graph[x][y].append(((next_x, next_y), space[next_x][next_y]))

    return dijkstra(graph, (0, 0), (n - 1, n - 1))

def dijkstra(graph, start, end):
    INFTY = int(10e9)
    n = len(graph)
    distance_table = [[INFTY] * n for _ in range(n)]

    start_x, start_y = start
    distance_table[start_x][start_y] = 0
    heap = [(0, start)]


    while heap:
        current_distance, (current_x, current_y) = heappop(heap)

        for ((next_x, next_y), next_distance) in graph[current_x][current_y]:
            cost = next_distance + current_distance
            if cost < distance_table[next_x][next_y]:
                distance_table[next_x][next_y] = cost
                heappush(heap, (cost, (next_x, next_y)))

    end_x, end_y = end
    print(distance_table)
    return distance_table[end_x][end_y] + space[start_x][start_y]

if __name__ == "__main__":
    print(solution(space))