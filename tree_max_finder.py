
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


def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


def find_max(root):
    if root is None:
        return None
    current = root
    while current.right:
        current = current.right
    return current.val


# Test
root = Node(5)
root = insert(root, 32)
root = insert(root, 32)
root = insert(root, 41)
root = insert(root, 37)
root = insert(root, 26)
root = insert(root, 20)


max_val = find_max(root)
if max_val is not None:
    print(f"Maximum value in the tree: {max_val}")
else:
    print("The tree is empty")