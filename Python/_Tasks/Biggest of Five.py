a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

ab = a if a > b else b
cd = c if c > d else d
max = ab if ab > cd else cd
emax = max if max > e else e

print(emax)