def solution(num_list):
    a = 1
    b = 0
    for i in num_list:
        a *= i
        b += i
    b *= b
    return 1 if a<b else 0