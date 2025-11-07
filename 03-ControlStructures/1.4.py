###
# Credit card payment 
#
account_balance = 500
total_payment = int(input("podaj kwotę płatności "))

if total_payment < account_balance:
    print('Payment completed')
    print(f"pozostałe środki {account_balance - total_payment}")
else:
    print('No funds')

