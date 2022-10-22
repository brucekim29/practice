list = []
while True:
    a,b,c, = map(int, input().split())
    for i in a,b,c:
        list.append(i)
    if a==b==c:
        print(10000+a*1000)
        break
    elif a==b or b==c or c==a:
        sorted_list = sorted(list)
        print(1000+sorted_list[1]*100)
        break
    else:
        print(max(list)*100)
        break