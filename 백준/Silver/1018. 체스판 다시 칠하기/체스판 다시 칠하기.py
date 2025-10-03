import sys

def solve():
    # 입력값 받기
    N, M = map(int, sys.stdin.readline().split())
    board = []
    for _ in range(N):
        board.append(sys.stdin.readline().strip())

    min_changes = float('inf')  # 최소 변경 횟수 초기화 (무한대)

    # 모든 8x8 부분 보드 탐색
    for i in range(N - 7):
        for j in range(M - 7):
            # 현재 8x8 보드의 시작점은 (i, j)
            count_w_start = 0  # 흰색으로 시작하는 경우의 칠하기 횟수
            count_b_start = 0  # 검은색으로 시작하는 경우의 칠하기 횟수

            # 8x8 보드 내부를 탐색
            for x in range(i, i + 8):
                for y in range(j, j + 8):
                    # (x, y) 좌표의 합이 짝수일 때
                    if (x + y) % 2 == 0:
                        # 'W'로 시작하는 경우, 이 칸은 'W'여야 함
                        if board[x][y] != 'W':
                            count_w_start += 1
                        # 'B'로 시작하는 경우, 이 칸은 'B'여야 함
                        if board[x][y] != 'B':
                            count_b_start += 1
                    # (x, y) 좌표의 합이 홀수일 때
                    else:
                        # 'W'로 시작하는 경우, 이 칸은 'B'여야 함
                        if board[x][y] != 'B':
                            count_w_start += 1
                        # 'B'로 시작하는 경우, 이 칸은 'W'여야 함
                        if board[x][y] != 'W':
                            count_b_start += 1

            # 두 경우 중 더 작은 값을 찾아 최소값 갱신
            min_changes = min(min_changes, count_w_start, count_b_start)

    print(min_changes)

# 함수 호출
solve()