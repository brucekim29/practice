def solution(x, n):
    answer = []
    if x == 0:
        answer = [0]*n
    else:
        y = (1+n)*x
        for i in range(x,y,x):
            answer.append(i)
    return answer