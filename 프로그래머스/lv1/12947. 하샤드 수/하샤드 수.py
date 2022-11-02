def solution(x):
    sum = 0
    x_1 = str(x)
    for i in range(len(x_1)):
        sum += int(x_1[i])
        if x % sum ==0:
            answer = True
        else:
            answer = False
    return answer