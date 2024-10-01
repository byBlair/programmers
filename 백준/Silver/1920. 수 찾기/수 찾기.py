from bisect import bisect_left

n = int(input())
arr = list(map(int,input().split()))
m = int(input())
qry = list(map(int,input().split()))
arr.sort()

for i in qry:
    idx = bisect_left(arr,i)
    if idx < n and arr[idx] == i:
        print(1)
    else:
        print(0)