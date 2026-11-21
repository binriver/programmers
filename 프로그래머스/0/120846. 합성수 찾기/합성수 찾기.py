def solution(n):
    answer = 0
    for i in range(1, n+1):
        k, t = 1, 0
        while k <= i and t < 3:
            if i % k == 0:
                t += 1
            k += 1
        if t >= 3:
            answer += 1
    return answer