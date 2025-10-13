s = input()
result = ''
stack = []
in_tag = False

for ch in s:
    if ch == '<':
        # 단어 스택 비워서 출력 후 태그 시작
        while stack:
            result += stack.pop()
        in_tag = True
        result += ch
    elif ch == '>':
        in_tag = False
        result += ch
    elif in_tag:
        # 태그 내부는 그대로 출력
        result += ch
    elif ch == ' ':
        # 공백 만나면 단어 뒤집고 공백 추가
        while stack:
            result += stack.pop()
        result += ' '
    else:
        # 일반 단어는 스택에 쌓기
        stack.append(ch)

# 남은 단어 처리
while stack:
    result += stack.pop()

print(result)
