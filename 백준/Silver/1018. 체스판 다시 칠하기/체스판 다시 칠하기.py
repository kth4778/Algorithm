def counter(a,b):                                       #체스판 색칠 횟수 구하는 함수
    return sum([1 for q,w in zip(a,b) if q!=w])
N,M=map(int,input().split())
result=[]
for i in range(N):      #입력된 체스판 넣기                  
    result.append([i for i in input()])


main_chess1=[['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B']]
main_chess2=[['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W']]

count_list1=[]

for i in range(N-7):
    for w in range(M-7):
        count_list1.append([p[w:w+8] for p in result[i:i+8]])

result_last=[0 for i in range((N-7)*(M-7))]
result_last2=[0 for i in range((N-7)*(M-7))]

for index,i in enumerate(count_list1):
    for ydex,w in enumerate(i):
        result_last[index]+=counter(main_chess1[ydex%2],w)
        result_last2[index]+=counter(main_chess2[ydex%2],w)
print(min(result_last+result_last2))