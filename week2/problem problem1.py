balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
MinimumMonthlyPayment = 0
UnpaidBalance = 0
RemainingBalance = 0
Totalpaid = 0
for n in range(1,13):
          MinimumMonthlyPayment = balance* monthlyPaymentRate
          UnpaidBalance = balance - MinimumMonthlyPayment;
          
          RemainingBalance = ( balance - MinimumMonthlyPayment ) * ( annualInterestRate/12 ) + UnpaidBalance
          balance = RemainingBalance
          Totalpaid += MinimumMonthlyPayment
          print("Month: "+str(n))
          print("Minimum monthly payment:" + str(round( MinimumMonthlyPayment*100 )/100 ))
          print("Remaining balance:" + str( round( RemainingBalance*100 )/100  ))
          if n == 12:
                    print("Totalpaid:" +str( round(Totalpaid *100)/100 ))
                    print("Remaining balance:" + str( round( RemainingBalance*100 )/100  ))
