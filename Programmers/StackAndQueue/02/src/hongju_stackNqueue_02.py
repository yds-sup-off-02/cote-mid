def solution(priorities, location):
    # 출력 순서 변수 선언
    answer = 0

    # 최고 중요도 변수 정의
    n_max_prior = max(priorities)

    # 내가 원하는 문서의 순서를 알 때까지 반복 연산
    while True:
        # 현재 연산 대상(문서)에 대한 변수 정의(FIFO 큐의 맨 앞 아이템)
        # 동시에 priorities 큐에서 그 값을 제거한다(변수를 정의한 이유중 하나)
        curr_val = priorities.pop(0)

        # 만약 현재 대상(문서)이 가장 중요도가 높다면
        if curr_val == n_max_prior:
            # 현재 문서는 반드시 출력되니, 출력 순서에 1을 더해주고
            answer += 1

            # 동시에 내가 찾는 문서라면(location 변수가 0이라면), 더이상 연산하지 않는다
            if location == 0:
                break
            # 내가 찾는 문서는 아니라면(location 변수가 0이 아니라면)
            # 한 칸씩 앞으로 밀렸으니 내가 찾는 문서의 위치도 한 칸 밀어준다(위치 조정)
            # (location 변수에서 1을 뺀다)
            else:
                location -= 1

            # priorities 큐가 바뀌었으니 최고 중요도를 다시 계산한다
            n_max_prior = max(priorities)

        # 만약 현재 연산 대상의 중요도가 가장 높지는 않다면
        else:
            # 현재 문서를 큐의 맨 뒤에 다시 넣고
            priorities.append(curr_val)

            # 만약 현재 문서가 내가 찾는 문서였다면
            # 내가 찾는 문서의 위치를 큐의 맨 뒤 아이템을 가르키게 한다(위치 조정(
            # (인덱스 연산을 위해 '-1')
            if location == 0:
                location = len(priorities) - 1
            
            # 가장 중요한 문서도 아니고 내가 찾는 문서도 아니었다면
            # 아이템이 한 칸씩 조정되었으니 내가 찾는 문서의 위치를 재조정해준다
            else:
                location -= 1
            
            # 다음 반복 싸이클로 넘어간다

    # print(answer)
    return answer

'''
Q. 중요도를 고려할 때, 내가 원하는 문서는 몇 번째로 출력되는가?
    e.g. 2-1-3-2의 중요도를 가질 때, 3번째 문서(인덱스 2)는 몇 번째에 출력될까?
        첫 번째(1)

    Input
        priorities: 각 문서들의 중요도를 나타내는 1차원 배열
        location: 몇 번째로 출력되는지 알고 싶은 문서의 위치(인덱스 값)
    Output
        내가 원하는 문서는 몇 번째로 출력 되는가(자연수)

    Keypoint
        큐의 조정에 따른 내가 원하는 문서의 위치 조정
'''
solution(priorities=[2, 1, 3, 2], location=2)
solution(priorities=[1, 1, 9, 1, 1, 1], location=0)