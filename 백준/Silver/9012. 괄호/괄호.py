import sys

input = sys.stdin.readline
result = []
n = int(input())
for i in range(n):
    stack = []
    line = input().strip() 
    is_valid = True

    for j in line:
        if j == "(":
            stack.append("(")
        elif j == ")":
            if not stack:
                is_valid = False
                break
            else:
                stack.pop()

    if not stack and is_valid:
        result.append("YES")
    else:
        result.append("NO")

for i in range(n):
    print(result[i])

