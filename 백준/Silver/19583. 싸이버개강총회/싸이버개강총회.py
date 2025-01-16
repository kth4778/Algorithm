import sys
input = sys.stdin.readline

def change_time(t):
    return int(t[:2]) * 60 + int(t[3:])

S,E,Q = input().split()
students = {}
answer = 0

S = change_time(S)
E = change_time(E)
Q = change_time(Q)

while True:
    try:
        time, name = input().split()
        time = change_time(time)

        if time <= S:
            students[name] = True
        elif E <= time <= Q:
            if name in students:
                if students[name]:
                    answer += 1
                    students[name] = False
             
    except:
        break

print(answer)