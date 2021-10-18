## This problem is from LeetCode numbered #167. Two Sum II - Input array is sorted

# Problem Statement: Given a 1-indexed array of integers numbers that is already sorted 
# in non-decreasing order, find two numbers such that they add up to a specific target
# number. Let these two numbers be numbers[index1] and numbers[index2] 
# where 1 <= first < second <= numbers.length. Return the indices of the two numbers, 
# index1 and index2, as an integer array [index1, index2] of length 2.

# Costraints:
# 2 <= numbers.length <= 3 * 104
# -1000 <= numbers[i] <= 1000
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers)-1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1


# driver code
def main():

    sol = Solution()
    nums = [5,25,75]
    target = 100

    print(sol.twoSum(nums, target))


if __name__ == "__main__":
    main()
