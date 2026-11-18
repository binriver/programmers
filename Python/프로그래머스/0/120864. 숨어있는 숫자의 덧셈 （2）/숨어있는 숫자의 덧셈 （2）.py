def solution(my_string):
    answer = 0
    my_string = [i if i.isdecimal() else "x" for i in my_string]
    my_string = "".join(my_string).split("x")
    
    for i in my_string:
        if i:
            answer += int(i)
            
    return answer
    