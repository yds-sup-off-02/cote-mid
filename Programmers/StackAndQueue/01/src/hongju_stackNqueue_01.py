def solution(progresses, speeds):
    # return 배열
    answer = []

    # 단위 날짜에 대한 변수: 싸이클 1회(하루)에 1씩 증가하는 특성
    time = 0
    # 배포 작업 수에 대한 변수: 단위 날짜당 몇 개의 작업이 배포되는가
    cnt = 0

    # 작업이 한 개라도 남아있다면 while문을 실행해 반복하여 모든 작업의 배포에 대해 계산하라
    while len(progresses) > 0:
        '''
        만약 progresses의 맨 앞 작업(즉, FIFO 큐의 맨 앞 작업)이 끝났다면
        그것을 제거하고
        그것에 해당하는 speeds 큐의 아이템도 제거하여 바로 다음 작업에 대해 계산하도록 하고
        단위 날짜(하루)에 배포되는 작업의 양에 1을 추가하라
        '''
        if (progresses[0] + time * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)

            cnt += 1
        
        # 그렇지 않고 progresses의 맨 앞 작업(즉, 큐의 맨 앞 작업)이 끝나지 않았다면
        # 더이상 해당 단위 날짜에 배포 가능한 작업이 없다는 이야기이므로 하루를 추가한다
            # 그리고 cnt(배포 작업 수)가 1회 이상 누산 됐다면
            # 정답(리턴 answer 리스트)에 그것을 추가하고(append)
            # 새로운 배포 작업 수 계산을 위해 cnt를 0으로 초기화 한다
                # cnt(카운트)가 1회 미만이라면 해당 단위 날짜에 배포 가능한 작업이 없다는 이야기이므로
                # append 하지 않는다
        # 이후 작업들의 배포 일정 계산을 위해 while문 반복
        else:
            time += 1

            if cnt >= 1:
                answer.append(cnt)
                cnt = 0
            
    answer.append(cnt)
    # print(answer)
    return answer

'''
Q. FIFO 큐의 특성을 고려할 때, 단위 날짜(하루)당 몇 개의 기능이 배포 되는가?
    (FIFO 큐이므로, 어떤 작업이 완료 돼도 반드시 앞의 작업이 완료 돼야 큐에서 나갈 수 있다)
    e.g. 7일째에 2개의 기능, 9일째에 1개의 기능

    Input
        progresses: 작업들 각각의 현재 진행 상태를 나타내는 1차원 배열
        speeds: 그 작업들 각각의 진행 속도를 나타내는 1차원 배열
            (단, 작업 속도는 변하지 않는다고 가정함)

    Output
        1차원 배열 answer:
            단위 날짜(하루)를 기준으로 몇 개의 작업이 동시에 배포되는가?
    
    Keypoint
        FIFO 큐의 이해
'''

solution(progresses=[93, 30, 55], speeds=[1, 30, 5])
# answer == [2, 1]
solution(progresses=[95, 90, 99, 99, 80, 99], speeds=[1, 1, 1, 1, 1, 1])
# answer == [1, 3, 2]