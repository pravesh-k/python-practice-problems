## This problem is from LeetCode numbered #3. Longest Substring Without Repeating Characters

# Problem Statement: Given a string s, find the length of the longest 
# substring without repeating characters.

# Costraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = ''
        l = 0
        
        # for each character in s
        for c in s:

            # check if c is seen, if not then add to seen
            if c not in seen:
                seen += c

            # if c already seen, slice the string at index of seen c and add current c at end
            else:
                l = max(l, len(seen))       # check max length
                seen = seen[seen.index(c)+1:] + c
                
        return max(l, len(seen))
                    

# driver code
def main():

    sol = Solution()
    s = "au"

    print(sol.lengthOfLongestSubstring(s))


if __name__ == "__main__":
    main()
