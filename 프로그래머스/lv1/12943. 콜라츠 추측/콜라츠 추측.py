def solution(num):
    answer = 0
    while num !=1:
        if num % 2 ==0:
            answer += 1
            num = num//2
        else:
            answer += 1 
            num = num * 3 + 1
    return answer if answer <= 500 else -1