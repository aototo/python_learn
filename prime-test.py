#!/usr/bin/python
# Yunen

# a > 1
def is_prime(a):
    result = True
    for n in range(2, a):
        if a % n == 0:
            result = False
            break           
    return result

def test():
    # prime numbers from 2 to 100
    prime_numbers = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    passed = True
    
    for n in range(2, 101):
        if is_prime(n):
            if n not in prime_numbers:
                passed = False
                print(str(n) + " is not a prime number.")
                break
        else:
            if n in prime_numbers:
                passed = False
                print(str(n) + " is not a prime number.")
                break        
    
    if passed:
        print("passed all test cases!")
  
test()
