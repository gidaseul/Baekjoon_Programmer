import sys
from collections import deque

# sys.stdin.readline을 짧은 변수명으로 설정
input = sys.stdin.readline

n,m = map(int,input().split())

number = list(map(int,input().split()))


queue = deque()
for i in range(1,n+1):
    queue.append(i)

def count(num_list):
    total_count = 0  # 총 연산 횟수를 저장할 변수

    for target_num in num_list:
        target_index = queue.index(target_num)

        if target_index <= len(queue) //2 :
            for _ in range(target_index):
                queue.rotate(-1)
                total_count += 1
            queue.popleft()

        else:
            for _ in range(len(queue)-target_index):
                queue.rotate(1)
                total_count+=1
            queue.popleft()

    return total_count
            

print(count(number))

