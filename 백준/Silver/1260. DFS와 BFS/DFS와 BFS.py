import sys
def dfs(idx):
    global visited
    visited[idx] = True
    print(idx,end=' ')
    for next in range(1, N+1):
        if not visited[next] and graph[idx][next]:
            dfs(next)

def bfs():
    global q, visited
    while q:
        cur = q.pop(0)
        print(cur, end=' ')
        for next in range(1,N+1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)
        

N,M,V = map(int,sys.stdin.readline().split())

graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

# 그래프 업데이트
for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a][b] = True
    graph[b][a] = True
    
 #DFS
dfs(V)
print() # 줄바꿈

visited = [False] * (N+1)
q = [V]
visited[V] = True
bfs()
