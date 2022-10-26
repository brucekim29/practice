t = list(input())
cm = 10
for i in range(len(t)-1):
    if t[i] == t[i+1]:      
        cm +=5      
    elif t[i] != t[i+1]:
        cm +=10
print(cm)