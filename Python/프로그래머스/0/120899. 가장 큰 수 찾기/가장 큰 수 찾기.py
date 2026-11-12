def solution(array):
    for i in range(1, len(array)):
        if array[i-1] < array[i]:
            tmp = [array[i], i]
    return tmp