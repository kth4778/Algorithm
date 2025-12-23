def solution(coin,cards):
    length = len(cards) + 1
    cards_info = {i:2 for i in cards}
    for i in range(len(cards)//3):
        cards_info[cards[i]] = 1

    left_cards = cards[:len(cards)//3]
    right_cards = cards[len(cards)//3:][::-1]
    round = 1

    while True:
        if right_cards:
            left_cards.append(right_cards.pop())
            left_cards.append(right_cards.pop())

        if len(left_cards) == 0:
            break

        switch = False

        for i in left_cards:
            if (length - i) in left_cards:
                if cards_info[i] == 1 and cards_info[(length-i)] == 1:
                    switch = True
                    left_cards.remove(i)
                    left_cards.remove(length-i)
                    break
                elif cards_info[i] == 1 and cards_info[(length-i)] == 2:
                    if coin >= 1:
                        switch = True
                        left_cards.remove(i)
                        left_cards.remove(length-i)
                        coin -= 1
                        break
                elif cards_info[i] == 2 and cards_info[(length-i)] == 2:
                    if coin >= 2:
                        switch = True
                        left_cards.remove(i)
                        left_cards.remove(length-i)
                        coin -= 2
                        break
        if switch:
            round += 1
            continue
        break
    if round > len(cards)//3:
        return len(cards)//3+1
    return round

        