

def solution(n):
    answer = 0
    a=[]
    for i in range(1,n+1):
        a.append(i)
    for b in range(1, len(a)+1):
        if b % 2 ==0:
            answer+=b
    return answer