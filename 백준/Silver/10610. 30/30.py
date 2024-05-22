num = list(input())
num.sort(reverse=True)
res = ''

# num2를 가장큰 값으로 만들어줌
for x in num:
    res+=x

#30의 배수가 되는지 검산을 함
if '0' in num: #일단 0이없으면 30의 배수가 될수없음
    if int(res)%30==0:
        print(res)#num2가 30의 배수이면 출력
    else:
        print(-1) #30의 배수가 안되면 -1출력
else: #0이 없으면 -1출력
    print(-1)