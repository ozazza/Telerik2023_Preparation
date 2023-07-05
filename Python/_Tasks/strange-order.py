numbers = input().split(',')

if len(numbers) >= 1 and len(numbers) <= 20:

  result = []

  for s in numbers:
    if int(s) < 0:
      result.append(s)
  for s in numbers:
    if int(s) == 0:
      result.append(s)
  for s in numbers:
    if int(s) > 0:
      result.append(s)

  print(','.join(result))