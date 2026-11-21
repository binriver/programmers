def solution(n):
    i = 1
    num = 1
    while num*i < n:
        i += 1
        num *= i
    return i