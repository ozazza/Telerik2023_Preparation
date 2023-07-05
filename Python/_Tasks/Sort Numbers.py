input_list = input().split(', ')

numbers = []
for i in input_list:
    numbers.append(int(i))

numbers.sort(reverse = True)

sorted = []
for n in numbers:
    sorted.append(str(n))

print(', '.join(sorted))