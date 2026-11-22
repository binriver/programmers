def solution(myStr):
    answer = myStr.replace('a', ' ')
    answer = answer.replace('b', ' ')
    answer = answer.replace('c', ' ')
    
    answer = answer.split()
    
    return answer if answer else ["EMPTY"]