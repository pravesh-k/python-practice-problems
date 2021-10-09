## This problem is from LeetCode numbered #189. Rotate an array

# Problem Statement: Given an array, rotate the array to the 
# right by k steps, where k is non-negative.

# Costraints:
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # below is a short and simple solution but it is
        # slow because of complexity of background steps

        # for i in range(k):            
            # nums.insert(0, nums.pop())
            
        # below given is another simple yet better 
        # solution for the problem statement

        n = len(nums)
        k = k % n
        kl, lk = nums[n-k:], nums[:n-k]
        lkl = kl + lk

        for i in range(n):
            nums[i] = lkl[i]

        # below given is the simplest and the best performing 
        # solution in terms of speed but memory performace is bad

        # k %= len(nums)
        # nums[k:], nums[:k] = nums[:-k], nums[-k:]

        return nums


# driver code
def main():

    sol = Solution()
    k = 3
    nums = [-4,-1,0,3,10]

    print(sol.rotate(nums, k))


if __name__ == "__main__":
    main()
