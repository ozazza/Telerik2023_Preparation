# 3 years. 5% per year

deposit = float(input())
y1 = float(deposit * 0.05 + deposit)
y2 = float(y1 * 0.05 + y1)
y3 = float(y2 * 0.05 + y2)

print('%.2f' % y1)
print('%.2f' % y2)
print('%.2f' % y3)