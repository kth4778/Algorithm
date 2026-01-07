import heapq

def solution(jobs):
    size = len(jobs)                    #작업의 수
    current_time = 0                    #현재 시간
    time = [0 for _ in range(size)]     #각 작업의 반환시간 기록
    que = []                            #우선순위 큐
    
    for i in range(size):
        heapq.heappush(que, [jobs[i][1], jobs[i][0], i])
    for q in range(size):
        unavailable_jobs = []
        count = 0
        switch = False

        while True:
            if count == size - q:
                switch = True
                break
            
            l, s, i = heapq.heappop(que)

            if s > current_time:
                heapq.heappush(unavailable_jobs, [s, l, i])
                count += 1
            else:
                time[i] = current_time + l - s
                current_time += l
                break
        if switch == True:
            s, l, i = heapq.heappop(unavailable_jobs)
            current_time = s + l
            time[i] = l
        
        for s, l, i in unavailable_jobs:
            heapq.heappush(que, [l, s, i])
    return sum(time) // size