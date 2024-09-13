from collections import deque

#1,2,3,4,5,6,7

n,k = map(int,input().split())
q = deque(range(1,n+1))
result = []
while q:
    for _ in range(k-1):
        q.append(q.popleft())
    result.append(q.popleft())
print('<{}>'.format(', '.join(map(str,result))))
