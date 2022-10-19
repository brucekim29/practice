def e(a,b):
    while b != 0:
        i = a % b
        a = b
        b = i
    return a
num1 ,num2 = map(int, input().split())
a = e(num1, num2)
answer = num1 * num2 // a
print(a)
print(answer)