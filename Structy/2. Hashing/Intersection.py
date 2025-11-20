# Intuition
# <!-- Describe your first thoughts / brute force way on how to solve this problem. -->
# take each list and put them into sets then loop through one and check the other

# Final Approach
# <!-- Describe your approach to solving the problem. -->
#
#
# Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->
# O(n + m_)

# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->
# O (m + n)
def intersection(a, b):
  pass # todo
  res = []
  x = set(a)
  y = set(b)

  for num in x:
    if num in y:
        res.append(num)
return num