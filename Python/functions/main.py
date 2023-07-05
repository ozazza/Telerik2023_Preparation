print('Hello')
print
print()
print('Hi')

x = 1
x = 6//2
print(x)

language = 'python'
first =language[0]
fourth = language[3]
print(first, fourth)
print(len(language))

# Characters
text = 'Q&A'
print(ord(text[0]))
print(ord(text[1]))
print(ord(text[2]))

print(chr(81))

first_chr = chr(81)
second_chr = chr(38)
third_chr = chr(65)
print(first_chr, second_chr, third_chr)

# Slicing
text = 'Python Language'
first_slice = text[0:6]
second_slice = text[7:]
print(first_slice, second_slice)

# Format
template= 'Country: {}, Capital: {}, Population: {}'
print(template.format('Bulgaria', 'Sofia', '6.8m'))
print(template.format('Philippines', 'Manila', '110m'))

first_name = 'Jane'
last_name = 'Smith'
print(f'First name {first_name}, Last name {last_name}')

# Read three numbers
# print their sum
# print the max number, max()

# line1 = input('a = ')
# line2 = input('b = ')
# line3 = input('c = ')
# print(line1, line2, line3)

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
# print(line1+line2+line3)

print('a + b + c = ', a + b + c)

max_num = max(a,b,c)
print('max: ', max_num)