## This problem is from LeetCode numbered 557. Reverse Words in a String

# Problem Statement: Given a string s, reverse the order of characters in each 
# word within a sentence while still preserving whitespace and initial word order.

# Costraints:
# 1 <= s.length <= 5 * 104
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.

from typing import List

class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.split()
        for i in range(len(s)):
            s[i] = "".join(reversed(s[i]))
        
        s = " ".join(s)
        print(s)


# driver code
def main():

    sol = Solution()

    s = "Let's take LeetCode contest"

    sol.reverseWords(s)


if __name__ == "__main__":
    main()
