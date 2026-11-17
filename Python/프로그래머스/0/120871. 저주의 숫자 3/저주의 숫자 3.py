def solution(n):
    answer = 0
    i = 0
    while i != n:
        i += 1
        answer += 1
        while answer % 3 == 0 or "3" in str(answer):
            answer += 1
            
    return answer