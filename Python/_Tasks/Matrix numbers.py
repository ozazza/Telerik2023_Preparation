n = int(input())

for col in range(1, n + 1):

    for row in range(col, n + col):
        print(row, end = '')
    
    print()