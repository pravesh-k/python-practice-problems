## Problem pattern printing.

# Problem statement: 
'''
Given the size, print a hollow diamond a shown in the sample design.
'''
# Sample input:
'''
size = 5
'''
# Constraints
'''
Size should be an odd number.
'''
# Sample Design:
'''
   *        s = 0
  * *       s = 1 
 *   *      s = 3
*     *     s = 5
 *   *      s = 3
  * *       s = 1
   *        s = 0
'''

# Code
def hollow_diamond(s):
    
    ls = list(range(1,s,2))+list(range(s-4,0,-2))
    print('*'.center(s))
    for i in ls:
        print(('*'+i*' '+'*').center(s))
    print('*'.center(s))

hollow_diamond(int(input('Enter size as an odd integer:\t')))