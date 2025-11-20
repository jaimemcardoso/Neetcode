# Intuition
# <!-- Describe your first thoughts / brute force way on how to solve this problem. -->
# We will need 2 counters for both a / b char frequencies
# We can then loop through one and check if the other counter has it and if it does append min(val1, val2) times to a result
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
#

from collections import Counter

def intersection_with_dupes(a, b):
  pass # todo
  aCounter = {}
  bCounter = {}
  res = []
  for i in range(len(a)):
    aCounter[a[i]] = aCounter.get(a[i], 0 ) + 1

  for i in range(len(b)):
    bCounter[b[i]] = bCounter.get(b[i], 0 ) + 1
  
  for key in aCounter:
    if key in bCounter:
      minEntries = min(bCounter[key], aCounter[key])
      for i in range(minEntries):
        res.append(key)
  return res


  ##### Alternative with Counter Import
def intersection_with_dupes(a, b):
  count_a = Counter(a)
  count_b = Counter(b)
  res = []

  for key in count_a:
    if key in count_b:
      minEntries = min(count_b[key], count_a[key])
      for i in range(minEntries):
        res.append(key)
  return res
