def solution(babbling):
    answer = 0
    
    for b in babbling:
        index = 0
        current_b = ""
        
        while index < len(b):
            if b[index] == 'a':
                if len(b[index:]) >= 3 and b[index:index+3] == "aya" and current_b != "aya":
                    index += 3
                    current_b = "aya"
                else:
                    break
            elif b[index] == 'y':
                if len(b[index:]) >= 2 and b[index:index+2] == "ye"  and current_b != "ye":
                    index += 2
                    current_b = "ye"
                else:
                    break
            elif b[index] == 'w':
                if len(b[index:]) >= 3 and b[index:index+3] == "woo" and current_b != "woo":
                    index += 3
                    current_b = "woo"
                else:
                    break
            elif b[index] == 'm':
                if len(b[index:]) >= 2 and b[index:index+2] == "ma" and current_b != "ma":
                    index += 2
                    current_b = "ma"
                else:
                    break
            else:
                break
        if index >= len(b):
            answer += 1
    return answer