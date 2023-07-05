n = input()

# numbers = []
# sum = 0

# for i in n:
#     numbers.append(int(i))

# for s in numbers:
#     if s < 2: 
#         sum += s
#     else: 
#         if sum < 2:
#             sum += s
#         else:
#             sum *= s

# print(sum)

result = []
first = int(n[0]) 
mid = int(n[1]) 
last = int(n[2]) 

result.append(first + mid + last)
result.append(first * mid + last)
result.append(first + mid * last)
result.append(first * mid * last)

print(max(result))