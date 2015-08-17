balance = 3806
annualInterestRate = 0.15

Monthlyinterestrate = annualInterestRate/12
bl_balance = balance
min_payment = balance / 12
while balance > 0:
          balance = bl_balance
          for n in range(12):
                    balance = ( balance - min_payment )* Monthlyinterestrate + ( balance - min_payment )                 
          min_payment += 1
          print(min_payment )
lowest_Payment = round((round(min_payment)+4)/10)*10
print('Lowest Payment: '+str(lowest_Payment))
