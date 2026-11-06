def solution(num_list):
    k = 0
    for i in num_list:
        while i > 1:
            i //= 2
            k += 1
        
    return k