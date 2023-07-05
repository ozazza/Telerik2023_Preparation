n = int(input())

numbers = []
merged = []
squashed = []

for i in range(n):
    numbers.append(input())

for ab in range(0, len(numbers)-1, 1):
    for cd in range(ab+1, len(numbers), 1):
        bc_sum = ''
        a = numbers[ab][0]
        b = numbers[ab][1]
        c = numbers[cd][0]
        d = numbers[cd][1]
        
        merged.append(b + c)

        bc_sum = str(int(b) + int(c))
        if len(bc_sum) > 1:
            bc_sum = bc_sum[1]
        

        squashed.append(a + str(bc_sum) + d)
        break

print(' '.join(merged))
print(' '.join(squashed))