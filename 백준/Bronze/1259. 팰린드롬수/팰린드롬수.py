while True:
    N = input().strip()  # 문자열 입력 받기
    if N == "0":  # 입력이 '0'이면 종료
        break
    
    if N == N[::-1]:  # 회문 여부 확인
        print("yes")
    else:
        print("no")
