# This is a quite complicated problem
# Creating a d = {key: (priority, value)} won't work for several reasons.
# We can use a dictionary to retrive data ina faster way : ( key value couple).
# Using a priority would imply retrive the minimum in O(n) time
# sorting the dictionary would require O(nlogn)
# To evict the least recently used item we would find a minimum priority.

# What is a data structure that can be used to moved numbers and queues 
# in a fast way an in  TC : O(1).
# Which data structure allow fast and several changes in numbers order without
# falling in the O(n) trap?
# LINKED LIST

# The mental model is : Hashmap + Linked List
# get (key) --> fast data fetching = Dictionary ( Hashmap )
# put(key,value) --> Add or update node
# move node to head
# if over capacity : remove tail 

# We know we must use linked lists and hashmaps
# How can I reorder elements such that the TC is O(1) ?

# Now using a singly linked list is slower, think about it.
# If you want to access a certain key you have to traverse the entire list : O(n)
# but a node in the linked list can be accessed  with a pointer : O(1)
# What if i want to fetch index 1 --> get(1). 
# Fetch it with a dict
# We can keep two markers, like head and tail.
# When you use something--> put head in its pointer
# Keep track of the capacity
# You never scan or search.
# 

# Now the hash map gives you instant access to the node object, not just its value.
# That node object gives you instant control over where it sits in the linked list.
# This is the fundamental trick:
# Use the hash map for where it is
# Use the linked list for what order it’s in

# OrderedDict is from Python’s collections module.
# It behaves like a normal dictionary but remembers the insertion order of keys.

# moving elements to the end or beginning (move_to_end) is O(1)
# popping elements from either side (popitem(last=False)) is O(1)
# end = Most recently used

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity
        
    def get(self, key: int) -> int:
        if key not in self.cache :
            return -1
        else :
            self.cache.move_to_end(key)
            return self.cache[key]    
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache :
            self.cache.move_to_end(key)

        self.cache[key] = value

        if len(self.cache) > self.cap :
            self.cache.popitem(last=False)        

        
