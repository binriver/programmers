def solution(arr):
    l_row = len(arr)
    l_col = len(arr[0])
    
    if l_row > l_col:
        for i in range(l_row):
            arr[i] += [0] * (l_row-l_col)
    elif l_row < l_col:
        for j in range(l_col-l_row):
            arr.append([0]*l_col)
    return arr