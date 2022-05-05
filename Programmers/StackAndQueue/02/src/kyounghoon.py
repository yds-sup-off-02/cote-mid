def solution(priorities, location):
    
    '''
    우선순위 list를 우선순위에 맞춰 정렬하여 
    location 위치에 해당하는 값을 return해 주는 함수
    '''
    
    transit_list = [] # 우선순위에 맞춰 변환된 값을 저장하는 list
    
    # 아래 두줄은 우선순위와 index를 묶어 2차원 배열로 만들어줌
    # combination = list(enumberate(priorities)) 와 비슷한 결과 (호현님 idea)
    indice = [x for x in range(len(priorities))]
    combination = [[x, y] for x, y in zip(priorities, indice)]

    # combination list 길이가 바뀌어도 계속 새롭게 looping하도록 함
    while len(transit_list) < len(priorities):
        for arr in combination:
            # combination에 한가지 항목만 남은 경우 처리
            if len(combination) == 1:
                transit_list.append(arr)
                break
            # if arr == max(combination): # max 함수가 2차원일 때 1차원의 값이 같을 경우 2차원의 값을 비교함
            # arr가 최우선 순위인 경우 pop하여 transit에 저장
            if arr[0] == max(list(zip(*combination))[0]):
                transit_list.append(combination.pop(combination.index(arr)))
                # print('max  :', combination)
                break
            # arr가 최우선순위가 아닌 경우 가장 뒤로 옮김
            else:
                tmp = combination.pop(combination.index(arr))
                combination.append(tmp)
                # print('else: ', combination)
                break
    
    # transit에 우선순위에 맞춰 저장된 값 중 뒤쪽에 기존 위치값만 저장
    final_list = [i[1] for i in transit_list]
    
    answer = final_list.index(location) + 1
    
    return answer
