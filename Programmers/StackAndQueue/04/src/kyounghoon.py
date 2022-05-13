def solution(prices):
    
    '''
    초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 
    가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
    '''

    result = []
    
    while len(prices):
        count = 0
        
        for i in range(len(prices)):
            if len(prices) == 1: # Pop으로 리스트를 줄여나가면서 마지막에 도달한 경우
                result.append(0)
                break
            elif prices[i] - prices[0] < 0: # 고정된 첫번째 값과 비교하는 값의 차를 통해 간격 측정
                result.append(i)
                break
            else: # 비교값이 계속 양수만 나오는 경우
                count += 1 

        if count == len(prices): # 비교값이 끝까지 떨어지지 않았을 경우 처리
            result.append(count - 1)
            
        prices.pop(0)
    
    return result
