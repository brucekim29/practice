test = int(input())

for i in range(test):
    a, b = map(int, input().split())
    print("Case #{}: {}" .format(i+1, a + b))