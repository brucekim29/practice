Round = int(input());Chang = 100;Sang = 100
for n in range(1, Round+1):
    a, b = map(int,input().split())
    if a > b :
        Sang -= a
    elif a < b:
        Chang -= b
    else:
        pass
print(Chang);print(Sang)