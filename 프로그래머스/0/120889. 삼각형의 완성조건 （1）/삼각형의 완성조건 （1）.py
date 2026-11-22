def solution(sides):
    sides = sorted(sides)
    a, b, c = sides[:]
    return 1 if c < a + b else 2