def solution(arr, queries):
    answer = []
    tmp = []
    for s, e, k in queries:
        for i in range(s, e+1):
            if arr[i] > k:
                tmp.append(arr[i])
        if tmp:
            answer.append(min(tmp))
        else:
            answer.append(-1)
        tmp = []
    return answer