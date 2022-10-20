k, n, m = map(int, input().split())
out = (k*n)-m

if out < 0 :
    out=0
print(out)