def solution(location):
    answer = 8
    horizontalNum = 'abcdefgh'
    
    y = int(location[1]) - 1
    x = horizontalNum.index(location[0])

    first,second = [-2,2], [-1,1]
    print(x,y)
    
    for i in range(2):
        for j in range(2):
            #x first
            x1 = x + first[i]
            y1 = y + second[j]
            #y first
            x2 = x + second[j]
            y2 = y + first[i]
            
            print(x1,y1, x2,y2)
            

            if x1 < 0 or y1 <0 or x1 > 7 or y1 > 7:
                answer -= 1
            if x2 < 0 or y2 <0 or x2 > 7 or y2 > 7:
                answer -= 1

    return answer

def solution2(location): #the solution in the book

    row = int(location[1])
    horizontalNum = 'abcdefgh'
    column = horizontalNum.index(location[0])

    steps = []
    for i in [-2,2]:
        for j in [-1,1]:
            steps.append((i,j))
            steps.append((j,i))
    
    result = 0
    for step in steps:
        next_row = row + step[0]
        next_column = column + step[1]

        if 1 <= next_row <= 8 and 1 <= next_column <= 8:
            result += 1

    return


