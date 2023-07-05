n = input()

str_n = str(n)
str_list = []

for c in str_n:
    str_list.append(c)

reverse = []
for s in range(len(str_list)-1, -1, -1):
    reverse.append(str_list[s])

reversed_digit = ''.join(reverse)
# digit_as_number = float(reversed_digit)

# if digit_as_number % 1 == 0:
#     print(int(digit_as_number))
# else:
    # print(reversed_digit)

print(reversed_digit)


# --------------
# x = input()

# outputString = list()

# for i in range(len(x)):
#     outputString.append(x[len(x)-1-i])

# print("".join(outputString))

# --------------
# n = input()

# for i in n[::-1]:
#     print(i, end = '')