def solution(A, B, k):
    A = sorted(A)
    B = sorted(B)

    for i in range(k):
        if A[i] < B[len(B)-1-i]:
            A[i] = B[len(B)-1-i]
        else:
            break

    return sum(A)