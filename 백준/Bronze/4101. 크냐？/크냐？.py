l = []
while True:
    a, b = map(int, input().split())
    if a == 0 and b ==0 :
        break
    elif a > b:
        y = 'Yes'
        l.append(y)
    else:
        n = 'No'
        l.append(n)  
for i in l:
    print(i)