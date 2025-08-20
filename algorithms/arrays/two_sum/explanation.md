# Explanation

Use a hash map to store previously seen numbers and their indices. 
For each number, check if `target - num` exists in the map. If it does, you've found the pair.

**Complexity:** O(n) time and O(n) space.
