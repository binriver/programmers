def solution(polynomial):
    a, b = 0, 0
    polynomial = polynomial.split(" + ")
    for num in polynomial:
        if "x" in num :
            if len(num) >= 2:
                a += int(num.split("x")[0])
            else:
                a += 1
        else:
            b += int(num)        
            
    if a == 0:
        return f"{b}"
    elif a == 1:
        return f"x" if b == 0 else f"x + {b}"
    else:
        return f"{a}x" if b == 0 else f"{a}x + {b}"