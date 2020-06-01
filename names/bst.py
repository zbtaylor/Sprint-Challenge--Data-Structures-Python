"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = BSTNode(value)
        root_node = self

        if new_node.value < root_node.value:
            if root_node.left == None:
                root_node.left = new_node
            else:
                root_node.left.insert(new_node.value)
        else:
            if root_node.right == None:
                root_node.right = new_node
            else:
                root_node.right.insert(new_node.value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        root_node = self

        if root_node.value == target:
            return True
        elif target < root_node.value:
            if root_node.left == None:
                return False
            else:
                return root_node.left.contains(target)
        else:
            if root_node.right == None:
                return False
            else:
                return root_node.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        root_node = self
        if root_node.right is not None:
            return root_node.right.get_max()
        else:
            return root_node.value

    # Part 2 -----------------------

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        root_node = self
        fn(root_node.value)
        if root_node.left:
            root_node.left.for_each(fn)
        if root_node.right:
            root_node.right.for_each(fn)

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.left.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # queue
        if self.value == None:
            return
        queue = [self]
        while(len(queue) > 0):
            print(queue[0].value)
            current_node = queue.pop(0)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
