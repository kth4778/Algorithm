def solution(phone_book):
    phone_numbers = {}
    
    for phone_number in phone_book:
        phone_numbers[phone_number] = 1
    
    for phone_number in phone_book:
        temp = ""
        for p in phone_number[:-1]:
            temp += p
            if temp in phone_numbers:
                return False
    return True