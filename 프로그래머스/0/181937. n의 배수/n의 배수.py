def solution(num, n):
  
# num%n은 int 값이지만, 이를 not() 함수 안에 넣으면 int가 bool로 해석되어서 num%n이 0이면 False로, 0이 아니면 True로 해석되면서 1을 반환한다.
    return int(not(num % n))
