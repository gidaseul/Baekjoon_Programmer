import sys
result = []
while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    T, F, S, P, C = map(int, line.split())
    result.append(T*6+F*3+S*2+P*1+C*2)
print(*result)