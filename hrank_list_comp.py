## Problem from hacker rank website, titled "List Comprehensions".

# Problem statement: 
'''
Given three integers x, y and z representing the dimensions of a cuboid along 
with an integer n. Print a list of all possible coordinates given by (i, j, k) 
on a 3D grid where the sum of i+j+k is not equal to n. Here, 0<=i<=x; 0<=j<=y;
0<=k<=z.
'''
# Sample IO:
# input:
'''
x, y, z, n = 1, 1, 2, 3

All permutations of [i, j, k] are:
[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 0, 0], 
[1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2]]
'''
# Output
'''
The list of all elements that do not sum to n = 3:
[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], 
[1, 1, 0], [1, 1, 2]]
'''
# Constraints
'''
Print the list in lexicographic increasing order.
'''

# Code:

def coordinates(x, y, z, n):
    return [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]

if __name__ == '__main__':
    
    x, y, z, n = map(int, input().split())
    
    print(coordinates(x, y, z, n))