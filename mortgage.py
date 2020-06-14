# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payement_start_month = int(input('please enter the extra_payement_start_month: '))
extra_payement_end_month = int(input('please enter extra_payement_end_month: '))
extra_payment = int(input('please enter the extra payement: '))


while principal > 0 :
    if extra_payement_start_month <= month and month <= extra_payement_end_month:
        payment = extra_payment + payment
    
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    payment = 2684.11
    month = month + 1
    print(month, round(total_paid, 2), round(principal, 2))

overpayement = payment + principal

#print('Total paid {} over {} months'.format(round(total_paid - overpayement, 2), month))
print(f'Total paid ${total_paid:0.2f} over {month} months')
