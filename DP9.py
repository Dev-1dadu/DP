#dp9 Binary Search Tree Implementation in Python (Menu-driven)

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# ----------- Insert Node -----------
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

# ----------- Search Node -----------
def search(root, key):
    if root is None:
        return False
    if root.key == key:
        return True
    elif key < root.key:
        return search(root.left, key)
    else:
        return search(root.right, key)

# ----------- Find Minimum Value Node -----------
def find_min(root):
    current = root
    while current.left is not None:
        current = current.left
    return current

# ----------- Delete Node -----------
def delete(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        # Node found
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # Node with two children
        temp = find_min(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root

# ----------- Traversals -----------
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=" ")

# ----------- Main Program -----------
root = None

while True:
    print("\n--- Binary Search Tree Operations ---")
    print("1. Insert Node")
    print("2. Delete Node")
    print("3. Search Node")
    print("4. Display (Inorder, Preorder, Postorder)")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter value to insert: "))
        root = insert(root, key)
        print("Node inserted successfully!")

    elif choice == 2:
        key = int(input("Enter value to delete: "))
        root = delete(root, key)
        print("Node deleted successfully!")

    elif choice == 3:
        key = int(input("Enter value to search: "))
        if search(root, key):
            print("Node found in BST!")
        else:
            print("Node not found!")

    elif choice == 4:
        print("\nInorder Traversal: ", end="")
        inorder(root)
        print("\nPreorder Traversal: ", end="")
        preorder(root)
        print("\nPostorder Traversal: ", end="")
        postorder(root)
        print()

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")

	