n,k=map(int,input().split())
studen_score=list(map(int,input().split()))
print(sorted(studen_score)[-k:][0])