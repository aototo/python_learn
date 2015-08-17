def clip(lo, x, hi):
    pi =2
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise  hi<  x > lo 
    '''
    # Your code here
    return min(max(x,lo),hi)
          
    
