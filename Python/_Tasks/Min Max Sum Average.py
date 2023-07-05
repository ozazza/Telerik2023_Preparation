n = int(input())

bigger = -10001
smaller = 10001
sum = 0

for i in range(n):
    num = float(input())

    bigger = max(bigger, num)
    smaller = min(smaller, num)
    sum += num

avg = sum / n

print(f'min={smaller:.2f}')
print(f'max={bigger:.2f}')
print(f'sum={sum:.2f}')
print(f'avg={avg:.2f}')