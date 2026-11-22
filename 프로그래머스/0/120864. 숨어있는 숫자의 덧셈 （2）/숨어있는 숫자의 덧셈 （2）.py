def solution(my_string):
    answer = 0
    my_string = [i if i.isdecimal() else " " for i in my_string]
    my_string = "".join(my_string).split()
            
    for i in my_string:
        answer += int(i)
        
    return answer
    