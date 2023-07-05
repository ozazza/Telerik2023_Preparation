price = float(input())
customer = float(input())

change = customer - price
leva = int(change)
stotinki = change - leva
tens = int(stotinki * 10)
hundreds = int(round(stotinki * 10 - tens, 2)*10) 

if change > 0:
    if leva >= 1:
        print(f'{str(leva)} x 1 lev')
    if stotinki > 0:
        
        if tens > 0:
            if tens > 5:
                tens -= 5
                print('1 x 50 stotinki')

            if tens > 3:
                tens -= 4
                print('2 x 20 stotinki')
            
            if tens > 2:
                tens -= 3
                print('1 x 20 stotinki')
                print('1 x 10 stotinki')
            
            if tens > 1:
                tens -= 2
                print('1 x 20 stotinki')

            if tens == 1:
                tens -= 1
                print('1 x 10 stotinki')
        
        if hundreds > 0:
            if hundreds >= 5:
                hundreds -= 5
                print('1 x 5 stotinki')

            if hundreds > 3:
                hundreds -= 4
                print('2 x 2 stotinki')
            
            if hundreds > 2:
                hundreds -= 3
                print('1 x 2 stotinki')
                print('1 x 1 stotinka')
            
            if hundreds > 1:
                hundreds -= 2
                print('1 x 2 stotinki')

            if hundreds == 1:
                hundreds -= 1
                print('1 x 1 stotinka')
else:
    print(change)
