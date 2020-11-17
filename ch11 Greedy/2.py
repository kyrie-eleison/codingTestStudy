def solution(array):

    answer = int(array[0])

    for num in array[1:]:
        num = int(num)
        if (num == 0 or num == 1):
                answer += num
        else:
            if (answer == 0 or answer == 1):
                answer += num
            else:
                answer *= num
    
    return answer
