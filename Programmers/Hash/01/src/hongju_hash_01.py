# def solution(participant, completion):
#     answer = ''

#     my_hash = {}

#     # Add to Hash with comparison
#     for runner in participant:
#         if runner in completion:
#             my_hash[runner] = 1
#         else: # Not in completion
#             my_hash[runner] = 0

#     # Mod. answer
#     for runner in my_hash: # .keys()
#         if not my_hash[runner]: # == 0 == False
#             answer = runner

#     return answer

# # Same-name runner:
# def solution(participant, completion):
#     answer = ''

#     my_hash = {}
#     # ls_0 = []
#     # ls_1 = []

#     # # Add to Hash with comparison
#     # for runner in participant:
#     #     if runner in completion:
#     #         ls_0.append(runner)
#     #     else: # Not in completion
#     #         ls_1.append(runner)

#     #     my_hash[0] = ls_0
#     #     my_hash[1] = ls_1

#     # # Mod. answer
#     # for runner in my_hash: # .keys()
#     #     if not my_hash[runner]: # == 0 == False
#     #         answer = runner

#     # Generate Hash
#     for runner in participant:
#         if my_hash[runner] != 0:
#             my_hash[runner] += 1
#         else:
#             my_hash[runner] = 1

#     # Modifier
#     for key in my_hash: # keys()
#         if key in completion:
#             my_hash[key] -= 1

#     # Checker
#     for key in my_hash:
#         if my_hash[key] != 0:
#             answer = key
    
#     return answer

# def solution(participant, completion):
#     my_hash = {}

#     # Writing hash
#     for runner in participant:
#        if my_hash[runner] in my_hash.keys():
#         my_hash[runner] += 1 

#     answer = ''
#     print(my_hash)
#     return answer

'''
    Others...
'''

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) -\
        collections.Counter(completion)

    # print(list(answer.keys())[0])
    # print(type(answer.keys()))
    # print(list(answer.keys())[0])

    return list(answer.keys())[0]

# def solution(participant, completion):
#     answer = ''
#     temp = 0
#     dic = {}
#     for part in participant:
#         dic[hash(part)] = part
#         temp += int(hash(part))
#     for com in completion:
#         temp -= hash(com)
#     answer = dic[temp]

#     return answer

solution(
    ["leo", "kiki", "eden"],
    ["eden", "kiki"]
)