def solution(chicken):
    result = 0
    while chicken > 9:
        result += chicken // 10
        coupon = chicken // 10 + chicken % 10
        chicken = coupon
    return result
        