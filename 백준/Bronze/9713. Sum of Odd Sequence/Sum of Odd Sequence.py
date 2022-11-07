t=int(input())
test=[]
for _ in range(t):
    n = int(input())
    sum = 0
    i = 1
    while i <= n:
        sum += i
        i += 2
    test.append(sum)
for s in test:
    print(s)