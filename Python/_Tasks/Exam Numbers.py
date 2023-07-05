x = int(input())
y = int(input())
t = int(input())

for i in range(x, y + 1):

    a = i // 100
    b = i % 100 // 10
    c = i % 10

    if a + b + c == t:
        print (i)