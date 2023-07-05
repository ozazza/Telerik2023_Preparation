
title = input()
n = int(input())

lines = []
mod_title = []
remove_indexes = []
counter = 0

for t in range(n):
    lines.append(input())
    
for line in lines:

    mod_title = title
    remove_indexes = []
    next_index_k = -1
    counter = 0
    
    for char_line in line:        
        if char_line in mod_title:
            
            for char_mod in mod_title:
                
                mod_last_char = len(mod_title)-1
                title_last_char = len(title)-1
                
                if char_mod == char_line:                                       
                    
                    diff_to_mod_last_char = mod_last_char - mod_title.index(char_mod) + 1
                    index_char_at_title = len(title) - diff_to_mod_last_char
                    
                    if index_char_at_title >= next_index_k:
                    
                        remove_indexes.append(index_char_at_title)
                        
                        next_index_k = index_char_at_title + 1
                        mod_title = title[next_index_k:]
                        counter += 1
                        break
                    
                    next_index_k = index_char_at_title + 1
                    mod_title = title[next_index_k:]

        else: break
            
    if counter == len(line):
        mod_title = []        
      
        for i in range(len(title)):            
            if i not in remove_indexes:
                mod_title.append(title[i])                
        
        title = ''.join(mod_title)
        
        print(title)
    else:
        print('No such title found!')