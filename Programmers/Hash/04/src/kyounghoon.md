def solution(genres, plays):

    plays_with_abs_idx = {}

    for i in range(len(plays)):
        plays_with_abs_idx[i] = plays[i]

    sorted_plays_with_abs_idx = dict(sorted(plays_with_abs_idx.items(), key=lambda x: x[1], reverse=True))

    unique_genres = list(set(genres))

    indice_genres = {}

    for i in range(len(unique_genres)):
        # result = list(filter(lambda x: genres[x] == unique_genres[i], range(len(genres))))
        result = list(filter(lambda x: genres[x] == unique_genres[i], sorted_plays_with_abs_idx.keys()))
        indice_genres[unique_genres[i]] = result

    total_play = {}

    for i in range(len(unique_genres)):
        count = 0
        for j in range(len(indice_genres[unique_genres[i]])):
            indice_list = indice_genres[unique_genres[i]].copy()
            count += plays[indice_list[j]]

        total_play[unique_genres[i]] = count    

    total_play = dict(sorted(total_play.items(), key=lambda x: x[1], reverse=True))

    answer = []

    for i in total_play:
        if len(indice_genres[i]) > 1:
            answer.append(indice_genres[i][:2])
        else:
            answer.append(indice_genres[i])

    answer = sum(answer, [])
    
    return answer
