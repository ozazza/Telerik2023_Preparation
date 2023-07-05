n = input()

even = 0
odd = 0

for i in n:
    if int(i) == 0 or int(i) % 2 == 0:
        even += int(i)
    else:
        odd += int(i)

if even > odd:
    print(f'{even} energy drinks')
elif even < odd:
    print(f'{odd} cups of coffee')
else:
    print(f'{odd} of both')
    