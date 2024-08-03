from collections import deque

def solution(n, computers):
    def bfs(node):
        queue = deque([node])
        while queue:
            current = queue.popleft()
            if not visited[current]:
                visited[current] = True
                for neighbor in range(n):
                    if computers[current][neighbor] == 1 and not visited[neighbor]:
                        queue.append(neighbor)

    visited = [False] * n
    network_count = 0

    for i in range(n):
        if not visited[i]:
            bfs(i)  # 새로운 네트워크를 발견하고 BFS로 그 네트워크의 모든 컴퓨터를 방문
            network_count += 1

    return network_count
