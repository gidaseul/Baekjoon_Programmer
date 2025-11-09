from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    importance = list(map(int, input().split()))
    queue = deque([(i, importance[i]) for i in range(N)])  # (문서 인덱스, 중요도)

    count = 0
    while queue:
        idx, priority = queue.popleft()

        # 뒤에 더 높은 우선순위가 있는가?
        if any(priority < q[1] for q in queue):
            queue.append((idx, priority))  # 뒤로 보냄
        else:
            count += 1  # 출력됨
            if idx == M:
                print(count)
                break
