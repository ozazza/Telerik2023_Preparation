
is_break = False
sum = 0

while not is_break:
    number = input()

    first = int(number[0])
    mid = int(number[1])
    last = int(number[2])

    if (first + last) == mid:
        sum += int(number)
    else:
        is_break = True

print(sum)