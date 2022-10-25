num = int(input())
num_a = 0
count = 0
for i in range(1, num+1):
    num_a += i 
    count += 1
    if num_a == num:
        print(count)
        break
    elif num_a > num:
        print(count - 1)
        break