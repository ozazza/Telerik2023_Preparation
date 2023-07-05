number = int(input())

result = []
n_is_prime = False
primes = []

# add primes from 1 to 1000 in list
for g in range(1, 1001, 1):
  
    # n=1 is prime by condition of the task
    if g == 1 or g == 2:
        
        primes.append(g)
    
    elif g > 1:
        for i in range(2, int(g ** 0.5) + 2, 1):
            
            if (g % i) == 0:
                n_is_prime = False
                break
        else:
            primes.append(g)
                
  

for n in range(1, number + 1, 1):  

    # check if n is prime
    if n in primes:
        
        for s in range(1, n + 1, 1):
        
            # if n is prime
            if s in primes:
                result.append(str(1))
            else:
                result.append(str(0))
            
        print(''.join(result))
        result.clear()