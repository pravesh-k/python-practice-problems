## Problem from hacker rank website, titled "python string formatting".

# Problem statement: 
'''
You are given an integer, N. Your task is to print an alphabet rangoli of size N. 
(Rangoli is a form of Indian folk art based on creation of patterns.)
'''
# Sample Design:
'''
#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''
# Input Format
'''
Only one line of input containing size of the rangoli.
'''
# Constraints
'''
1 <= size <= 27
'''

# Code:
def print_rangoli(size):
    rows_in_rangoli = 2*size

    for i in range(1, rows_in_rangoli):
        if i > size:
            i = rows_in_rangoli - i
    
        alpha_pattern = list(map(chr, range(ord('a')-1+size, ord('a')-1+size-i, -1)))
        # print(alpha_pattern)
        alpha_pattern += alpha_pattern[:len(alpha_pattern)-1][::-1]
        print('-'.join(alpha_pattern).center((4*size-3), '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)