from collections import deque
import sys

def push(x):
    d.append(x)
    return d

def pop():
    if len(d) == 0:
        return -1
    else:
        return d.popleft()
    
def size():
    return len(d)

def is_empty():
    if len(d) == 0:
        return 1
    else:
        return 0
    
def front():
    if len(d) == 0:
        return -1
    else:
        return d[0]
def back():
    if len(d) == 0:
        return -1
    else:
        return d[-1]

if __name__ == '__main__':
    d = deque()
    n = int(sys.stdin.readline())
    commands = sys.stdin.read().splitlines()
    
    for command in commands:
        parts = command.split()  # 공백 기준으로 나누기
        cmd = parts[0]  # 첫 번째 단어가 명령어

        if cmd == 'push':
            push(int(parts[1]))  # 두 번째 값이 숫자이므로 변환해서 전달
        elif cmd == 'pop':
            print(pop())
        elif cmd == 'size':
            print(size())
        elif cmd == 'empty':
            print(is_empty())
        elif cmd == 'front':
            print(front())
        elif cmd == 'back':
            print(back())

