# Intuition
# <!-- Describe your first thoughts / brute force way on how to solve this problem. -->

# Final Approach
# <!-- Describe your approach to solving the problem. -->
# use a dictionary to maintain items seen, and if an item has been seeen then return true else false
# Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->
# O(N)

# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->
# O(n) since we need a set 


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = set()

        for num in nums:
            if num in count:
                return True
            else:
                count.add(num)
        return False
