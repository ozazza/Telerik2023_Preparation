n = int(input())

primes = []
line = []

# list with prime number to 1001
for i in range(1, 1001, 1):
    if i < 3:
        primes.append(i)
    elif i > 2:
        for p in range(2, int( i / 2) + 1, 1):
            if (i % p) == 0:
                break
        else:
            primes.append(i)

for k in range(1, n + 1, 1):
    
    if k in primes:
        for s in range(1, k + 1, 1):
            
            if s in primes:
                line.append('1')
            else:
                line.append('0')
        
        print(''.join(line))
        line.clear()                


