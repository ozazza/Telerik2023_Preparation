# 0.5L bottles $0.1 deposit
# 1L bottles $0.25 deposit
#  You must print two digits after the decimal point.

half = float(input()) * 0.1
big = float(input()) * 0.25
total = format(half+big, '.2f')
print(total)