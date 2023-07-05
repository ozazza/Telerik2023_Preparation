# Write a program that displays the name of the season 
# associated with a given date and month. 
# Use the table below to determine the season's start 
# and end dates.

# Season	Start Date
# ----------------------
# Spring	March 20
# Summer	June 21
# Autumn	September 22
# Winter	December 21

# For example, Autumn lasts from September 22 to December 20,
# both inclusive.

month = input()
date = int(input())

if (month == 'March' and date >= 20) or (month == 'June' and date <= 20) or (month == 'April' or month == 'May'):
    print('Spring')
elif (month == 'June' and date >= 21) or (month=='September' and date <= 21) or (month=='July' or month == 'August'):
    print('Summer')
elif (month == 'September' and date >= 22) or (month == 'December' and date <= 20) or (month == 'October' or month == 'November'):
    print('Autumn')
else:
    print('Winter')