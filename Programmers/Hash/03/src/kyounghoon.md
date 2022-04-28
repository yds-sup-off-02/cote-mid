from collections import Counter

def solution(clothes):
    
    key_list = []
    value_list = []

    for value, key in clothes:
        key_list.append(key)
        value_list.append(value)

    count_key = dict(Counter(key_list))

    result = 1
    for key in count_key.keys():
        count = count_key[key]
        result = (count + 1) * result

    final_result = result - 1

    return final_result
