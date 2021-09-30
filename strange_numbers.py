## This problem appeared in TCS Digital Exam | TCS Elevate Wings 1 DCA Exam

#  Problem statement: Check if a number is strange or not (A strange number
#  is a natural number whose greatest prime factor is strictly greater
#  than it's square root)

#  Example Input: 14
#  Output: Strange (because largest prime factor of 14 is 7 
#  which greater than square root of 14 which is 3.741)

from math import sqrt

def largestPrimeFactor(n):

	# finding the largest prime factor of the given number
	max = -1
	while n % 2 == 0:
		max = 2
		n >>= 1

	for i in range(3,int(sqrt(n))+1,2):
		while n % i == 0:
			max = i
			n = n / i

	if n > 2:
		max = n

	return max

# function to check if a number is straneg or not
def checkStrange(n):
	
	factor = largestPrimeFactor(n)
	if factor > sqrt(n):
		return True
	else :
		return False

# driver code
if __name__ == '__main__':
	
	n = int(input())
	
	if checkStrange(n):
		print("Strange")
	else:
		print("Not Strange")
