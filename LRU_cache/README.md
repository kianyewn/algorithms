# Takeaway

## Attempt 1
- For the first attempt, I thought I can use the fact that in python, dictionaries are ordered, and therefore I can del a key value, and then add a key value back to model the recency of key-value pairs used.
- However, it turns out that it does not work, and removal of the least recency key is not in O(1), because i have to convert the dictionary keys into a list, and extract the first element in the list, which corresponds to the least recently used key.


## Attempt 2
- The solution to get O(1) `get` and O(1) `put` is to use a double linked list
- The reason why we can get a O(1) for both `get` and `put` is because:
  - 1. if we want to remove a key, we can just use a hashmap[key, Node] so that look up for the key is in O(1).
  - 2. After looking up the node, we can adjust the node before and after via pointers, Eg, if we want to remove a node, set the node.prev.next = node.next, and node.next.prev = node.prev. This is also O(1)
  - 3. When we update the linkedlist, we always add it to the `head`. i.e, the node next to the `head` is always the most recent, and then node previous to the `tail` is the least recent value.
  - 4. If we want to remove the least recently, we again adjust the pointers in O(1) via tail.prev.prev.next = tail, tail.prev = tail.prev.prev.
### key point:
- One short cut is to actually initialize the double linkedlist with a null `head` and `tail`, so that we do not have to worry about checking for null values to indicate the end of the linkedlist.
- if we want to get and put in O(1), we should use double linked list.