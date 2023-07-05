lst = input().split(', ')
target = input()

# alone and different
for i in range(1, len(lst)-1, 1):
    number = lst[i]
    left = lst[i - 1]
    right = lst[i + 1]
    
    if number == target and number != left and number != right:
        if left > right:
            number = left
        elif left < right:
            number = right
        else:
            number = left
    lst[i] = number

print(f"[{', '.join(lst)}]")