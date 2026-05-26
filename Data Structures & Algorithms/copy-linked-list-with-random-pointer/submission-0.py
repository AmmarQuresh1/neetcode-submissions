"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
"""
Structuring the Recursive Function
With that in mind, here is the complete step-by-step logic for your copy(node) function.

Base Case: If node is null, return null.

Memoization Check: If node is already in your HashMap, return the copied node from the map (map.get(node)).

Create the Copy: If you get past those first two checks, it means you've found a new node that needs to be copied. 
So, create the new node: newNode = new Node(node.val).

Cache the Copy (Crucial Step): Immediately put this new node into your HashMap before doing anything else. 
map.put(node, newNode). 
This is what prevents the infinite loop. 
When the recursion comes back around for this node, it will be found in the map at step 2.

Make the Recursive Calls: Now you set the next and random pointers for your newNode. 
You do this by calling the copy function on the original node's pointers:

newNode.next = copy(node.next);

newNode.random = copy(node.random);

Return the Copy: Finally, return the newNode you created.

"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        copied_nodes = dict()

        def _copy(node: 'Optional[Node]') -> 'Optional[Node]':
            # base case
            if not node:
                return None
            
            if node in copied_nodes.keys():
                return copied_nodes.get(node)
            
            new_node = Node(node.val)

            copied_nodes[node] = new_node

            new_node.next = _copy(node.next) 
            new_node.random = _copy(node.random)
            
            return new_node
        
        return _copy(head)
