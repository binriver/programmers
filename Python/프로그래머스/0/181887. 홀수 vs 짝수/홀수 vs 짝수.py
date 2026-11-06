def solution(num_list):
    odd, even = 0, 0
    for idx, num in enumerate(num_list):
        if idx % 2 == 0:
            odd += num
        else:
            even += num
    return odd if odd >= even else even