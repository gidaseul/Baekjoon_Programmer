import sys

input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    a,b = map(int,input().split())
    graph.append([a,b])

sorted_data = sorted(graph, key=lambda point: (point[0], point[1]))

for i in sorted_data:
    print(i[0],i[1])