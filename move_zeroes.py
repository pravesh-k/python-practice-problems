## This problem is from LeetCode numbered #283. Move Zeroes

# Problem Statement: Given an integer array nums, move all 0's to the 
# end of it while maintaining the relative order of the non-zero elements.

# Costraints:
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        count_zeroes = nums.count(0)

        # iterate over the list and till not all zeroes are moved
        while i < len(nums) and j < count_zeroes:
            if nums[i] == 0:                    # pop the element if it is 0 and 
                nums.append(nums.pop(i))        # append at last position in array
                j += 1                          # count the number of zeroes moved
            else:
                i += 1
        
        return nums


# driver code
def main():

    sol = Solution()
    nums = [0]

    print(sol.moveZeroes(nums))


if __name__ == "__main__":
    main()
