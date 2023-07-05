row = int(input())
even = 1
odd = 1

for i in range(1, row + 1):
    m = int(input())

    if i % 2 == 0:
        even *= m
    else:
        odd *= m

if even == odd:
    print(f'yes {odd}')
else:
    print(f'no {odd} {even}')