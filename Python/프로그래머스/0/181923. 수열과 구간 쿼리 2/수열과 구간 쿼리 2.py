def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        tmp = 1000001
        for i in range(s, e+1):
            if k < arr[i] < tmp:
                tmp = arr[i]
        answer.append(-1 if tmp == 1000001 else tmp)
    return answer