def gcdIter(a, b):
          y = 1
          x = 2
          while x<= min(a,b):
                    if a%x ==0 and b%x==0:
                              a = a / x
                              b = b / x
                              y *= x
                              x =2
                    else:
                              x+=1
          print(y)
