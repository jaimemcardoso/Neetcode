# Intuition
# <!-- Describe your first thoughts / brute force way on how to solve this problem. -->
# we have to loop through it once, while we loop we can set up a obj with a compliment value and key
# while looping we can check if we have encountered the compliment value and return that key and i
# Final Approach
# <!-- Describe your approach to solving the problem. -->
#
#
# Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->
# O(n)

# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->
# O(n)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        
        for i in range(len(nums)):
            c = target - nums[i]
            if c not in comp:
                comp[nums[i]] = i
            else:
                return [comp[c], i]
            