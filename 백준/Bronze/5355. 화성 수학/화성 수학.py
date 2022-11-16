t = int(input())
for _ in range(t):
    test = list(input().split())
    test[0] = float(test[0])
    for i in range(1, len(test)):
        if test[i] == '@':
            test[0]*=3
        elif test[i] == '%':
            test[0] += 5
        else:
            test[0] -= 7
    print("{:.2f}".format(test[0]))