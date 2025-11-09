import math

s = input().strip()
t = input().strip()


len_s = len(s) 
len_t = len(t)  

l = (len_s * len_t) // math.gcd(len_s,len_t) # 최소공배수 구하는 방법 = (두 자연수의 곱 )나누기 (최대 공약수)

s_rep = s * (l // len_s)
t_rep = t * (l // len_t)

print(1 if s_rep == t_rep else 0)