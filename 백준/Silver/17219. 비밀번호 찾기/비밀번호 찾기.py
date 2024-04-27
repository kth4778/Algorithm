a,b=map(int,input().split())
sitepassword_list={}
find_sitepassword=[]
for _ in range(a):
    q,w=input().split()
    sitepassword_list[q]=w
for _ in range(b):
    e=input()
    find_sitepassword.append(sitepassword_list[e])
for i in find_sitepassword:
    print(i)