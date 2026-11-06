def solution(todo_list, finished):
    answer = []
    for x, fin in zip(todo_list, finished):
        if not fin:
            answer.append(x)
    return answer