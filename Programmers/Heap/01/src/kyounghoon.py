def solution(scoville, K):
    
    '''
    섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
    Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때,
    모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.
    '''
    
    scoville.sort() # sorted in ascending order for conducting binary_search

    def amended_binary_search(scoville, K): 
        head, tail = 0, (len(scoville) - 1)

        try: # if K exists in the list
            if scoville.index(K):
                return scoville.index(K)

        except: # if K does not exist in the list
            while True:

                if scoville[-1] < K: # if the last value of the list is smaller than K, it returns whole list 
                    return tail + 1
                
                if scoville[0] > K: # if the first value of the list is greater than K, it returns whole list
                    return tail + 1

                mid = int((head + tail)/2) 

                if scoville[mid] < K: # cutting the list by mid index value
                    head = mid
                else:
                    tail = mid
                
                if head+1 == tail: # return tail index when head meets tail
                    return tail

    tail = amended_binary_search(scoville, K)

    scoville = scoville[:tail]

    answer = 0
    
    while scoville[0] < K:
        try:
            scoville.append(scoville.pop(1) * 2 + scoville.pop(0))
            scoville.sort()
            answer += 1

        except IndexError: # this means there are no values to calculate
            answer = -1
            
    return answer
