def solution(clothes):
    # answer = 0
    # my_hash = {}

    # # Init Hash
    # for set in clothes:
    #     if set[1] in clothes: # set[1] == Category
    #         my_hash[set[1]] += 1
    #     else: # if False 
    #         my_hash[set[1]] = 1

    # # Counting cases
    
    # # Get max(Kind of Categories)
    # cat_max = len(my_hash) # == my_hash.keys()

    # tmp = 1 # Minimum number of case >= 1

    # for n in my_hash.values():
    #     for i in range(1, cat_max + 1):
    #         n * 1

    # print(answer)
    # return answer

    type_h = {}

    for _, type in clothes:
        if type not in type_h:
            type_h[type] = 2 # Starts with '2'
        else:
            type_h[type] += 1

    cnt = 1
    for v in type_h.values(): # Type: dict_values() 
        cnt *= v

    # print(cnt - 1) # '-1 for None(by condition)
    return cnt - 1

solution([
    ["yellowhat", "headgear"], 
    ["bluesunglasses", "eyewear"], 
    ["green_turban", "headgear"]
])
solution([
    ["crowmask", "face"], 
    ["bluesunglasses", "face"], 
    ["smoky_makeup", "face"]
])