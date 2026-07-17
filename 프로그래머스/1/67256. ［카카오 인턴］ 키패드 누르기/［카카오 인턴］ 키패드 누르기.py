def solution(numbers, hand):
    result = ""
    L = [3, 0]
    R = [3, 2]
    
    dict = {}
    dict[1] = [0, 0]
    dict[2] = [0, 1]
    dict[3] = [0, 2]
    dict[4] = [1, 0]
    dict[5] = [1, 1]
    dict[6] = [1, 2]
    dict[7] = [2, 0]
    dict[8] = [2, 1]
    dict[9] = [2, 2]
    dict[0] = [3, 1]
    
    for number in numbers:
        number_y = dict[number][0]
        number_x = dict[number][1]
        if number == 1 or number == 4 or number == 7:
            result += "L"
            L = [number_y, number_x]
        elif number == 3 or number == 6 or number == 9:
            result += "R"
            R = [number_y, number_x]
        else:
            L_distance = abs(L[0] - number_y) + abs(L[1] - number_x)
            R_distance = abs(R[0] - number_y) + abs(R[1] - number_x)

            if L_distance < R_distance:
                result += "L"
                L = [number_y, number_x]
            elif L_distance > R_distance:
                result += "R"
                R = [number_y, number_x]
            else:
                if hand == "right":
                    result += "R"
                    R = [number_y, number_x]
                else:
                    result += "L"
                    L = [number_y, number_x]
    return result