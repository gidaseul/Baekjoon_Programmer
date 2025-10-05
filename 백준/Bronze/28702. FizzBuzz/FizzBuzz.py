import sys
input = sys.stdin.readline

def fizzbuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# 이렇게 놓는 이유는 i가 1이라면 3만큼 더하면 되고, 2라면 2, 3이라면 1만큼 더하면 된다.
# 그렇기 때문에 반대로 놓아야 다음을 예측이 가능하다.
for i in range(3, 0, -1):
    n = input().strip()
    if n.isdigit():
        fizzbuzz(int(n)+i)
        break
    