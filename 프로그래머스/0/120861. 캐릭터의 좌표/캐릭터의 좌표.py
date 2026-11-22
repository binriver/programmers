def solution(keyinput, board):
    move = {"up":(0,1), "down":(0,-1), "left":(-1,0), "right":(1,0)}
    answer =[0,0]
    x_lim, y_lim = board[0]//2, board[1]//2
    
    for m in keyinput:
        dx, dy = move[m]
        if -x_lim <= answer[0] + dx <= x_lim and -y_lim <= answer[1] + dy <= y_lim:
            answer[0] += dx
            answer[1] += dy
        else:
            pass
        
    return answer