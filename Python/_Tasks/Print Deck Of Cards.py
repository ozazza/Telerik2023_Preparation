card = input()

start_deck = 2

# if card is not a digit then end of range is one of the below:
j = 11
q = 12
k = 13
a = 14

str_j = 'J'
str_q = 'Q'
str_k = 'K'
str_a = 'A'

end_deck = 0
if card == str_j: end_deck = j + 1
elif card == str_q: end_deck = q + 1
elif card == str_k: end_deck = k + 1
elif card == str_a: end_deck = a + 1
else: end_deck = int(card) + 1

for i in range(start_deck, end_deck):
    
    if i == end_deck: break
    else:
        if i <= 10: print(f'{i} of spades, {i} of clubs, {i} of hearts, {i} of diamonds')
        if i == j: print(f'{str_j} of spades, {str_j} of clubs, {str_j} of hearts, {str_j} of diamonds')
        if i == q: print(f'{str_q} of spades, {str_q} of clubs, {str_q} of hearts, {str_q} of diamonds')
        if i == k: print(f'{str_k} of spades, {str_k} of clubs, {str_k} of hearts, {str_k} of diamonds')
        if i == a: print(f'{str_a} of spades, {str_a} of clubs, {str_a} of hearts, {str_a} of diamonds')

