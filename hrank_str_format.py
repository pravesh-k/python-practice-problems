## Problem from hacker rank website, titled "python string formatting".

# Problem statement: 
'''
Given an integer, , print the following values for each integer  from  to :
1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary

Complete the print_formatted function.
print_formatted has the following parameters: int number: the maximum value to print

The output should be printed in a manner such that the four values must be printed 
on a single line in the order specified above for each i from 1 to number. Each value 
should be space-padded to match the width of the binary value of number and the 
values should be separated by a single space.
'''
# Input Format
'''
A single integer denoting n
'''
# Constraints
'''
1 <= n <= 99
'''

# Code:
def print_formatted(number):
    s = len(bin(number)[2:])
    for i in range(1, n+1):
        print(f'{str(i).rjust(s)} '
            f'{str(oct(i))[2:].rjust(s)} '
            f'{str(hex(i)).upper()[2:].rjust(s)} '
            f'{str(bin(i))[2:].rjust(s)}')
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)