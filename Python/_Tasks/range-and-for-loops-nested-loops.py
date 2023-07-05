for n in range(1, 11, 3):
    print(n)

my_name = 'Mario'

for c in my_name:
    code = ord(c)
    print(f'{c} code = {code}')

# 3 * 5
# *****
# *****
# *****

row = int(input())
col = int(input())

for r in range(row):
    st = '*'
    stars = ''
    
    for c in range(col):
        stars += st
    
    print(stars)

row1 = int(input())
col1 = int(input())

for r in range(row1):
    for c in range(col1):

        # end = '' print stays on same line 
        print('*', end ='') 
    
    print()


# Break statements

hidden_letter = 'h'

while True:
    your_input = input()

    if hidden_letter == your_input:
        print('You guessed correctly')
        break

    elif hidden_letter > your_input:
        print('My letter is larger than your letter')
    else:
        print('My letter is smaller than your letter')

