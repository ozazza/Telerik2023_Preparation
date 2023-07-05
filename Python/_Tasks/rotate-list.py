input_list = input().split(',')
n = int(input())

for i in range(n):
    
    popped = input_list.pop(0)
    input_list = input_list[0:]
    input_list.append(popped)

print(','.join(input_list))
