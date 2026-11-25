def solution(num_list, n):
    l = len(num_list)//n
    answer = [[] for i in range(l)]
    for i in range(l):
        for j in range(n):
            answer[i].append(num_list[j])
        num_list = num_list[n:]
    return answer