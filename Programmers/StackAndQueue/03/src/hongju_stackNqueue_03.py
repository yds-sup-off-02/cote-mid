# def solution(bridge_length, weight, truck_weights):
#     answer = 0

#     bridge = [0] * len(truck_weights)
#     cnt = 0
#     passed = []
#     n_tot_trucks = len(truck_weights)

#     while len(passed) != n_tot_trucks:
#         cnt += 1

#         # Shift bridge
#         if bridge[0]:
#             passed.append(bridge.pop(0))

#         # Append to bridge that
#         # Pop from truck_weights
#         if \
#             truck_weights and \
#             ((sum(bridge) + truck_weights[0]) < weight) and \
#             (not bridge[-1]) \
#         : # not bridge[-1] -> bridge_length
#             bridge.append(truck_weights.pop(0))

#     print(answer)
#     return answer

def solution(bridge_length, weight, truck_weights):
    answer = 0 # Cycle

    bridge = [0] * bridge_length

    # 'bridge' queue만 가지고 풀이
    while len(bridge):
        answer += 1

        # Mod. bridge
        bridge.pop(0)

        # 'bridge_lentgh'의 길이에 성능이 크게 영향을 받지만, 코드가 간결
        # 보낼 truck이 남아있는가?
        if truck_weights:
            # 다리 하중 검사
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            # 무게를 견딜 수 없으면
            else:
                bridge.append(0) # Queue의 크기 유지를 위한 append

    # print(answer)
    return answer

'''
Q. 트럭이 다리를 전부 건너는데 최소 몇 초가 필요한가?

Input
    다리의 길이(트럭 수용 가능 대수)
    다리의 트럭 수용 가능 무게
    트럭 각각의 무게

Output
    최소 소요 시간(초 단위)

Watch for
    bridge_length
'''
solution(2,	10,	[7,4,5,6])
solution(100, 100, [10])
solution(100, 100, [10,10,10,10,10,10,10,10,10,10])