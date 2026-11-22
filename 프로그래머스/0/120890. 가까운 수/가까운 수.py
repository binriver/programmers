def solution(array, n):
    answer = array[0]
    for i in range(0,len(array)):
        if abs(n - array[i]) < abs(n - answer):
            answer = array[i]
        elif abs(n - array[i]) == abs(n - answer):
            if array[i] < answer:
                answer = array[i]
    return answer