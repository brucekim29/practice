def solution(n):
    answer = 0
    A = []
    for i in range(len(str(n))):
        m = str(n)
        A.append(m[i])
    A.sort()
    for n in range(len(str(n))):
        answer += int(A[n]) * (10**n)
    return answer