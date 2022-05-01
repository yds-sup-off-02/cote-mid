def solution(genres, plays):
    answer = []

    # '''
    # {
    #     'classic': {
    #         0: 500,
    #         2: 150,
    #         3: 800,
    #         ...
    #     },
    #     'pop': {
    #         1: 600,
    #         4: 2500,
    #         ...
    #     },
    #     ...
    # }
    # '''

    # melon_hash = {}
    # melon_inner_hash = {}
    
    # for i in range(len(genres)):
    #     if genres[i] not in melon_hash:
    #         melon_hash[genres[i]] = plays[i]
    #     else:
    #         melon_hash[genres[i]] += plays[i]

    genres_dict = {}
    genres_list = []

    for i in range(len(genres)):
        if genres[i] not in genres_dict:
            genres_dict[genres[i]] = []
        
        genres_dict[genres[i]]\
            .append(
                [i, plays[i]]
            )
    '''
        genres_dict ==
        {
            'classic': [
                [0, 500], [2, 150], [3, 800]
            ], 
            'pop': [
                [1, 600], [4, 2500]
            ]
        }
    '''
    # print(genres_dict)

    for g in genres_dict:
        # g == 'classic', 'pop'
    
        genres_dict[g].sort(
            key=lambda x: x[1], # e.g. 800, 500, 150
            reverse=True # Descending
        ) # Sort values. e.g. [3, 800], [0, 500], [2, 150]
        genres_list.append(
            [g, sum(
                    # Genetate array to get summary.
                    [play for _, play in genres_dict[g]]
                    # play's e.g. 800, 500, 150.
                    # [800, 500, 150]
                )
            ]
        ) # Init second hash. e.g. [ ['classic', 1450], ['pop', 3100] ]
    # print(genres_dict)
    # print(genres_list)

    genres_list.sort(
        key=lambda x: x[1],
        reverse=True # Descending
    )
    # Sort values. e.g. [ ['pop', 3100], ['classic', 1450] ]
    # print(genres_list)

    for g, _ in genres_list:
        answer.extend( # extend => Append iterable item.
            [x[0] for x in genres_dict[g][:2]] # Top 2 songs
            # x == [4, 2500]
            # x[0] == Song's ID. e.g. 4
        )
    # print(answer)

    return answer

solution(["classic", "pop", "classic", "classic", "pop"],
    [500, 600, 150, 800, 2500])