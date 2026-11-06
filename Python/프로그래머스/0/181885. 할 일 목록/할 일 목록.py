def solution(todo_list, finished):
    answer = []
    for idx, fin in enumerate(finished):
        if fin == 0:
            answer.append(todo_list[idx])
    return answer