counter = 0
sum = 0
while counter < 1:
    n = input()

    first = int(n[0])
    mid = int(n[1])
    last = int(n[2])

    if (first + last) == mid:
        sum += int(n)
    else:
        counter = 1

print(sum)