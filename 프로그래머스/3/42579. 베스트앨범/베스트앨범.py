def solution(genres,plays):
    size = len(genres)
    lst = []
    dict = {}

    for i in range(size):
        lst.append([genres[i], plays[i], i])

        if genres[i] not in dict:
            dict[genres[i]] = plays[i]
        else:
            dict[genres[i]] += plays[i]

    lst = sorted(lst, key = lambda x : (-dict[x[0]], -x[1], x[2]))

    answer = []
    genres_count = {}

    for i in lst:
        if i[0] not in genres_count:
            genres_count[i[0]] = 1
            answer.append(i[2])
        else:
            if genres_count[i[0]] == 2:
                continue
            else:
                genres_count[i[0]] += 1
                answer.append(i[2])
    return answer