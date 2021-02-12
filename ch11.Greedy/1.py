def solution(array):
    array = sorted(array)

    answer = 0
    curr_anx = 0
    wait = 0

    for i in range(len(array)):
        traveler = array[i]
        curr_anx = traveler
        wait += 1

        if wait == curr_anx:
            answer += 1
            wait = 0

        