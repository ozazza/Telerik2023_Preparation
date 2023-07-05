n = int(input())
a = int(n / 1000)
b = int((n % 1000) / 100)

sum_ab = int(str(a) + str(b) + '00')
c = int((n - sum_ab)/10)

sum_abc = int(str(a) + str(b) + str(c) + '0')
d = n - sum_abc

print(a + b + c + d)