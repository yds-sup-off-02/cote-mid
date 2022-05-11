def solution(bridge_length, weight, truck_weights):
    '''
    solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 
    다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다. 
    이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.
    '''
    
    total_weight = sum(truck_weights) 
    waiting_list = truck_weights # 변수명이 마음에 안들어서 변경
    moving_list = [] # 다리 위에 있는 트럭을 나타내는 리스트
    arrived_weight = 0 # 도착한 트럭의 무게를 저장하는 변수
    count = 0

    # 선두에 있는 트럭의 무게가 weight보다 큰 경우는 없다고 가정
    while True:
        if len(waiting_list) > 0: # index out of range 방지
            head = waiting_list[0] # 대기하고 있는 트럭 중 맨 앞의 트럭 무게
        
        # 다리 위의 트럭무게와 대기 하는 트럭 중 맨 앞의 트럭무게의 앞이 한계하중량 보다 작으면
        if (sum(moving_list) + head) <= weight and len(waiting_list) > 0:  
            moving_list.append(waiting_list.pop(0)) # 대기줄에서 다리위 리스트로 옮기기
            count += 1

        # 다리 위의 트럭무게에 여유가 없으면
        else:
            if (len(moving_list) >= bridge_length): # 다리 위가 트럭으로 꽉차서 넘어가면 다리위에서 도착 리스트로 옮기기
                arrived_weight += moving_list.pop(0)
            else:
                count += 1
                moving_list.append(0) # 트럭이 종착지를 향해 이동하는 것을 의미함
        
        if arrived_weight == total_weight: # arrived_weight의 합계값이 기존 리스트의 합계값과 일치하면 loop 종료 후 count값 return
            break            
    
    answer = count + 1 # 마지막 카운트를 못하기 때문에 1을 더함
    return answer
