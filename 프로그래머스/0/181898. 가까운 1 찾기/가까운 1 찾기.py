def solution(arr, idx):
    l = len(arr)
    if 1 in arr[idx:l]:
        while idx <= l:
            if arr[idx] == 1:
                answer = idx
                break
            else:
                idx += 1
    else:
        answer = -1    
    return answer