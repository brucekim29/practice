t = int(input())
answer = []
for _ in range(t):
    x,y = map(int,input().split())
    answer.append(x+y)
for n in range(t):
    print(answer[n])