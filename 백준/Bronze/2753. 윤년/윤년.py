year = int(input())
if year %4 ==0 and year%100 !=0:
    yoon=1
elif year %400==0:
    yoon=1
else:
    yoon=0
print(yoon)