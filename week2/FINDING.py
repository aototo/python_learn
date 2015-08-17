epsilon = 0.1
y = 9
guess = y/2.0

while abs(guess*guess - y ) >= epsilon:
  guess = guess -((( guess**2 ) - y ) / (2*guess ))
  print(str(guess))
  
print(" Square root or " + str(y) + 'is about' + str(guess) )
