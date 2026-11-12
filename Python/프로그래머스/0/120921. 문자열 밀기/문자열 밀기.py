def solution(A, B):
    answer = 0
    while answer < len(A) and A != B:
        A = A[-1] + A[:-1]
        answer += 1
    return -1 if answer == len(A) else answer