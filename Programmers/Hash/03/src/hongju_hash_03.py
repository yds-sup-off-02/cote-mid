import collections

def solution(clothes):
    answer = 0
    my_hash = {}

    # Init Hash
    for product, cat in clothes.itmes(): # category
        if my_hash.key(cat):
            my_hash[cat] = 1
        else:
            my_hash[cat] += 1

    # Counting cases
    # Get max(Kind of Categories)
    cat_max = len(my_hash) # == my_hash.keys()

    tmp = 1 # Minimum number of case >= 1

    for n in my_hash.values():
        for i in range(1, cat_max + 1):
            n * 1

    print(answer)
    return answer

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