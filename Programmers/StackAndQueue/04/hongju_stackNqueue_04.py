# def solution(prices):
#     answer = []

#     while prices:
#         curr_price = prices.pop(0)

#         cnt = 0
#         for other_price in prices:
#             if curr_price <= other_price:
#                 cnt += 1
#             else:
#                 cnt += 1
#                 # Condition 3:
#                 # 3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 
#                 # 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
#                 break;
#         answer.append(cnt)

#     # print(answer)
#     return answer

def solution(prices):
    answer = [0] * len(prices)
    # == calloc() in C

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

'''
Q. 어떤 주식의 가격이 하락하지 않고 몇 초간 유지되었는가?
    (단, 모든 가격의 간격은 1초)

Input
    주식의 1초당 가격 배열 'prices'

Output
    어떤 가격이 하락하지 않고 유지된 기간(초 단위)
'''
# solution([1, 2, 3, 2, 3])