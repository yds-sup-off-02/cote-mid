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

# Same-name runner:
def solution(participant, completion):
    answer = ''

    my_hash = {}
    # ls_0 = []
    # ls_1 = []

    # # Add to Hash with comparison
    # for runner in participant:
    #     if runner in completion:
    #         ls_0.append(runner)
    #     else: # Not in completion
    #         ls_1.append(runner)

    #     my_hash[0] = ls_0
    #     my_hash[1] = ls_1

    # # Mod. answer
    # for runner in my_hash: # .keys()
    #     if not my_hash[runner]: # == 0 == False
    #         answer = runner

    # Generate Hash
    for runner in participant:
        if my_hash[runner] != 0:
            my_hash[runner] += 1
        else:
            my_hash[runner] = 1

    # Modifier
    for key in my_hash: # keys()
        if key in completion:
            my_hash[key] -= 1

    # Checker
    for key in my_hash:
        if my_hash[key] != 0:
            answer = key
    
    return answer

solution(
    ["leo", "kiki", "eden"],
    ["eden", "kiki"]
)