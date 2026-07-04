def solution(s):
    index = 9
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    while index > 0:
        index = 9
        
        for i in range(10):
            l = s.find(words[i])
            if l != -1:
                s = s[:l] + str(i) + s[l + len(words[i]):]
                index += l
            else:
                index += l
    return int(s)