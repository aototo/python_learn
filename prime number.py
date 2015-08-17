
def prime(a):
            for n in range(3,int(a+1)):
                    for x in range(2,n):
                              if n%x > 0:
                                        if n == x+1:
                                                  print(n)
                                                  break
                              else:
                                        break