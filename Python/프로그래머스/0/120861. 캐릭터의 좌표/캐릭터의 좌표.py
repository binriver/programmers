def solution(keyinput, board):
    move = {"up":[0,1], "down":[0,-1], "left":[-1,0], "right":[1,0]}
    answer = [0,0]
    maplimit = [board[0]//2, board[1]//2]
    for m in keyinput:
        if maplimit[0]*(-1) <= answer[0] + move[m][0] <= maplimit[0] and maplimit[1]*(-1) <= answer[1] + move[m][1] <= maplimit[1]:
            answer[0] += move[m][0]
            answer[1] += move[m][1]
    return answer