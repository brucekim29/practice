t = int(input())
for _ in range(t):
    dic = {}
    num = int(input())
    for _ in range(num):
        cost , name = map(str,input().split())
        dic[name]=(int(cost))
    print(max(dic, key=dic.get))