import sys
input = sys.stdin.readline
n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))
arr.sort()

 # 산술평균
a = sum(arr) / n 
a = int(round(a,0))

# 중앙값
k = int((n-1)/2)
b = arr[k]

# 최빈값 
dict = {}
for i in arr:
  if i not in dict:
    dict[i] = 1
  else:
    dict[i] += 1  

maxi = max(dict.values())
max_dict = []
for i in dict:
    if maxi == dict[i]:
        max_dict.append(i)

if len(max_dict) == 1:
    c = max_dict[0]
else:
    c = max_dict[1]
    
# 범위
d = max(arr) - min(arr)

# 출력
print(a)
print(b)
print(c) 
print(d)
