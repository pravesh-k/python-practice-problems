## This problem appeared in TCS Digital Exam | TCS Elevate Wings 1 DCA Exam

#  Problem statement: Find the sum of digits of a given number until 
#  the final sum is a 1 digit number and if final sum is 1 then 
#  print "UNO" otherwise print "NOT UNO"

#  Example Input: 51112
#  Output: UNO (because 5+1+1+1+2=10 then, 1+0=1)

n = int(input())

def digSum( n):
	sum = 0
	
	while(n > 0 or sum > 9):
		
		# if n has become 0 then 
		# sum will be the new n
		if(n == 0):
			n = sum
			sum = 0
		
		# adding the last digit 
		# to sum and removing it 
		# from the number
		sum += n % 10		
		n //= 10
	
	return sum

# driver code
r = digSum(n)

if r == 1:
    print("UNO")
else:
    print("NOT UNO")