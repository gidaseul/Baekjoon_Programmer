import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 모든 익은 토마토를 큐에 초기화
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j, 0)) # 좌표와 함께 시작 날짜 0을 저장

final_day = 0
while queue:
    x, y, day = queue.popleft()
    final_day = day # 마지막으로 꺼낸 토마토의 날짜를 저장

    # 상하좌우 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 범위와 익지 않은 토마토 확인
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            graph[nx][ny] = 1 # 방문 처리 (토마토 익음)
            queue.append((nx, ny, day + 1))

# 모든 토마토가 익었는지 확인
is_all_ripe = True
for row in graph:
    if 0 in row:
        is_all_ripe = False
        break

if is_all_ripe:
    print(final_day)
else:
    print(-1)