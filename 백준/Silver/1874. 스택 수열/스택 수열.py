import sys

n = int(input())
stack = []
current = 1
result = []
is_valid = True

for _ in range(n):
    target_number = int(input())

    while current <= target_number:
        stack.append(current)
        result.append("+")
        current += 1
    
    if stack[-1] == target_number:
        stack.pop()
        result.append("-")
    
    else:
        is_valid = False

if not is_valid:
    print("NO")
else:
    for i in result:
        print(i)


