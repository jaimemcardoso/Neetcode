# Intuition
# <!-- Describe your first thoughts / brute force way on how to solve this problem. -->
# Create a set and if we see the item again return False
#   then true outside loop
# Final Approach
# <!-- Describe your approach to solving the problem. -->
# Create a set based on items and check it against original length
#
# Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->
# O(N)

# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->
# O(N)

def all_unique(items):
  unique_items = set(items)
  return len(unique_items) == len(items)