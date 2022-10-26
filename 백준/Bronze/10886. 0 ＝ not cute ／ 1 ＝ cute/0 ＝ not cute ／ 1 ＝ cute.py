t = int(input());c = 0;n = 0; test=[]
for _ in range(t):
    test += list(map(int, input()))
    c = test.count(1)
    n = test.count(0)
if c > n:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')