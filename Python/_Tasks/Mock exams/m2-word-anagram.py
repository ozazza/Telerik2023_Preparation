w = input()
n = int(input())

words = []

for m in range(n):
    words.append(input())

for word in words:

    if len(word) == len(w):
        break_counter = 0
        
        # word = sorted(word)
        # w = sorted(w)

        for char in word:

            if char not in w:
                break_counter += 1
                break
        
        for ch in w:
            if ch not in word:
                break_counter += 1
                break

        # if the 2 breaks not fall then
        if break_counter < 1:
            print('Yes')
        else:
            print('No')

    else:
        print('No')
