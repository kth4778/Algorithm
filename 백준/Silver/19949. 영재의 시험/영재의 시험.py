answer = list(map(int,input().split()))
result = 0

def score(lst):
    p = 0
    for a,b in zip(lst, answer):
        if a == b:
            p += 1
    return p


for one in range(1,6):
    for two in range(1,6):
        for three in range(1,6):
            if one == two == three:
                continue
            for four in range(1,6):
                if two == three == four:
                    continue
                for five in range(1,6):
                    if three == four == five:
                        continue
                    for six in range(1,6):
                        if four == five == six:
                            continue
                        for seven in range(1,6):
                            if five == six == seven:
                                continue
                            for eight in range(1,6):
                                if six == seven == eight:
                                    continue
                                for nine in range(1,6):
                                    if seven == eight == nine:
                                        continue
                                    for ten in range(1,6): 
                                        if eight == nine == ten:
                                            continue
                                        if score([one, two, three, four, five, six, seven, eight, nine, ten]) >= 5:
                                            result += 1
print(result)