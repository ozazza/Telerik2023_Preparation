a = int(input())
b = int(input())
c = int(input())

if a > b:
    if b > c:
        print(a,b,c)
    else:
        if c > a:
            print(c,a,b)
        else:
            print(a,c,b)
else:
    if a > c:
        print(b,a,c)
    else:
        if b > c:
            print(b,c,a)
        else:
            print(c,b,a)