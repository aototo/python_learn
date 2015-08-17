# Python edX #
##Week 1 Lecture 1##
what dies a computer do?

* Fundamentally a computer:
	- Performs calculations
	- Remenbers the results

constructor 

***calculations*** 计算

* What calculations?
	- Built in primitives
	- Creating our own methods of calculating


###are simple calculations enough
* Searching the World Wide Web
* Playing chess

***algorithms*** 算法

***
### BASIC MACHINE ARCHITECTURE

How do we capture a recipe in a mechanical process?

* Build a machine to conpute square roots
 	
 	#####--Fixed Program Computers
 	* Calculator
	* Atanasoff and Berry's(1941)computer for systems of linear equations
	* Alan Turing's(1940's)bombe - decode Enigma codes

It's a stored program computer.

****
###Stored program computer
* Sequence of instructions(program)stored inside computer
	* Built form predefined set of primitive instryctions
		* Arithmetic and logic
		* Simple tests
		* Moving data

***memory*** 内存
***
###PROGRAMMING LANGUAGE CHARACTERISTICS

***primitives*** 基本类型

Determines whether a string is legal --***Syntax***

Determines whether a string has meaning --***Static semantics***

Assigns a meaning to a legal sentence --***Semantics***
***
##Week Lecture 2
###TYPES OF PROGRAMMING LANGUAGES###
***instructions*** 指令
***interpretive language.***

Basically inside of Python there are three different
kinds of scalar objects.

>***multiplication*** [*]

>***addition*** [ + ] 

>***subtravtion*** [ - ]

>***parentheses*** [ () ]

>***greater than***[ > ]

>***equal to***[ = ]

>***quotes***[ "" ]

***type conversion*** type 转换！


method   | Description
-------  | -------------
round    | round(number,lenght)
str		  | conversion to string
len      |lenght
type  	  | Get type 
lower()  |Uppercase lowercase turn
upper    |Lowercase uppercase turn
ord(char)     | Get the ASCII number of a character
chr(number)| Get the character given by an ASCII number

conditional（bool）
***
##Week 2

###ITERATION

	>>> range(5)
	[0, 1, 2, 3, 4]
	
	>>> range(2, 5)
	[2, 3, 4]
***
	
	>>> abs(-1.2) 
 	1.2
  
	>>> abs(-11216.5) 
	11216.5
#####Uppercase lowercase turn

	>>> a = "AA"
	>>> a.lower()
	"a"
#####Lowercase uppercase turn
	
	>>> a="aa"
	>>> a.upper()
	"A"
	
#####key in
	>>> "a" in "asdasd"
	True
	
#####isupper,index,count,replace
	>>> str1="exterminate!"
	>>> str1.isupper()
	False
	
	>>> str1.index('e')
	0
	
	>>> str1.count('e')
	3
	
	>>> str1.replace('e', '*') 
	'*xt*rminat*!'
	
#####Capitalize,Swapcase,find
	>>> str2 = 'number one - the larch'
	
	>>> str2.capitalize()
	'Number one - the larch'
	
	str2 = 'Number one - the larch'
	>>> str2.swapcase()
	'nUMBER ONE - THE LARCH'
	
	>>> str2.find('n')
	0
	>>> str2.find('!')
	-1
	
	
##week 3

ITERATIVE ALGORITHMS 

	def iterMul(a,b):
		result = 0
		while b > 0:
			result += a
			b -=1
		return result
		
recursive algorithm:		
		
	def recurMul(a,b):
		if b == 1:
			return a
		else:
			return a + recurMul(a,b-1)
			
			
Euclid's 算法
		
		
		if b == 0:
      		return a
    	else:
			return gcdRecur(b, a mod b)
			
		二
		
		while b:
			x = a
			a = b
			b = a % b 
		retuen a
       	
       	
##tuple
	>>> t = ("a", "b", "mpilgrim", "z", "example") 
	>>> t
	('a', 'b', 'mpilgrim', 'z', 'example')
	>>> t[0]                                       
	'a'
	>>> t[-1]                                      
	'example'
	>>> t[1:3]
	
##Lists
append()

	>>> Techs=["22","123"]
	>>> Techs.append('112')
	>>> Techs
	['22', '123', '112']
	
range()
	
	range(10, 3, -1)
	[10, 9, 8, 7, 6, 5, 4]
	-----------------------
	>>> aList = range(1, 6)
	>>> bList = aList
	>>> aList[2] = 'hello'
	>>> aList == bList
	True

insert()

	>>>listA.insert(2,100) -> 2 is index
	
index()
	
	>>> listA
	[100, 0, 1, 4, 7]
	>>> listA.index(1)
	>>> 2

	>>> listA.pop(4)
	>>> 7
	
	
##week4

###LECTURE 7 INTRODUCTION - TIME

***************

###TESTING AND DEBUGGING
#####Testing and Debugging
* Would be great if our code always worked properly the first time we run it!
* But life ani't perfect , so we need:
	* Testing methods 
		* Ways of trying code on examples to determine if running correctly
	* Debugging methods
		* Ways of fixing a program that you know does not work as intended

#####When should you test and debug?
* Design your code for ease of testing and debugging
	* Break program into components that can be tested and debugged independently

#####When are you ready to test?
* Ensure that code will actually run 
	* Remove syntax errors
	* Remove static semantic errors
	* Both of these are typically handled by Python interpreter

####Testing
* Goal:
	* Show that bugs exist
	* Would be great to prove code is bug free, but generally bard
	* generally hard 
		* Usually can't run on all possible inputs to check
		* Formal methods sometimes help,but usually only on simpler code
		

#### Test suite
* Want to find a collection of inputs that has high likelihood of revealing bugs,yet is efficient 
	* Partition space of inputs into subsets hat provide equivalent information about correctness
		* Partition space of inputs into subsets such that each element of set is in exactly one subset
	* Construct test suite that contains one input from each element of partition
	* Run test suite

				Example of partition
				def isBigger(x,y):
					"""Assumes x and y are ints
						returns True if x is less than y
						else False """
				* input space is all pairs of integers
				* Possible partition
					- x positive , y positive
					- x negative , y negative
					- x positive , y negative
					- x negative , y positive
					- x = 0 , y = 0
					- x = 0 , y!=0
					- x !=0 , y =0

####Why this partition?
* Lots of other choices
	- E.g.,x prime , y prime, x not; both prime; both not
* Spaces of inputs often have natural boundaries
	- Integers are positive , negative or zero
	- From this perspective , have 9 subsets
		* Split x = 0 , y != 0 into x = 0 ,y positive and x = 0 , y negative
		* Same for x != 0 , y = 0

####Partitioning
* What if no natural partition to input space?
	- Random testing - probability that code is correct increases with number of trials; but should be able to use code to do better
	- Use heuristics based on exploring paths through the specifications ***- black-box testing***
	- Use heuristics based on exploring paths through the code ***- glass-box testing***
	
####Black-box testing
* Test suite designed without looking at code 
	- Can be done by someone other than implementer
	- Will avoid inherent biases of implementer, exposing potential bugs more easily
	
			def sqrt(x,eps):
				"""Assumes x ,eps floats
						x >= 0
						eps > 0
					returns res such that 
						x-eps <= res*res <= x+eps """
						
			* Paths through specification:
				- x = 0
				- x > 0

####Paths through a specification
* Also good to consider boundary cases 
	- For lists: empty list , singleton list , many element list
	- For numbers , very small , very large , "typical"
	


####Glass-box Tesying
* Use code directly to guide design of test cases
* Glass-box test suite is path-complete if every potential path through the code is tested at least once 
	- Not always possible if loop can be exercised arbitrary times , or recursion can be arbitrarily deep
* Even path-complete suite can miss a bug,depending on choice of examples

			def abs(x):
				"""Assumes x is an int
					returns x if x>=0 and -x otherwise """
					if x < -1:
						return -x
					else:
						return x
			* Test suite of {-2,2} will be path complete
			* But will miss abs(-1) which incorrectly returns -1
				- Testing boundary cases and typical cases would catch this {-2 -1 ,2}
				
				
####Conducting tests
* Start with ***unit testing***
	- Check that each module (e.g. function) works correctly
* Move to ***integration testing***
	- Check that system as whole works correctly

####Test Drivers and Stubs
* Drivers are code that
	- Set up environment needed to run code
	- Invoke code on predefined sequence of inputs 
	- Save results , and 
	- Report

* Drivers simulate parts of program that use unit being tested
* ***Stubs*** simulate parts of program used by unit being tested
	- Allow you to test units that depend on software not yet written

	
###Debugging

* The "history" of debugging
	- Often claimed that first bug was found by team at Harvard that was working on the Mark II Aiken Relay Calculator

	
###EXCEPTIONS

***
###ASSERTIONS - TIME


##Week5

###Computational complexity
* How much time will it take a program to run?
* How much memory will it need to run?
Need to balance minimazing computational
complexity with conceptual complexity
	* -Keep code simple and easy to understand , but where possible optimize performance

###How do we measure complexity
* Given a function , would like to answer:"How long will this take run?"
* Could just run on some input and time it.
* Problem is that this depends on:
	1.	Speed of computer
	2. Specifics of Python implementation
	3. Value of input
* Avid(1)and(2)by measuring time in terms of number of basic steps executed

###Cases for measuring complexity
* Best case: minimum running time over all possible inputs of a given size 
	-	For linearSearch - constant , i.e.independent of size of inputs
* Worst case : maximum running time over all possible inputs of a given size
	- For linearSearch - linear in size of list
* Average (or expected)case : average running time over all possible inputs of a given size
* We will focus on worst case - a kind of ***upper bound*** on running time

###Complexity classes
* 
