import sys
input = sys.stdin.readline

array = input().strip()  # int 변환 안 해도 됨 (자리수 분리 목적)

digits_list = list(array)
digits_list.sort(reverse=True)   

result = "".join(digits_list)
print(result)
