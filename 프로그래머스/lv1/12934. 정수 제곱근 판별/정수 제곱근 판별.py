def solution(n):
    for i in range(0,n+1):
        if i * i ==n:
            answer = i+1
            return answer*answer
        else:
            answer = -1
    return answer