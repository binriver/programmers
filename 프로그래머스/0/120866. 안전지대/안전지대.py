def solution(board):
    bomb = []
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == 1:
                bomb.append((i, j))
                
    for i, j in bomb:
        for a in range(i-1, i+2):
            for b in range(j-1, j+2):
                if 0 <= a < len(board) and 0 <= b < len(board):
                    board[a][b] = 1
    
    
    return sum([n.count(0) for n in board])