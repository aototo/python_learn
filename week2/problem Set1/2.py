s = 'bobbwboxboboboboboftnyx'
Count = 0
sLen = len(s)
a= -1
for x in range(sLen):
          a = s.find('bob',a+1)
          if(a!=-1):
                    Count += 1
                    continue
          else:
                    break
print("Number of vowels: "+str(Count))

