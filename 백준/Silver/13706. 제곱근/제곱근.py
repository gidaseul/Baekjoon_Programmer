# math.sqrt 같은 경우를 사용하면 안되는 이유


# 소수를 처리하는 방법인 부동 소수점을 이해하면 알 수 있는데 
# 컴퓨터의 소수를 표현하는 방법은 수학에서 사용하는 표현 방식과 달라서 어느 정도의 오차가 존재함.

# 따라서 보통 경우 제곱근을 구하는 경우에서 **0.5 , math.sqrt를 사용하게 되면 다시 정수로 변환하는 과정에서 오차가 발생하게 된다.

# <중요!>
# 문제에서 주어지는 입력(N)은 항상 제곱근의 값이 정수가 되는 값으로 주어진다고 함.

# => 1~N까지 사이에는 N의 제곱근이 존재한다는 의미이기 때문에 확인할 필요 존재함. 이걸 이진 탐색으로


import sys

n = int(sys.stdin.readline().strip())

left, right = 1, n   # 정답은 1 이상 n 이하 어딘가에 있음
answer = 1

while left <= right:
    mid = (left + right) // 2
    sq = mid * mid     # mid^2

    if sq == n:
        answer = mid
        break
    elif sq < n:
        # mid는 제곱해도 n보다 작으니까 일단 후보로 저장
        answer = mid
        left = mid + 1
    else:
        # mid^2가 너무 크다 → mid를 줄여야 함
        right = mid - 1

print(answer)
