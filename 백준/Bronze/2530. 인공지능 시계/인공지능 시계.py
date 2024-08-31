import datetime

time = input()
d = int(input())
now = datetime.datetime.strptime(time, '%H %M %S')
next_time = now + datetime.timedelta(seconds=d)
print(next_time.hour, next_time.minute, next_time.second)