import datetime

class Person( object ):
          def __init__(self,name):
                    """create a person called name """
                    self.name = name
                    self.birthday = None
                    self.lastName = name.split(' ')[-1]

          def getLastName(self):
                    """ return selfs last name  """
                    return self.lastName

          def setBirthday(self,month,day,year):
                    """  """
                    self.birthday = datetime.date(year , month ,day)

          def getAge(self):
                    """ return self a current age in daya """
                    if self.birthday == None:
                              raise ValueError
                    return (datetime.date.today() - self.birthday).days

          def __it__(self,other):
                    if self.lastName == other.laseName:
                              return self.name < other.name
                    return self.lastName < other.lastName
          #other methods

          def __str__(self):
                    """ return self's name """
                    return self.name



##L12 PROBLEM 5

def genPrimes():
          primes = []    # primes generated so far
          last = 1            # last number tried
          while True:
                    last +=1
                    for p in primes:
                              if last % p == 0:
                                        break
                    else:
                              primes.append(last)
                              yield last
