def solution(n, k):
    price = n * 12000 + k * 2000
    x = n // 10
    answer = int(price - (x * 2000))
    return answer