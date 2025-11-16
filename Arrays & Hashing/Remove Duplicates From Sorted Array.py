# Intuition
# <!-- Describe your first thoughts on how to solve this problem. -->
# First have a set that you can add numbers to, if the number is in the set remove it from array if not continue

# Approach
# <!-- Describe your approach to solving the problem. -->
# using a set keep track of the unique values while going
# through the list of nums while l != len of nums

# when we find a number that is unique we set it to nums[l] 
# and move r up one value until

# Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->
# O(N)
# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->
# O(n)s


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        items = set()
        l = r = 0

        while r != len(nums):
            if nums[r] in items:
                r += 1
            else:
                items.add(nums[r])
                nums[l] = nums[r]
                r += 1
                l += 1
        return len(items)

                