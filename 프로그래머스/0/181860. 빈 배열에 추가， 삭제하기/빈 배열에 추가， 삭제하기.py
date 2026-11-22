def solution(arr, flag):
    X = []
    for a, b in zip(arr, flag):
        if b == 1:
            X += [a] * a * 2
        elif b == 0 and len(X) >= a:
            X = X[:-a]
            
    return X