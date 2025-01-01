bowl = input()

answer = 0
set_bowl = None

for b in bowl:
    if set_bowl == None:
        answer += 10
    
    else:
        if set_bowl == b:
            answer += 5
        else:
            answer += 10
    
    set_bowl = b

print(answer)