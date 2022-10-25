t,m = map(int, input().split())
s = 45
if s - m > 0:
    m = m - s + 60
    t = t - 1
    if t < 0 :
        t = 24 - 1
    print("{} {}".format(t, m))
elif s - m <= 0:
    print("{} {}".format(t, m-s))