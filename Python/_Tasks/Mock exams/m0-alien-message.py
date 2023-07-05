
en = input()
sp = input()

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

en_numbers = []
sp_numbers = []
max_len = [len(en), len(sp)]
longest_len = max(max_len)
result = []

for i in range(longest_len):
    en_char_nr= 0 
    sp_char_nr = 0
    sub = 0
    sub_has_value = False
    
    if len(en) > i:
        if en[i] == ' ' or en[i] == '-':
            sub = en[i]
            sub_has_value = True
            result.append(sub)
            continue
        else:
            en_char_nr = abc.index(en[i])
    
    if len(sp)> i:
        if sp[i] == ' ' or sp[i] == '-':
            sub = sp[i]
            sub_has_value = True
            result.append(sub)
            continue
        else:
            sp_char_nr = abc.index(sp[i])
            
        # en_numbers.append(str(en_char_nr))
        # sp_numbers.append(str(sp_char_nr))
        
        if not sub_has_value:
            sub = abc[abs(en_char_nr - sp_char_nr)]
        
    result.append(sub)

print(''.join(result))