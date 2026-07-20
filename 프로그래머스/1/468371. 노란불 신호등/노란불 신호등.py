def solution(signals):
    s = []
    
    for signal in signals:
        s.append([])
        
        for _ in range(signal[0]):
            s[-1].append('G')
        for _ in range(signal[1]):
            s[-1].append('Y')
        for _ in range(signal[2]):
            s[-1].append('R')
    
    count = 0
    
    while True:
        if count == 10000000:
            return -1
        
        r = []
        count += 1
        for i in s:
            p = count % len(i)         
            r.append(i[p - 1])
        
        r = len([i for i in r if i == "Y"])
        
        if r == len(s):
            return count
        
        