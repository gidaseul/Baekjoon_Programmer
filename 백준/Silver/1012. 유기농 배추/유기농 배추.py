from collections import deque
import sys

# 재귀 깊이 제한 해제
sys.setrecursionlimit(100000)

def dfs(x, y):
    # 1. 경계 조건 확인: 밭의 범위를 벗어났을 경우
    if x < 0 or x >= m or y < 0 or y >= n:
        return

    # 2. 방문 여부 & 배추 유무 확인: 배추가 없거나 이미 방문했다면 탐색 중단
    if graph[y][x] == 0:
        return

    # 3. 방문 처리: 현재 위치의 배추를 0으로 바꿔 다시 세지 않도록 함
    graph[y][x] = 0

    # 4. 상하좌우 탐색 (재귀 호출)
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    result = 0

    # 2차원 배열을 순회하며 배추 덩어리 찾기
    for y in range(n):  # y 좌표 (세로)
        for x in range(m): # x 좌표 (가로)
            if graph[y][x] == 1:
                dfs(x, y)
                result += 1

    print(result)

    