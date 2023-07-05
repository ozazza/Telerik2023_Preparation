n = int(input())

if n >= 1 and n <= 10:

    for i in range(n):
        lst = input().split(',')

        if len(lst) >= 1 and len(lst) <= 20:
            
            sorted_numbers = []
            sorted_strings = []

            for s in lst:
                sorted_numbers.append(int(s))
            
            sorted_numbers.sort()


            for t in sorted_numbers:
                sorted_strings.append(str(t))

            if lst == sorted_strings:
                print('true')
            else:
                print('false')
