command = input()
x = 0
y = 0

for i in command:
    if i == 'D':
        y -= 1
    elif i == 'U':
        y += 1
    elif i == 'R':
        x += 1
    else:
        x -= 1
print(f'({x}, {y})')