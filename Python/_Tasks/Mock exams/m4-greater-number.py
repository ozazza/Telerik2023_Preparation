sub = input().split(',')
full = input().split(',')

result = []

for s in sub:
    num_is_found = False
    
    # for i2 in full:
    if s in full:
        
        index_s_in_full = full.index(s)
        next_i = index_s_in_full + 1
        
        if len(full) > next_i:
            sliced_full = full[next_i:]
            
            for m in sliced_full:
                if int(m) > int(s):
                    num_is_found = True
                    result.append(m)
                    break
        
        if not num_is_found:
            result.append('-1')
                
print(','.join(result))