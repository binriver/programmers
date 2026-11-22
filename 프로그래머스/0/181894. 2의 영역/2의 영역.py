def solution(arr):
    if 2 not in arr:
        return [-1]
    answer = []
    for idx, i in enumerate(arr):
        if i == 2:
            answer.append(idx)   
    
    return arr[answer[0]:answer[-1]+1]