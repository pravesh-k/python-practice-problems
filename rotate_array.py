from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(k):
            nums.insert(0, nums.pop())

        return nums


# driver code
def main():

    sol = Solution()
    k = 3
    nums = [-4,-1,0,3,10]

    print(sol.rotate(nums, k))


if __name__ == "__main__":
    main()
