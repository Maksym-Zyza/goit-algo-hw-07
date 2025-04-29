class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def sum_values(root):
    """Recursive Solution for Binary Search Tree"""
    if root is None:
        return 0
    return root.val + sum_values(root.left) + sum_values(root.right)


# Test
root = Node(25)
root = insert(root, 33)
root = insert(root, 24)
root = insert(root, 45)
root = insert(root, 37)
root = insert(root, 26)
root = insert(root, 18)

total_sum = sum_values(root)
print(f"Sum of all node values in the tree: {total_sum}")
