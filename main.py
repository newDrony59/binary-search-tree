'''
the Question: 
Binary Search Tree is a node-based binary tree data structure which has the following properties:

    The left subtree of a node contains only nodes with keys lesser than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node’s key.
    The left and right subtree each must also be a binary search tree.

Create a class that converts the number into a node in the tree (every node should have left child,
 right child and the value of the node "child can be none"). 
The class should have a function that inserts a new node to the binary tree. And another function 
that prints the final binary tree (tree should be printed from left to the write {left-root-right})

Examples: 
          10                                                           15
       5     11 ➞ [3, 5, 6, 10, 11]                               7          18        ➞  [5, 9, 7, 15, 17, 18, 19]
   3     6                                                     5     9     17     19

root()=Node(10) -> 10 is the root of the tree (first node in the top)
root.insert(5)
root.insert(11)
root.insert(3)
root.insert(6)
root.PrintTree() -> [3, 5, 6, 10, 11]
root.data -> 10
root.left.data -> 5
root.right.data -> 11

'''

class Node:
    tree=[]
# crate node for number every nood have left childe and right chile and data
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
        Node.tree.clear()

    def insert(self, data):
# Compare the new value with the parent node

        if self.data:
            # check for the new value if it bigger than the root if it true then check if the root have a left chiled
            # if not have make this data a new node as aleft node for the root and this node have a left and right
            # if the root already have aleft so it recall the func insert but this time to left node to cheack agine
            # if the new inert data is smaller than that nood or not and the same for the right
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        # cheak the object left childe if it has left  child recall the func to cheak again if it have left etc...
        # if it not have  it print the data of that node
        if self.left:
            self.left.PrintTree()
        Node.tree.append(self.data)
        if self.right:
            self.right.PrintTree()
        return Node.tree

