import sys
input = sys.stdin.readline

#0번째 인덱스부터 시작해 n-1번째 인덱스까지 각 원소의 값들을 넣고, 해당 값을 지금까지 구해온 sub_sum에 더하는 경우와 더하지 않는 경우를 각 가지로 나누어 재귀함수를 호출한다.
# 각 재귀함수에서 sub_sum이 구하고자 하는 s와 같다면 전역변수 cnt에 1을 더해주면 갯수를 세준다.
n,s = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
def subset(idx,sub_sum):
    global cnt

    if idx >= n:
        return
    sub_sum += arr[idx]
    if sub_sum == s:
        cnt += 1

    #현재 arr[idx]를 선택한 경우의 가지
    subset(idx+1,sub_sum)
    #현재 arr[idx]를 선택하지 않은 경우의 가지
    subset(idx+1,sub_sum - arr[idx])

subset(0,0)
print(cnt)

