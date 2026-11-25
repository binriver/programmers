def solution(balls, share):
    T, B = 1, 1
    
    for i in range(1, share+1):
        T *= balls
        balls -= 1
        B *= i
        
    return T/B