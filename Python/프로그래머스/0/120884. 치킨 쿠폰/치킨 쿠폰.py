def solution(chicken):
    result = 0
    coupon = 0
    while chicken >= 10:
        result += chicken // 10
        coupon = chicken // 10 + chicken % 10
        chicken = coupon
    return result
        