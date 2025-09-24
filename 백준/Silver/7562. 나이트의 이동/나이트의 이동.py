# 3     <-- 테스트 케이스의 개수 (t = 3)
# 8     <-- 첫 번째 체스판 크기 (l = 8)
# 0 0   <-- 첫 번째 시작 위치
# 7 0   <-- 첫 번째 목표 위치
# 100   <-- 두 번째 체스판 크기 (l = 100)
# 0 0   <-- 두 번째 시작 위치
# 30 50 <-- 두 번째 목표 위치
# 10    <-- 세 번째 체스판 크기 (l = 10)
# 1 1   <-- 세 번째 시작 위치
# 1 1   <-- 세 번째 목표 위치

import sys 
from collections import deque

input = sys.stdin.readline

def knight_move_bfs(l,start, target):
    if start == target:
        return 0
    
    q = deque()
    q.append((start[0], start[1], 0))  # (x, y, 이동 횟수)

    # 맵 크기에 맞게 visited 맵 초기화
    visited = [[False] * l for _ in range(l)] # 방문여부 파악하기 위해 False로 우선 처리
    visited[start[0]][start[1]] = True #(x,y)는 이미 방문했으니까 
    
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]

    while q:
        x,y,count = q.popleft()

        # 8가지 방향으로 이동 확인
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < l and 0 <= ny < l:
                # 여기에 들어온 경우라면 일단 맵의 범위 안에 들어온 상태이기 때문에 방문 여부 파악
                if not visited[nx][ny]:
                    # 목표 지점에 도착
                    if nx == target[0] and ny == target[1]:
                        return count + 1 
                    
                    visited[nx][ny] = True
                    q.append((nx, ny, count + 1))
    return -1 # 목표 지점에 도달할 수 없는 경우 (문제에서는 이런 경우는 없음)

test_cases = int(input())
for _ in range(test_cases):
    l = int(input())
    start_x, start_y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    
    start_pos = (start_x, start_y)
    target_pos = (target_x, target_y)
    
    print(knight_move_bfs(l, start_pos, target_pos))










