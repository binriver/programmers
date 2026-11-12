def solution(my_string):
    tmp = my_string.split(" ")
    answer = int(tmp[0])
    
    for op in range(1, len(tmp), 2):
        if tmp[op] == "+":
            answer += int(tmp[op+1])
        else:
            answer -= int(tmp[op+1])
    
    return answer