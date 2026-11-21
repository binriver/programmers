def solution(n):
    numbers = []
    answer = []
    for i in range(2, 10001):
        k = 2
        while k != i:
            if i % k == 0:
                break
            k += 1
        if k == i:
            numbers.append(k)
    for k in numbers:
        if k > n:
            break
        else:
            if n % k == 0:
                answer.append(k)
    return answer