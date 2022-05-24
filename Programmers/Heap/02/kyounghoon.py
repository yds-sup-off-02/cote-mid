import heapq

def solution(jobs):
    '''
    각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs가 매개변수로 주어질 때, 
    작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지 
    return 하도록 solution 함수를 작성해주세요. (단, 소수점 이하의 수는 버립니다)
    '''
  
    
    working_list = [[w_t, r_t] for r_t, w_t in jobs] # swap positions // ref) r_t(request_time), w_t(working_time)
    
    first = working_list[0]
    working_list = working_list[1:]
    
    heapq.heapify(working_list)
    
    cum_w_t = first[0] # cumulative working time
    cum_idle_t = 0

    for w_t, r_t in working_list: # calculate cum_w_t and cum_idle_t
        idle = cum_w_t - r_t
        cum_w_t += w_t
        cum_idle_t += idle

    answer = int((cum_w_t + cum_idle_t) / (len(working_list) + 1))
    
    return answer
