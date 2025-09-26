from collections import deque
import sys


c_node = int(input())
c_edge = int(input())

# 인접 리스트, 1번부터 N번까지 사용하기 위해 N+1 크기로 초기화
graph = [[] for _ in range(c_node + 1)]

# 방문 여부를 체크하는 배열을 N+1 크기로 초기화
visited = [False] * (c_node+1)

for _ in range(c_edge):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start_node):
    count = 0
    queue = deque([start_node])

    visited[start_node] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                count +=1

    return count

print(bfs(1))