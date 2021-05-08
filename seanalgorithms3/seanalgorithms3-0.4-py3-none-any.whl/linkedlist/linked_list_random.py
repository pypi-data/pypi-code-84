'''
A linked list is given such that each node contains an additional random pointer which 
could point to any node in the list or null.

Return a deep copy of the list.

 

Example 1:



Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":
{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points 
to itself.
'''

class ListRandomNode:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next 
        self.random = random 

def copy_random_list(head):
    copies = {None:None}

    current = head
    while current:
        new_node = Node(current.val, None, None)
        copies[current] = new_node 
        current = current.next 
    
    for val in copies:
        if val: copies[val].next = copies[val.next]
        if val: copies[val].random = copies[val.random]

    return copies[head]