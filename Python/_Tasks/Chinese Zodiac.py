n = int(input())

sign = ''

if n %12 == 8: sign = 'Dragon'
elif n % 12 == 9: sign = 'Snake'
elif n % 12 == 10: sign = 'Horse'
elif n % 12 == 11: sign = 'Sheep'
elif n % 12 == 0: sign = 'Monkey'
elif n % 12 == 1: sign = 'Rooster'
elif n % 12 == 2: sign = 'Dog'
elif n % 12 == 3: sign = 'Pig'
elif n % 12 == 4: sign = 'Rat'
elif n % 12 == 5: sign = 'Ox'
elif n % 12 == 6: sign = 'Tiger'
elif n % 12 == 7: sign = 'Hare'

print(sign)

number = 50
if number > 10:
    print("Larger than 10")
if number > 20:
    print("Larger than 20")
if number > 50:
    print("Larger than 50")
else:
    print("Not larger than 50")