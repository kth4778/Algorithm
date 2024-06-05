import sys
input = sys.stdin.readline

L,K=map(int,input().split())
dic={}
for i in range(K):
    a=input().strip()
    dic[a]=i
c=sorted(dic.items(),key=lambda x:x[1])
for i in c[:L]:
    print(i[0])
