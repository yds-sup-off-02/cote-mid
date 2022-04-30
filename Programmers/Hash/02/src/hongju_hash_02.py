def solution(phone_book):
    # # Non Hash
    # for std in phone_book:
    #     sameone_flag = True

    #     for chk in phone_book:
    #         if sameone_flag:
    #             sameone_flag = False
    #             continue
    #         else:
    #             if 

    # answer = True
    # return answer

    # -------------------------------------
    answer = True
    my_hash = {}
    
    # Init Hash
    for number in phone_book:
        my_hash[number] = 1

    # Processing
    for number in phone_book:
        tmp = ''

        for digit in number:
            tmp += digit

            if tmp in my_hash and tmp != number: # in my_hash.keys()
                answer = False
    # print(answer)
    return answer

solution(["119", "97674223", "1195524421"]) # False
solution(["123","456","789"]) # True
solution(["12","123","1235","567","88"]) # False