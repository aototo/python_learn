print("Please think of a number between 0 and 100!")
high = 100
low = 0
nowCorrect = int(( high + low ) / 2)
print('Is your secret number '+ str(nowCorrect) + '?')
while True:
   input_value = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
   if input_value  =='l':
      low = nowCorrect
      nowCorrect = int((high + low)/2)
      print('Is your secret number '+ str(nowCorrect) + ' ?')
   elif input_value  =='h':
      high = nowCorrect
      nowCorrect = int((high+low)/2)
      print('Is your secret number '+ str(nowCorrect) + ' ?')
   elif input_value  =='c':
      print('Game over. Your secret number was:  '+str(nowCorrect))
      break
   else:
      print('Sorry, I did not understand your input.')
      print('Is your secret number '+ str(nowCorrect) + ' ?')


      
