def solution(dots):
    dots = sorted(dots)
    
    return (dots[-1][0] - dots[0][0]) * (dots[-1][1] - dots[0][1])