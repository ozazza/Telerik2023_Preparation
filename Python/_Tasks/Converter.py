# 1 gallon = 4.54 litres and 
# 1 mile = 1.6 km
# MPG (miles per gallon)

m = int(input())

km_per_gallon = float(m * 1.6)
liters_per_km = float(4.54/ km_per_gallon)

result = int(liters_per_km * 100)

print('{} litres per 100 km'.format(result))