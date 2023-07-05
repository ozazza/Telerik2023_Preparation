n = int(input())

old = -201
for i in range(n):

    new = int(input())    
    bigger = max(new, old)
    old = bigger

print(old)