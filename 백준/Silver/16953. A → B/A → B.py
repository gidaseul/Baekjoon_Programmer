
# A를 B로 바꿀 때 필요한 연산의 최솟값 -> 달리 말하면 B -> A로 생각해보자
# 미로를 생각하자! 정답에서 돌아갈 경우에 도착한 값이 A랑 맞는지 파악하는 것이 연산량이 줄어들게 됨.


A,B = map(int,input().split())
count = 1 

while B > A:

  if B % 10 == 1:
      B //= 10 # 만약에 1001이라면 기존 수에서 10으로 몇번 나눠야 하는지 보고 
      count +=1
  
  elif B % 2 == 0: # 짝수일 경우
    B //=2
    count+=1

  else:
    break
if B == A:
  print(count)
else:
  print(-1) 
