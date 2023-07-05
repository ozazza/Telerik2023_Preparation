n = input()

sum = 0

while len(n) > 1:

    for c in n:
        if c.isdigit():
            sum += int(c)
    
    n = str(sum)
    sum = 0

print(n)