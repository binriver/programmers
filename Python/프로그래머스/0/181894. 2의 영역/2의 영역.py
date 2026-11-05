def solution(arr):
    answer = []
    for idx, i in enumerate(arr):
        if i == 2:
            answer.append(idx)   
    if len(answer) == 0:
        return [-1]
    else:
        return arr[answer[0]:answer[-1]+1]