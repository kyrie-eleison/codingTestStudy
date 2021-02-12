def solution(board):
    answer = 0
    n = len(board)
    array = board
    visited = set()
    
    BFS = [(((0,0), (0,1)), "h")]

    while BFS:
        len_bfs = len(BFS)

        
        for _ in range(len_bfs):
            location1, location2, status = BFS.pop(0)
            if location2 == (n-1, n-1):
                return answer
            
            if status == "h":
                below1, below2 = (location1[0]+1, location1[1]), (location2[0]+1, location2[1])
                up1, up2 = (location1[0]-1, location1[1]), (location2[0]-1, location2[1])
                right1, right2 = location2, (location2[0], location2[1]+1)
                left1, left2 = (location1[0], location1[1]-1), location1

                rotate_rd1, rotate_rd2 = location2, (location2[0]+1, location2[1])
                rotate_ru1, rotate_ru2 = (location2[0]-1, location2[1]), location2
                rotate_ld1, rotate_ld2 = location1, (location1[0]+1, location1[1])
                rotate_lu1, rotate_lu2 = (location1[0]-1, location1[1]), location1

                nochange = [(below1, below2), (up1, up2), (right1, right2), (left1, left2)]
                change = [((rotate_ld1, rotate_ld2), (below1, below2)), ((rotate_lu1, rotate_lu2), (up1, up2)), ((rotate_rd1, rotate_rd2), (below1, below2)), ((rotate_ru1, rotate_ru2), (up1, up2))]

                for move in nochange:
                    if good_move(move, array, visited):
                        visited.add(move)
                        BFS.append((move, "h"))

                for move in change:
                    if good_rotate(move, array, visited):
                        visited.add(move[0])
                        BFS.append((move[0], "v"))

                    
            
            else:
                below1, below2 = location2, (location2[0]+1, location2[1])
                up1, up2 = (location1[0]-1, location1[1]), location1
                right1, right2 = (location1[0], location1[1]+1), (location2[0], location2[1]+1)
                left1, left2 = (location1[0], location1[1]-1), (location2[0], location2[1]-1)

                rotate_rd1, rotate_rd2 = location2, (location2[0], location2[1]+1)
                rotate_ru1, rotate_ru2 = location1, (location1[0], location1[1]+1)
                rotate_ld1, rotate_ld2 = (location2[0], location2[1]-1), location2
                rotate_lu1, rotate_lu2 = (location1[0], location1[1]-1), location1

                nochange = [(below1, below2), (up1, up2), (right1, right2), (left1, left2)]
                change = [((rotate_ld1, rotate_ld2), (left1, left2)), ((rotate_lu1, rotate_lu2), (left1, left2)), ((rotate_rd1, rotate_rd2), (right1, right2)), ((rotate_ru1, rotate_ru2), (right1, right2))]
                
                for move in nochange:
                    if good_move(move, array, visited):
                        visited.add(move)
                        BFS.append((move, "v"))

                for move in change:
                    if good_rotate(move, array, visited):
                        visited.add(move[0])
                        BFS.append((move[0], "h"))
                

        answer += 1


def good_move(location, array, visited):

    if location in visited:
        return False

    n = len(array)
    ((x1, y1), (x2, y2)) = location
    coords = [(x1, y1), (x2, y2)]
    
    for coord in coords:
        x, y = coord
        if not ((0 <= x <= n-1 and 0 <= y <= n-1) and array[x][y] == 0):
            return False 

    return True

def good_rotate(location, array, visited)

    (location, move_location) = location

    if location in visited:
        return False

    n = len(array)
    ((x1, y1), (x2, y2)) = move_location
    coords = [(x1, y1), (x2, y2)]
    
    for coord in coords:
        x, y = coord
        if not ((0 <= x <= n-1 and 0 <= y <= n-1) and array[x][y] == 0):
            return False 

    return True