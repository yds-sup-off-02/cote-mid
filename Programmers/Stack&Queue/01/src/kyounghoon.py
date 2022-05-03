def solution(progresses, speeds):
    
    
    '''
    진행도에 작업진행속도(Speeds)를 더해서 순차적으로 100이 넘는 Range를 list를 정리하는 함수
    '''
    
    results = [] # speeds와 progresses를 더한 결과 저장
    final_list = [] # 최종 출력 리스트
    position = 0 # Queue 방식으로 사용이 가능하도록 리스트 내에 시작점을 지정 하는 변수
    
    for i in range(99): # 문제 정의에 맞춰서 최대 99회까지 순환할 가능성이 있어 99로 지정
        
        # 순환한 횟수만큼 스피드에 곱해서 results에 overwriting하기
        results = [x + y*(i+1) for x, y in zip(progresses, speeds)]

        count = 0

        for j in range(position, len(results)):
            if j+1 < len(results): # index out of range 방지
                # 100 넘어가는 index value가 1개인 경우 (position을 활용해서 이전 값이 100이 안되면 count 안되도록 함)
                if (results[position] >= 100 and results[j] >= 100 and results[j+1] < 100):
                    count += 1
                    break
                # 100 넘어가는 index value가 복수인 경우
                elif (results[position] >= 100 and results[j] >= 100 and results[j+1] >= 100):
                    count += 1
                    # j+1로 for문을 돌기 때문에 마지막 2칸을 읽지 못하는 경우가 생겨서 2칸 모두 100이 넘으면 count를 한번 더해주는 방식
                    if results[position] >= 100 and j == (len(results) - 2) and results[-2] >= 100 and results[-1] >= 100:
                        count += 1
                        break                    
            else: # 마지막 index에 도달하게 되면 빠지는 분기문
                if results[position] >= 100 and position == (len(results) - 1) and results[-1] >= 100:
                    count += 1
                    break
    
        if count > 0: # count가 0 이상일때만 리스트에 추가
            final_list.append(count)

        if sum(final_list) > 0:
            position = sum(final_list)

        if position == len(results):
            break
    
    return final_list
