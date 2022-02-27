## Problem from hacker rank website, titled "designer door mat".

# Problem statement: 
'''
Mr. Vincent works in a door mat manufacturing company. One day, he designed 
a new door mat with the following specifications:

Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
'''
# Input Format
'''
A single line containing the space separated values of N and M.
'''
# Constraints
'''
5 < N < 101
15 < M < 303
'''
# Sample Design
'''
For Size: 7 x 21 

---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
'''

def door_mat(n,m):
    for i in range(0,n):
        if i==n//2:
            print('WELCOME'.center(m, '-'))
        elif i<n//2:
            print(((2*i+1)*'.|.').center(m, '-'))
        else:
            print((((2*n)-(2*i+1))*'.|.').center(m, '-'))


if __name__ == '__main__':
    n, m = input().split(" ")
    door_mat(int(n), int(m))