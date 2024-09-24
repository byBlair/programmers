N = int(input())
link = int(input())
cnt = 0

def dfs(virus):
    global cnt  # 전역 변수 cnt를 사용한다고 명시
    visited[virus] = 1
    for i in network[virus]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1  # cnt 값을 증가

network = [[] for _ in range(N+1)]

for i in range(link):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

visited = [0] * (N + 1)
dfs(1)  # 1번 컴퓨터에서 시작
print(cnt)