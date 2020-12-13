#This is a LIS problem

def solution(string1, string2):

    d = [[0]*(len(string2)+1) for _ in range(len(string1)+1)]

    for i in range(1, len(string1)+1):
        for j in range(1, len(string2)+1):
            if string1[i-1] == string2[j-1]:
                d[i][j] = d[i-1][j-1] + 1
            else:
                d[i][j] = max(d[i-1][j], d[i][j-1])

    L_ij = d[len(string1)][len(string2)]

    return len(string2) - L_ij
