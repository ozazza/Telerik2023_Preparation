n = int(input())

sum = 0
for i in range(n):
    new = float(input())
    sum += new

ave = round(sum / n, 2)
print(f'{ave:.2f}')