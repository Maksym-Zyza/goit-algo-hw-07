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


def find_min(root):
    if root is None:
        return None
    current = root
    while current.left:
        current = current.left
    return current.val


# Test
root = Node(51)
root = insert(root, 33)
root = insert(root, 24)
root = insert(root, 42)
root = insert(root, 57)
root = insert(root, 16)
root = insert(root, 48)


min_val = find_min(root)
if min_val is not None:
    print(f"Minimum value in the tree: {min_val}")
else:
    print("The tree is empty")