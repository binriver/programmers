def solution(ineq, eq, n, m):
    if ineq == ">" :
        if (eq == "=" and n >= m) or (eq == "!" and n > m):
            answer = 1
        else:
            answer = 0
    else:
        if (eq == "=" and n <= m) or (eq == "!" and n < m):
            answer = 1
        else:
            answer = 0
    return answer