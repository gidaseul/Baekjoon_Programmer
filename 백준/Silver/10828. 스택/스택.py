import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size_count = 0  # size() O(1)로 만들기

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self.size_count += 1

    def pop(self):
        if self.top is None:
            return -1
        node = self.top
        self.top = self.top.next
        self.size_count -= 1
        return node.data    

    def size(self):
        return self.size_count  # O(1) 연산

    def is_empty(self):
        return 1 if self.top is None else 0

    def peek(self):  # top() 메서드 이름 충돌 해결
        if self.top is None:
            return -1
        return self.top.data

if __name__ == '__main__':
    s = Stack()
    commands = sys.stdin.read().splitlines()  # 입력 최적화

    for command in commands[1:]:  # 첫 줄 (n) 무시하고 처리
        parts = command.split()
        if parts[0] == 'push':
            s.push(int(parts[1]))
        elif parts[0] == 'pop':
            print(s.pop())
        elif parts[0] == 'size':
            print(s.size())
        elif parts[0] == 'empty':
            print(s.is_empty())
        elif parts[0] == 'top':
            print(s.peek())  # top() → peek()으로 변경
