
width = {'1': 2, '0': 4}
default_width = 3

while True:
    number = input().strip()
    if number == '0':
        break

    total_width = sum(width.get(d, default_width) for d in number)
    total_width += len(number) + 1
    print(total_width)

