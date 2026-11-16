def solution(a, b):
    def get_gcd(a,b):
        while b > 0:
            a, b = b, a % b
        return a
    a, b = a // get_gcd(a, b), b // get_gcd(a,b)
    while b > 1:
        if b % 10 == 0:
            b /= 10
        elif b % 5 == 0:
            b /= 5
        elif b % 2 == 0:
            b /= 2
        else:
            return 2
    return 1