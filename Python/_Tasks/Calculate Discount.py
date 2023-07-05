discount = 0.65

items = int(input())

for i in range(items):
    p = input()
    
    price = float(p)
    total = price - price * discount

    print(f'{total:.2f}')