# Intuition
# <!-- Describe your first thoughts / brute force way on how to solve this problem. -->
# Could use a for loop for range(len(nums) * 2 )
# and loop through and when we cross original len we subtract one.
#
# Final Approach
# <!-- Describe your approach to solving the problem. -->

# Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->


# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n) #preallocate so we can use i to index values
        for i, num in enumerate(nums):
            ans[i] = ans[i + n] = num
        return ans
