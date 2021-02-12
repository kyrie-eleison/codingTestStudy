#!usr/bin/python3

graph = [[], [(2, 1), (3, 1)], [(4, 1)], [(2, 1), (6, 1)], [(3, 1)], [(2, 1)], []]

from heapq import *
import copy

def solution(graph):
    graph_copy = copy.deepcopy(graph)
    n = len(graph)
    for i in range(1, n):
        for (node, _) in graph[i]:
            graph_copy[node].append((i, 1))

    graph = graph_copy
    
    INFTY = int(10e9)
    distance_table = [INFTY] * n
    distance_table[1] = 0
    heap = [(0, 1)]

    while heap:
        current_distance, current_node = heappop(heap)

        for (next_node, next_distance) in graph[current_node]:
            cost = next_distance + current_distance
            if cost < distance_table[next_node]:
                distance_table[next_node] = cost
                heappush(heap, (cost, next_node))

    # Find the answer
    for i in range(n):
        if distance_table[i] == INFTY:
            distance_table[i] = -1
    max_number = max(distance_table)
    max_index = []
    count = 0
    for i in range(1, n):
        if max_number == distance_table[i]:
            max_index.append(i)
            count += 1
    
    return (min(max_index), max_number, count)

if __name__ == "__main__":
    print(solution(graph))
