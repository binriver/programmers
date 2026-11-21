def solution(numbers, k):
    i = 0
    while k > 1:
        if i+2 < len(numbers):
            i += 2
        elif i+2 == len(numbers):
            i = 0
        else:
            i = 1
        k -= 1
    return numbers[i]