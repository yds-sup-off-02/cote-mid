'''
"Disk Controller"

Q. 모든 작업이 각각 요청부터 종료까지의 소요 시간이 있을 때, 
그것의 모든 평균에 대한 최솟값을 구하라

Input
    [시작시간, 소요시간]이 각각 담긴 2차원 배열

Output
    모든 작업들의 소요시간에 대한 평균이 '최소'가 되는 값
'''

def solution(jobs):
    import heapq as hq
    
    answer = 0
    time = 0
    cycle = 0

    time_before = -1

    heap = []
    hq.heapify(heap)

    while cycle < len(jobs):
        # Consider 'time', Append to 'heap' heap
        for job in jobs:
            if time_before < job[0] <= time:
                # Basis = Cost time, not 'Request time'
                hq.heappush(heap, [job[1], job[0]])

        if heap:
            curr = hq.heappop(heap)
            time_before = time
            # Append Cost time
            time += curr[0]
            # ??????
            answer += time - curr[1]
            cycle += 1
        # No tasks to Run
        else:
            time += 1
    
    answer //= len(jobs) # Truncation
    # print(answer)
    return answer

solution([[0, 3], [1, 9], [2, 6]])