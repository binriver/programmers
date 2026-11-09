def solution(arr):
    answer = []
    for i in arr:
        tmp = [i] * i
        answer += tmp
    return answer