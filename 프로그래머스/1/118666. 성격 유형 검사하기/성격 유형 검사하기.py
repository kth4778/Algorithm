def solution(survey, choices):
    d = {}
    d["R"] = 0
    d["T"] = 0
    d["C"] = 0
    d["F"] = 0
    d["J"] = 0
    d["M"] = 0
    d["A"] = 0
    d["N"] = 0
    # RT, CF, JM, AN
    
    for i in range(len(survey)):
        if choices[i] < 4:
            d[survey[i][0]] += abs(4 - choices[i])
        elif choices[i] > 4:
            d[survey[i][1]] += (choices[i] - 4)
    
    result = ""
    
    if d["R"] > d["T"]:
        result += "R"
    elif d["R"] < d["T"]:
        result += "T"
    else:
        result += "R"
        
    if d["C"] > d["F"]:
        result += "C"
    elif d["C"] < d["F"]:
        result += "F"
    else:
        result += "C"
        
    if d["J"] > d["M"]:
        result += "J"
    elif d["J"] < d["M"]:
        result += "M"
    else:
        result += "J"
        
    if d["A"] > d["N"]:
        result += "A"
    elif d["A"] < d["N"]:
        result += "N"
    else:
        result += "A"
        
    return result