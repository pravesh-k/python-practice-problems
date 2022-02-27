## Problem from hacker rank website, titled "py if else".

# Problem statement: 
'''
Given an integer, n, perform the following conditional actions:

If n is odd, print "Weird"
If n is even and in the inclusive range of 2 to 5, print "Not Weird"
If n is even and in the inclusive range of 6 to 20, print "Weird"
If n is even and greater than 20, print "Not Weird"
'''
# Input Format
'''
A single line containing a positive integer, n.
'''
# Constraints
'''
1 <=n <= 100
'''

# function to find if a number is weird or not weird
def nature(n):
    even = lambda n: n%2==0
    if even(n) and (n in range(2, 6) or n > 20):
        return 'Not Weird'
    else:
        return 'Weird'
        

if __name__ == '__main__':
    n = int(input('Enter a number\t').strip())
    print(nature(n))