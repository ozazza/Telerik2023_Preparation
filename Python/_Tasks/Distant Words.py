t = int(input())
n = int(input())

if t >=0 and t <= 1000 and n >= 1 and n <= 20:
    list_words = []
    list_distances = []
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # Add words from input
    for i in range(n):
        word = input()
        list_words.append(word)
    
    # Add each word in list in order to check each char number +1 in Alphabet
    total_distance = 0
    for each_word in list_words:

        sum = 0
        distance = 0
        for char in each_word:
            for c in abc:
                if char == c:
                    sum += abc.index(c) + 1
                    
                    break
        
        distance = abs(t - sum)       
        total_distance += distance
        list_distances.append(distance)
    
    for r in range(n):
        print(f'{list_words[r]} {list_distances[r]}')
    
    print(f'{round(total_distance / n, 2):.2f}')