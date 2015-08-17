balance = 320000
annualInterestRate = 0.2
x= 0
Monthlyinterestrate = annualInterestRate/12.0
bl_balance = balance 
min_payment = balance / 12.0
max_payment =balance *( 1+ Monthlyinterestrate )** 12/12
guess = (min_payment + max_payment ) / 2.0

print(min_payment)
print(max_payment)
print(guess)
while abs(balance) > 0.01:
          balance = bl_balance
          for n in range(12):
                    balance = ( balance - guess )* Monthlyinterestrate + ( balance - guess )
          if balance >0:
                    min_payment = guess
                    guess = ( min_payment + max_payment ) / 2
          if balance < -0:
                    max_payment = guess
                    guess = ( min_payment + max_payment ) / 2
         
print("Lowest Payment: "+str(round((guess),2)))
