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
            
    if a > 0 and b > 0:
        return f"x + {b}" if a == 1 else f"{a}x + {b}" 
    elif a > 0 and b == 0:
        return f"x" if a == 1 else f"{a}x"
    elif a == 0 and b > 0:
        return f"{b}"