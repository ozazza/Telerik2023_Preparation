n = input()

result = ''

if n.isdigit() and int(n) >= 0 and int(n) < 10:
    s = int(n)
    if s == 1:
        result = 'one'
    elif s == 2:
        result = 'two'
    elif s == 3:
        result = 'three'
    elif s == 4:
        result = 'four'
    elif s == 5:
        result = 'five'
    elif s == 6:
        result = 'six'
    elif s == 7:
        result = 'seven'
    elif s == 8:
        result = 'eight'
    elif s == 9:
        result = 'nine'
    elif s == 0:
        result = 'zero'
else:
    result = 'not a digit' 

print(result)