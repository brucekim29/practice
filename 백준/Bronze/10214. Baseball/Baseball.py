t = int(input())
a_t = 0
b_t = 0
for a in range(0, t):
    for i in range(1,10):
        a,b = map(int, input().split())
        a_t += a
        b_t +=b
    if a_t > b_t:
        print('Yonsei')
    elif a_t < b_t:
        print('Korea')
    else:
        print('Draw')