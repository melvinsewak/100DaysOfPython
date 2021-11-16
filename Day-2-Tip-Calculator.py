print('Welcome to tip calculator')
total_bill_amount = float(input('Enter the total bill amount: '))
total_tip_perc = float(input('Enter the tip in percentage: '))
total_people = int(input('Enter the number of people: '))
per_person_amount = total_bill_amount*(1+total_tip_perc/100)/total_people
per_person_amount = round(per_person_amount, 2)
print(f'Each has to pay {per_person_amount}')