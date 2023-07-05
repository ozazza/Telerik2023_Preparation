n = int(input())

logs_left = n
count_rows = 0
count_logs = 0

for row in range(1, n + 1):

    for col in range(1, row + 1):
        
        logs_left -= 1        
        count_logs += 1
        
    count_rows += 1
    
    if count_logs >= n:
        break

        
if count_logs == n and logs_left == 0:
    print(count_rows)

else: print(count_rows-1)

