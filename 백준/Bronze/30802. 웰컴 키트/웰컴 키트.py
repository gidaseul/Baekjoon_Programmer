N = int(input())
a = list(map(int,input().split()))
T,P = map(int,input().split())

min_tshirts = 0

for size in a:
    if size % T != 0:
        min_tshirts += size // T +1
    else:
        min_tshirts += size // T

max_pens = N // P
pen = N % P

print(min_tshirts)
print(max_pens, pen)
