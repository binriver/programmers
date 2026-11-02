def solution(arr, queries):
    for k in range(len(queries)):
        i, j = queries[k][0], queries[k][1]
        arr[i], arr[j] = arr[j], arr[i]
    return arr