T = int(input())

for _ in range(T):
    a,b = map(int,input().split())
    word = input()
    answer = ''.join([chr(ord('A') + ((ord(s)-ord('A'))*a + b)%26) for s in word])
    print(answer)
