line1 = input().split(',')
line2 = input().split(',')

result = []
for l in line2:
    result.append(l)

x = 0
for m in range(0, len(line1)):

    result.insert(x, line1[m])
    x += 2

print(','.join(result))