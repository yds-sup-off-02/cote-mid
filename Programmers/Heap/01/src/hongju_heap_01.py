'''
"Spicier"

Q. 모든 음식의 스코빌 지수가 7 이상이 되도록 하는 최소 횟수는?
    단, 불가능할 시 return '-1'

Input
    각 음식의 스코빌 지수가 담긴 배열

Output
    모든 음식의 스코빌 지수가 7 이상이 되도록 하는 최소 횟수
'''

def solution(scoville, K):
    answer = 0 # Should be '2'

    import heapq as hq

    hq.heapify(scoville)

    while True:
        first = hq.heappop(scoville) # Heapify real-init
        
        if first >= K:
            break
        if len(scoville) == 0: # Cannot make all itmes >= 7
            return -1

        second = hq.heappop(scoville) # Cycle weight
        hq.heappush(scoville, first + second * 2)
        
        answer += 1
    
    # print(answer)
    return answer

solution([1, 2, 3, 9, 10, 12], 7)