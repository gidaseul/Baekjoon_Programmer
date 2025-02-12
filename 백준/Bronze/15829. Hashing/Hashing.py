n = int(input())
a = list(input())
result = 0
for i in range(n):
    result += ((ord(a[i])-96)*31**i)%1234567891
print(result%1234567891)