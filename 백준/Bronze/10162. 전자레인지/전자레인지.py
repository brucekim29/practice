import sys
iput = sys.stdin.readline
T = int(input())
A_num = 0;B_num = 0;C_num = 0;cook = 0
while True:
    if T % 10 != 0:
        print(-1)
        break
    elif T >= 300:
        A_num += T // 300
        cook = T % 300
        if cook >= 60:
            B_num += cook // 60
            cook = cook % 60
            C_num += cook //10
        else:
            C_num += cook //10
    elif T >= 60:
        B_num += T // 60
        cook = T % 60
        C_num += cook //10
    else:
        C_num += T // 10
    print(A_num, B_num, C_num)
    break