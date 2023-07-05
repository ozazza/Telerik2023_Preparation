n = int(input())

numbers = []
counter = 0
duplicates = []
times = []

for s in range(n):
    numbers.append(int(input()))
    
for i in numbers:
    
    if i in duplicates: continue
    else:
        for d in numbers:
            
            if i == d:
                counter += 1
                if i in duplicates:
                    index = duplicates.index(i)
                    times[index] += counter
                else:
                    duplicates.append(i)
                    index = duplicates.index(i)
                    
                    if len(times) <= index:
                        for k in range(len(times), index + 1, 1):
                            
                            if k == index:
                                times.append(counter)
                            else:
                                times.append(0)
                    else:
                        times[index] += counter
            counter = 0

index_max_time = times.index(max(times)) 
print(duplicates[index_max_time])

