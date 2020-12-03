#https://programmers.co.kr/learn/courses/30/lessons/42891#
#Use binary search

def solution(food_times, k):
    
    #이분탐색을 이용하여 풀이
    #round_num번 돌면서 먹은 음식의 양이 k보다 작을 때, 그 중 가장 큰 round_num을 구한다
    start, end = 0, max(food_times)
    while True:
        if start > end:
            round_num = end
            break
        
        mid = (start + end)//2
        left = 0
        for food in food_times:
            if food <= mid:
                left += food
            else:
                left += mid
                
        if left == k:
            round_num = mid
            break
        elif left < k:
            start = mid + 1
        else:
            end = mid - 1
            
    #round_num번 회전할 동안 먹은 음식의 양(=지난시간)을 구함
    left_time = 0
    for food in food_times:
        if food <= round_num:
            left_time += food
        else:
            left_time += round_num

    #round_num번 도는 동안 남은 음식들을 체크해가면서 하나씩 먹어가면서, 최초로 k를 넘는 index 구하기
    for i in range(len(food_times)):
        food = food_times[i]
        if food > round_num:
            left_time += 1
            
        if left_time > k:
            return i+1
        
    return -1