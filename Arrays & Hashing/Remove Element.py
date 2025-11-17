# Intuition
# <!-- Describe your first thoughts / brute force way on how to solve this problem. -->
# I think this is a 2 pointer problem, we can go through l / r while  r !== len of list
#  then setting left equal to right if its not val
# Final Approach
# <!-- Describe your approach to solving the problem. -->

# Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->
# O(N)

# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->
# O(1)



class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        notEqual = 0 # Keeping track of how many times we haven't seen val
        l = r = 0 # pointers to keep L R posititons so we can replace in place

        while r < len(nums):
            #check if nums[r] = val, if true => r++
            if nums[r] == val:
                r += 1
            else:
                nums[l] = nums[r]
                r += 1
                l += 1
                notEqual += 1
        print(notEqual)
            #else it is not val so we set nums[l] = nums[r] and move L++ R++, add 1 to count