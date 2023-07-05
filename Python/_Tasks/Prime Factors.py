n = int(input())

for i in range(2, n - 1):
    if n == 1:
        break

    i_is_prime = False

    # check if i is prime
    for check in range(2, i):

        if i % check == 0:
            i_is_prime = False
            break
    else:
        i_is_prime = True                       
        
    if i_is_prime:

        if n % i == 0:
            while n % i == 0:
                n = int(n / i)
                print(i)