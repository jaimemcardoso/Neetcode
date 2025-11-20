# Intuition
# <!-- Describe your first thoughts / brute force way on how to solve this problem. -->
# Create 2 sets, one for each array
# loop through each one and check if the other set doesn't have items
# OR we could create an object { k : count } and if the count is over 1 remove it from the object and return object.values
#
# Final Approach
# <!-- Describe your approach to solving the problem. -->
#
#
# Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->
#

# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->
#
def exclusive_items(a, b):
    pass # todo
    res = []
    x = set(a)
    y = set(b)

    for letter in x:
        if letter not in y:
            res.append(letter)
    
    for letter in y:
        if letter not in x:
            res.append(letter)

    return res


