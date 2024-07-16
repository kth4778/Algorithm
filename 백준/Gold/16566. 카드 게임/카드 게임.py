from bisect import bisect_right
import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())

m_lst = list(map(int,input().split()))
k_lst = list(map(int,input().split()))

m_idx = [0]*m
m_lst.sort()

for i in k_lst:
    idx = bisect_right(m_lst,i)
    if not m_idx[idx]:
        print(m_lst[idx])
        m_idx[idx] = 1
    else:
        while True:
            idx += 1
            if not m_idx[idx]:
                m_idx[idx] = 1
                print(m_lst[idx])
                break