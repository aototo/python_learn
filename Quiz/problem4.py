def f(s):
    return 'a' in s

def satisfiesF(L):
          alist = []
          if len(L) == 0:
                    print(0)
          else:
                    for a in L:
                              if f(a):
                                        alist.append(a)
                                        L = alist
                    print(len(L))

satisfiesF([])

