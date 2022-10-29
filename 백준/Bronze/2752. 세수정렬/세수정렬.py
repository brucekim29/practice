a,b,c = map(int,input().split())
if a > b > c:
    print(c, b, a)
elif a < b > c and a > c:
    print(c, a, b)
elif c > b > a:
    print(a, b, c)
elif a > b and c > b and a>c:
    print(b, c, a)
elif a > b and c > b and c > a:
    print(b, a, c)
else:
    print(a, c, b)