def solution(num, total):
    answer = [i for i in range(1, num+1)]
    
    s = (total - sum(answer)) // num
    
    for k in range(len(answer)):
        answer[k] += s
    
    return answer