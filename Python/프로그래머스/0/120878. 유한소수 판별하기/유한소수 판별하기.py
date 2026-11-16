def solution(a, b):
    def get_gcd(a,b):
        while b > 0:
            a, b = b, a % b
        return a
    a, b = a // get_gcd(a, b), b // get_gcd(a,b)
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
    
    return 1 if b == 1 else 2