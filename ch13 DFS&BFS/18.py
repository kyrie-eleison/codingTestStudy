# https://programmers.co.kr/learn/courses/30/lessons/60058

def solution(p):
    answer = ""

    if p == "" or good(p):
        return p

    u = p[0:uFunc(p)+1]
    v = p[uFunc(p)+1:]

    if good(u):
        v = solution(v)
        return u + v

    else:
        answer += "("
        answer += solution(v)
        answer += ")"
        u = u[1:-1]
        for s in u:
            if s == "(":
                answer += ")"
            else:
                answer += "(" 

    return answer

def good(p):

    if p == "":
        return True

    stack = [p[0]]

    for i in range(1, len(p)):
        next_s = p[i]

        if next_s == "(":
            stack.append(next_s)

        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(next_s)

    if stack:
        return False
    else:
        return True

def uFunc(p):

    left = 0
    right = 0

    for i in range(len(p)):
        s = p[i]
        if s == "(":
            left += 1
        else:
            right += 1

        if left == right:
            return i
