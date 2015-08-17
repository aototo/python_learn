s='abcdabcdefadddabcdefg'
str_len = len(s)
longest = 1
s_2=""
s_3=""
before_single_s=""
for x in s:
          if( x >= before_single_s):
                    s_2 += x
                    s_2_len = len(s_2)
                    if longest==str_len:
                              if( len(s_3) < len(s_2) ):
                                s_3=s_2
          else:
                    if( len(s_3) < len(s_2) ):
                                s_3=s_2
                    s_2 = x                               
          before_single_s = x
          longest += 1
print('Longest substring in alphabetical order is: '+ s_3)
