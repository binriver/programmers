def solution(balls, share):
    T = 1
    for i in range(share+1, balls+1):
        T *= i
    B = 1
    for j in range(1, balls-share+1):
        B *= j
        
    return T/B