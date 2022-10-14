a, b, c = map(int, input().split())
numbers = []

for i in a, b, c:
    numbers.append(i)
    
numbers.sort()
print(numbers[1])
