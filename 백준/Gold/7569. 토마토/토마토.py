from collections import deque

# M: 가로, N: 세로, H: 높이
M, N, H = map(int, input().split())
# 3차원 리스트로 입력 받음
tomatoes = []
for _ in range(H):
    floor = [list(map(int, input().split())) for _ in range(N)]
    tomatoes.append(floor)

# 6방향: 상, 하, 좌, 우, 앞, 뒤
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

# 큐에 처음 익은 토마토들의 위치를 추가
queue = deque()
for z in range(H):
    for x in range(N):
        for y in range(M):
            if tomatoes[z][x][y] == 1:
                queue.append((z, x, y))

def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            # 유효한 범위에 있고 익지 않은 토마토가 있을 때
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and tomatoes[nz][nx][ny] == 0:
                tomatoes[nz][nx][ny] = tomatoes[z][x][y] + 1
                queue.append((nz, nx, ny))

# BFS 실행
bfs()

# 결과 확인
res = 0
for z in range(H):
    for x in range(N):
        for y in range(M):
            if tomatoes[z][x][y] == 0:  # 익지 않은 토마토가 남아 있으면 -1 출력
                print(-1)
                exit(0)
            res = max(res, tomatoes[z][x][y])

# 최소 날짜 계산 (초기값이 1이므로 1을 빼줌)
print(res - 1)
