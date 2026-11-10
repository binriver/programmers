def solution(n):
    answer = [[0] * n for _ in range(n)]
    x, y, d = 0, 0, 0
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    for i in range(1, n*n+1):
        answer[x][y] = i
        if 0 <= x+dx[d] < n and 0 <= y+dy[d] < n and answer[x+dx[d]][y+dy[d]] == 0:
            x += dx[d]
            y += dy[d]
        else:
            d = (d+1) % 4
            x += dx[d]
            y += dy[d]
        
    return answer