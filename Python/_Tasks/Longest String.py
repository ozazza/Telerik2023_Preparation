food = ''
longest = ''
length = 0
max_len = 0
counter = 0

while food != 'END' or counter == 50:
    counter += 1 
    food = input()

    if food != 'END':
        length = len(food)

        if length >= max_len:
            longest = food
            max_len = length
    else:
        break

print(longest)