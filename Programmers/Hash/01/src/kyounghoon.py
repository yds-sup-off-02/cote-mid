# 호현님 코드 (매우 창의적)

def solution(participant, completion):
    completion.append('z'*100) #   리스트 길이를 맞춰주고 정렬할때 append한 값이 제일 뒤로 가고 겹치지 않도록
    participant.sort()# 정렬
    completion.sort()#정렬
    for i in range(len(participant)) : #for문을 participant안의 이름의 갯수만큼 반복하게 했습니다.
        if participant[i] != completion[i] : # participant의 i번째 이름이 completion의 i번째 이름이랑 다르면
            answer = participant[i] #answer로 participant의 i번째 이름이 정의되게 했습니다.
            return answer #마지막으로 return값으로 answer에 정의 된 이름이 출력됩니다.
