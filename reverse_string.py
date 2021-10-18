## This problem is from LeetCode numbered #344. Reverse String

# Problem Statement: Write a function that reverses a string. The input string 
# is given as an array of characters s

# Costraints:
# 1 <= s.length <= 105
# s[i] is a printable ascii character.

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]

        print(s)

# driver code
def main():

    sol = Solution()

    s = ["H","a","n","n","a","h"]

    sol.reverseString(s)


if __name__ == "__main__":
    main()
