# Intuition
# <!-- Describe your first thoughts / brute force way on how to solve this problem. -->
#   I will have a object with the divisor thats needed and the index {d: i} while looping through
#   if we have seen it then I can return tuple (i, key)
# Final Approach
# <!-- Describe your approach to solving the problem. -->
#
#
# Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->
# O(N)

# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->
# O(N)

def pair_product(numbers, target_product):
  pass # todo
  compliment = {}
  for i in range(len(numbers)):
    target = target_product / numbers[i]
    if target in compliment:
        return (compliment[target], i)
    else:
        compliment[numbers[i]] = i
