def solution(n, k):
    answer = 0

    while True:
        quotient = n//k
        remainder = n%k

        if quotient > 0:
            answer += remainder + 1
            n = quotient

        else:
            answer += remainder - 1
            break


    return answer
  
  #Need to be more familiar with quotient/remainder thinking