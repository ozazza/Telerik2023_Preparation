# 1 hour of free calls and 
# 20 text messages 
# for 12.00 levas.

# minute costs 0.10 levas
# each additional message costs 0.06 levas
# any additional minutes/text messages are subject to 20% sales tax.

#  calculates the additional 
# charge for text, the additional 
# charge for minutes, 
# and the sales tax charge for both. 
# Also, display the total amount paid.

messages = int(input())
minutes = int(input())

free_mess = 20
free_mins = 60
price_plan = 12

messages = messages - free_mess if messages >= free_mess else 0
minutes = minutes - free_mins if minutes >= free_mins else 0

mess_price = float(0.06 * messages) if messages > 0 else 0
mins_price = float(0.1 * minutes) if minutes > 0 else 0
tax = float(mess_price * 0.2 + mins_price * 0.2) if mess_price > 0 or mins_price > 0 else 0
total_amt = float(mess_price + mins_price + tax + price_plan)
 
print('{0} additional messages for {1:.2f} levas'.format(messages, mess_price))
print('{0} additional minutes for {1:.2f} levas'.format(minutes, mins_price))
print('{:.2f} additional taxes'.format(tax))
print('{:.2f} total bill'.format(total_amt))