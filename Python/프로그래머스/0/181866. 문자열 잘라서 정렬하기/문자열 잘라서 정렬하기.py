def solution(myString):
    answer = myString.split('x')
    answer = [a for a in answer if a != ""]
    answer.sort()
    return answer