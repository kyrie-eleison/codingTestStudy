graph = [[], [2, 3], [3, 4], [], []]
visited = [0]*(len(graph)+1)

def solution(graph, k, x):

    dist_array = [None]*(len(graph)+1)
    visited[x] = 1
    dist_array[x] = 0
    dist = -1

    BFS = [x]

    while BFS:
        bfs_len = len(BFS)
        dist += 1
        for _ in range(bfs_len):
            node = BFS.pop(0)
            dist_array[node] = dist

            for next_node in graph[node]:
                if visited[next_node] == 0:
                    visited[next_node] = 1
                    BFS.append(next_node)

    answer = []
    for i in range(1, len(dist_array)):
        if dist_array[i] == k:
            answer.append(i)

    if answer:
        return answer
    else:
        return -1
