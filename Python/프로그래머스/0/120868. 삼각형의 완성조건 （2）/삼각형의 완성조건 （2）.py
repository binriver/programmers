def solution(sides):
    
    answer = 0
    
    a, b = max(sides), min(sides)
    
    for i in range(a-b+1, a+1):
        answer += 1
            
    for j in range(a+1, a+b):
        answer += 1
        
    return answer