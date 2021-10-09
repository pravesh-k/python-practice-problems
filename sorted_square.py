## This problem is from LeetCode numbered #977. Squares of Sorted Array

# Problem Statement: Given an integer array nums sorted in non-decreasing 
# order, return an array of the squares of each number sorted in non-decreasing order.

# Costraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        # # iteraying through each element. squaring it and 
        # # replacing with array's original element
        # for i in range(len(nums)):
            # nums[i] *= nums[i]

        # list comprehension format for above for loop
        nums = [nums[i]*nums[i] for i in range(len(nums))]
  
        return sorted(nums)


# driver code
def main():

    sol = Solution()
    
    nums = [-4,-1,0,3,10]

    print(sol.sortedSquares(nums))


if __name__ == "__main__":
    main()
