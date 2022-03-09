## Problem from hacker rank website, titled "Find the Runner-Up Score!".

# Problem statement: 
'''
Given the participants' score sheet for your University Sports Day, you 
are required to find the runner-up score. You are given n scores. Store 
them in a list and find the score of the runner-up.

n = number of scores
arr = list of scores
'''
# Sample IO:
# input:
'''
5
2 3 6 6 5
'''
# Output
'''
5
'''
# Constraints
'''
2 <= n <= 10
-100 <= arr[i] <= 100
'''

# Code:

def runner_up(arr):
    return sorted(set(arr))[-2]

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    print(runner_up(arr))