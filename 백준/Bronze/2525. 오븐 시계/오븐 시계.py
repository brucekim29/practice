h, m = map(int, input().split())
c = int(input())

for i in range(24):
    if m + c >= 60:
        
        m = m - 60
        h = h + 1
        if h >= 24:
            h = h - 24
print('{} {}' .format(h, m+c))