def solution(numlist, n):
    answer = []
    for i in numlist:
        if i - n >= 0:
            answer.append([abs(i-n), 1])
        else:
            answer.append([abs(i-n), -1])
    answer = sorted(answer, key=lambda x: (x[0], -x[1]))
    
    result = [n+i*j for i,j in answer[:]]
    
    return result