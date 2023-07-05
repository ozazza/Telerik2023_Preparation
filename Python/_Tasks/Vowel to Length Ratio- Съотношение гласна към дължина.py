
# vowels a, e, i, o, u

n = int(input())

if n >= 1 and n <= 20:
    list_foods = []
    list_len = []
    list_vow = []
    list_ratio = []

    for i in range(n):

        food = input()
        length = len(food)

        list_foods.append(food)
        list_len.append(length)

        vowels = 0
        for char in food:
            if char =='a' or char == 'e' or char == 'i' or char =='o' or char == 'u':
                vowels += 1

        list_vow.append(vowels)
        list_ratio.append(vowels/length)

    min_ratio = min(list_ratio)
    list_same_ratio = []
    count_index = 0

    for r in list_ratio:
        if r == min_ratio:
            list_same_ratio.append(count_index)
        
        count_index +=1

    # if Ratio has one max value
    if len(list_same_ratio) == 1:
        index = list_same_ratio[0]
        print(f'{list_foods[index]} {list_vow[index]}/{list_len[index]}')

    # if Ratio has few max values
    elif len(list_same_ratio) > 1:
        
        # get the index of the max value from the list_vowels
        max_vow_index = list_vow.index(max(list_vow))

        # check if max vowel value repeats in list_vowels and
        # if repeats then get their indexes
        list_same_vowels = []
        for ind in list_same_ratio:
            if list_vow[max_vow_index] == list_vow[ind]:
                list_same_vowels.append(ind)
        
        list_same_vowels.append(max_vow_index)

        # if the max value of list_vowels not repeats 
        if len(list_same_vowels) == 1:
            print(f'{list_foods[max_vow_index]} {list_vow[max_vow_index]}/{list_len[max_vow_index]}')
        
        # if the max value repeats in list vowels
        # then the list_same_vowels will have length > 1
        elif len(list_same_vowels) > 1:
            max_len_index = list_len.index(max(list_len))
            print(f'{list_foods[max_len_index]} {list_vow[max_len_index]}/{list_len[max_len_index]}')
