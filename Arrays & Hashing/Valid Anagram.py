# Intuition
# <!-- Describe your first thoughts / brute force way on how to solve this problem. -->
#  Using an dict to store key / value pairs and keeping count of items
#  if counts match then we can assume its an anagram
# 
# Final Approach
# <!-- Describe your approach to solving the problem. -->

# Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->
# O(m + n)

# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->
# O(26) => o(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len not same we can assume theyre not anagrams
        if len(s) != len(t): return False

        sCounter = {}
        tCounter = {}

        for i in range(len(s)):
            sCounter[s[i]] = sCounter.get(s[i], 0 ) + 1
            tCounter[t[i]] = tCounter.get(t[i], 0 ) + 1
        
        return sCounter == tCounter