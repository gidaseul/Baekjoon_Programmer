from collections import deque

n, k = map(int, input().split())
result = []
queue = deque([i for i in range(1, n + 1)])

while queue:
    # k-1번 왼쪽으로 회전
    queue.rotate(-(k - 1))
    
    # 맨 앞에 있는 사람을 제거하고 결과 리스트에 추가
    result.append(queue.popleft())

print("<" + ", ".join(map(str, result)) + ">")