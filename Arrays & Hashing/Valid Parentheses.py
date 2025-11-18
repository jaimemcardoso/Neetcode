# Intuition
# <!-- Describe your first thoughts / brute force way on how to solve this problem. -->
# we can use a stack to add the chars in string to it and then pop the last value as we looop through
# the bottom of the string and compare it as a compliment inside a object 


# Final Approach
# <!-- Describe your approach to solving the problem. -->
#
#

# Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->
# O(N)
#
# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->
# O(N)
# The input string s is valid if and only if:

# 1 Every open bracket is closed by the same type of close bracket.
# 2 Open brackets are closed in the correct order.
# 3 Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        compliment = {")": "(", "]": "[", "}": "{"}
        stack = []
        for char in s:
            if char in compliment.values(): # if its opening add to stack
                stack.append(char)
            else: # if stack isnt 
                if not stack or stack[-1] != compliment[char]:
                    return False
                stack.pop()

        return len(stack) == 0

