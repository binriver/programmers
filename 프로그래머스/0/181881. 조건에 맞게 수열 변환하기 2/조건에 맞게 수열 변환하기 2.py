def solution(arr):
    M = 0
    for i in range(len(arr)):
        k = 0
        while (arr[i] >= 50 and not arr[i] % 2) or (arr[i] < 50 and arr[i] % 2):
            if arr[i] >= 50 and not arr[i] % 2:
                arr[i] //= 2
            elif arr[i] < 50 and arr[i] % 2:
                arr[i] = arr[i] * 2 + 1
            k += 1
        if k >= M:
            M = k
            
    return M