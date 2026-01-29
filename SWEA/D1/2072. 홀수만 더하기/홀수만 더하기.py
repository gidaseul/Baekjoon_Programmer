T = int(input())
for test_case in range(1, T + 1):
    odd_sum = 0
    numbers = list(map(int, input().split()))

    for num in numbers:
        if num % 2 != 0:
            odd_sum += num
            
    print(f"#{test_case} {odd_sum}")