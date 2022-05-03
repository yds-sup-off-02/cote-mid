def solution(progresses, speeds):
    
    results = []
    final_list = []
    position = 0
    
    for i in range(101):
        results = [x + y*(i+1) for x, y in zip(progresses, speeds)]
        # print(results)

        count = 0

        for j in range(position, len(results)):
            if j+1 < len(results): # index out of range 방지
                if (results[position] >= 100 and results[j] >= 100 and results[j+1] < 100):
                    count += 1
                    break
                elif (results[position] >= 100 and results[j] >= 100 and results[j+1] >= 100):
                    count += 1
                    if results[position] >= 100 and j == (len(results) - 2) and results[-2] >= 100 and results[-1] >= 100:
                        count += 1
                        break                    
            else: # position이 마지막 index에 도달하면
                if results[position] >= 100 and position == (len(results) - 1) and results[-1] >= 100:
                    count += 1
                    break

        if count > 0:
            final_list.append(count)

        if sum(final_list) > 0:
            position = sum(final_list)

        if position == len(results):
            # print('position: ', position, 'list_length: ', len(results))
            break
        
        # print('position: ', position)
    
    return final_list
