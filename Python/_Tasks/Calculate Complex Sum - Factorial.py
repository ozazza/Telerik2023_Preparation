# S = 1 + 1!/x + 2!/x2 + … + N!/xN
# Each element is calculated as 
# follows: (previous_element) * i / xi

n = int(input())
x = float(input())

s = 1
fac = 1

for i in range(1, n + 1):
    
    """ if i == 0: fac = 1
    elif i == 1: fac = 1
    elif i == 2: fac = 2
    elif i == 3: fac = 6
    elif i == 4: fac = 24
    elif i == 5: fac = 120
    elif i == 6: fac = 720
    elif i == 7: fac = 5040
    elif i == 8: fac = 40320
    elif i == 9: fac = 362880
    elif i == 10: fac = 3628800 """

    fac *= i

    s += fac / x ** i

print(f'{s:.5f}')