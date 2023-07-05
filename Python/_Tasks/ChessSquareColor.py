label = input()
rank = int(input())

dark = 'dark'
light = 'light'
color =''

if  label =='b' or label =='d' or label =='f' or label =='h':
    if rank % 2 == 0:
        color = dark
    else:
        color = light
else:
    if rank % 2 == 0:
        color = light
    else:
        color = dark

print(color)