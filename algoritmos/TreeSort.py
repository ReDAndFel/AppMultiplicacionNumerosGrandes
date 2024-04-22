class Node:
    def __init__(self, item=0):
        self.key = item
        self.left = None
        self.right = None

root = None

# A recursive function to insert a new key in BST
def insertRec(root, key):
    # If the tree is empty, return a new node
    if root is None:
        return Node(key)

    # Otherwise, recur down the tree
    if key < root.key:
        root.left = insertRec(root.left, key)
    elif key > root.key:
        root.right = insertRec(root.right, key)

    return root

def treeins(arr):
    global root
    root = None
    for i in range(len(arr)):
        root = insertRec(root, arr[i])
    return inorderRec(root)

# A function to do inorder traversal of BST
def inorderRec(root):
    if root:
        inorderRec(root.left)
        inorderRec(root.right)