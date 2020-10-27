array = []
for _ in range(n):
    a, b = input().split(" ")
    array.append(a,b)

def solution(array):
    arraySorted = sorted(array, key = lambda x: x[1])
    return [x[0] for x in arraySorted]