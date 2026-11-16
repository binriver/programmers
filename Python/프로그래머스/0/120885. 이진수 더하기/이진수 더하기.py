def solution(bin1, bin2):
    a, b = int(bin1, 2), int(bin2, 2)
    result = bin(a + b)
    return result[2:]