def solution(arr):
    i = 0
    while 2 ** i < len(arr):
        i += 1
    return arr + [0] * (2**i-len(arr))