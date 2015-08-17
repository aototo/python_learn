def lenIter(aStr):
          '''
          ater: a string
          returns: int , the length of aStr
          '''

          #Your code here
          length = 0
          for x in aStr:
                    length +=1
          return length



def lenRecur(aStr):
          if  aStr != '':
                    return 1+ lenRecur(aStr[1:])
          else:
                    return 0


def semordnilap(str1, str2):
          if len(str1)!=len(str2):
                    return False
          if str1=='' and  str2=='':
                    a_str1 = str1[0:1]
                    a_str2 = str2[-1]
                    if a_str1 == a_str2:
                              print(a_str1,a_str2)
                              return semordnilap(str1[1:], str2[:-1])
                    else:
                              return False
          else:
                  return True 


def fibMetered(x):
    global numCalls
    numCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fibMetered(x-1) + fibMetered(x-2)

def testFib(n):
    global numCalls
    numCalls = 0
    for i in range(n+1):
        print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
        print ('fib called ' + str(numCalls) + ' times')

testFib(10)
