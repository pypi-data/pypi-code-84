'''
We are given a linked list with head as the first node.  Let's number the nodes in the list: node_1, 
node_2, node_3, ... etc.

Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val such that j > i, 
node_j.val > node_i.val, and j is the smallest possible choice.  If such a j does not exist, the next larger 
value is 0.

Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).

Note that in the example inputs (not outputs) below, arrays such as [2,1,5] represent the serialization of a 
linked list with a head node value of 2, second node value of 1, and third node value of 5.

 

Example 1:

Input: [2,1,5]
Output: [5,5,0]
Example 2:

Input: [2,7,4,3,5]
Output: [7,0,5,5,0]
Example 3:

Input: [1,7,5,1,9,2,5,1]
Output: [7,9,9,9,0,5,0,0]
 

Note:

1 <= node.val <= 10^9 for each node in the linked list.
The given list has length in the range [0, 10000].
'''
import itertools

def next_larger_node(head):
    res, stack = [], []
    while head:
        while stack and stack[-1][1] < head.val:
            res[stack.pop()[0]] = head.val 
        stack.append((len(res), head.val))
        res.append(0)
        head = head.next 
    return res 

def next_larger_node_v2(head):
    if not head: return []
    current, count = head, 0
    while current:
        count += 1
        current = current.next
    
    counter = itertools.count()
    stack, result = [(head.val, next(counter))], [None] * count
    head = head.next 

    while head:
        while stack and stack[-1][0] < head.val:
            result[stack[-1][1]] = head.val 
            stack.pop()
        stack.append((head.val, next(counter)))
        head = head.next 

    while stack:
        result[stack[-1][1]] = 0
        stack.pop()

    return result

