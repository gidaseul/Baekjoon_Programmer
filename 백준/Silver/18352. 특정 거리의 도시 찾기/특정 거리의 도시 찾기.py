import sys
from collections import deque

# sys.stdin.readline을 짧은 변수명으로 설정
input = sys.stdin.readline

# N, M, K, X를 공백으로 구분해 입력받아 정수형으로 변환
N, M, K, X = map(int, input().split())

# 그래프 정보를 저장할 인접 리스트 초기화 (1번부터 N번 도시까지 사용)
graph = [[] for _ in range(N + 1)]

# distance 배열 초기화 및 BFS 함수 호출
distance = [-1] * (N + 1)
distance[X] = 0 # BFS 함수 밖에서 초기화해도 됨

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)


def bfs(graph, start, distance):
    queue = deque([start])

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if distance[i] == -1:
                distance[i] = distance[v] +1
                queue.append(i)

bfs(graph, X, distance)

found = False

for i in range(1,N+1):
    if distance[i] == K:
        print(i)
        found = True

if not found:
    print(-1)
