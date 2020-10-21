#Solution with recursion

def solution(n,m, location, direction, maps):
    answer = 1
    x = location[0]
    y = location[1]

    if (y <= 0 or maps[x][y-1] == 1) and (y <= 0 or maps[x-1][y] == 1) and (y>= m-1 or maps[x][y+1] == 1) and (x>= n-1 or maps[x+1][y] == 1):
        return answer

    

    if direction == 0:
        direction = 3
        if y <= 0 or maps[x][y-1] == 1:
            return solution(n,m,location, direction, maps)
        else:
            maps[x][y] = 1 
            return solution(n,m,(x,y-1), direction, maps) + 1
    elif direction == 1:
        direction = 0
        if y <= 0 or maps[x-1][y] == 1:
            return solution(n,m,location, direction, maps)
        else:
            maps[x][y] = 1
            return solution(n,m,(x-1,y), direction, maps) + 1
    elif direction == 2:
        direction = 1
        if y>= m-1 or maps[x][y+1] == 1:
            return solution(n,m,location, direction, maps)
        else:
            maps[x][y] == 1
            return solution(n,m,(x,y+1), direction, maps) + 1
    else: 
        direction = 2
        if x>= n-1 or maps[x+1][y] == 1:
            return solution(n,m,location, direction, maps)
        else:
            maps[x+1][y] == 1
            return solution(n,m,(x+1,y), direction, maps) + 1


#Solution in the textbook

def solution(n,m,location,direction,maps):
    history = [[0]*m for _ in  range(n)]
    x = location[0]
    y = location[1]
    history[x][y] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def turnLeft():
        global direction
        direction -= 1
        direction %= 4

    count = 1
    turn_time = 0
    while True:
        turnLeft()
        nx = x + dx[direction]
        ny = y + dy[direction]

        if history[nx][ny] == 0 and maps[nx][ny] == 0:
            history[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_time = 0
            continue

        else:
            turn_time += 1

        if turn_time == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]
            if history[nx][ny] == 0:
                x = nx
                y = ny
            else:
                break
            turn_time = 0



    return count
        
        

# Need of list comprehension
# Use of global keyword
# while True instead of recursion
# Use of dx, dy
        

