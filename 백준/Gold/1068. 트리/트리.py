import sys
input = sys.stdin.readline

n = int(input().strip())
tree = list(map(int, input().split()))
delete = int(input())

def dfs(del_node):
    tree[del_node] = -10
    for i in range(n):
        if del_node == tree[i]:
            dfs(i)
dfs(delete)
cnt = 0

for i in range(n):
    if tree[i] != -10 and i not in tree:
        cnt+= 1
print(cnt)