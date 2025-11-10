

class Node:
    def __init__(self, city, population):
        self.city = city
        self.population = population
        self.left = None
        self.right = None


def insert(root, city, population):
    if root is None:
        return Node(city, population)
    if city < root.city:
        root.left = insert(root.left, city, population)
    elif city > root.city:
        root.right = insert(root.right, city, population)
    else:
        print("City already exists! Use update option.")
    return root


def delete(root, city):
    if root is None:
        print("City not found!")
        return root
    if city < root.city:
        root.left = delete(root.left, city)
    elif city > root.city:
        root.right = delete(root.right, city)
    else:
        # Node with one or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # Node with two children → find inorder successor
        temp = findMin(root.right)
        root.city, root.population = temp.city, temp.population
        root.right = delete(root.right, temp.city)
    return root

def findMin(node):
    while node.left:
        node = node.left
    return node


def update(root, city, new_pop):
    if root is None:
        print("City not found!")
        return
    if city < root.city:
        update(root.left, city, new_pop)
    elif city > root.city:
        update(root.right, city, new_pop)
    else:
        root.population = new_pop
        print("Population updated successfully!")

# Display cities in ascending order
def inorder(root):
    if root:
        inorder(root.left)
        print(f"{root.city} : {root.population}")
        inorder(root.right)


def descending(root):
    if root:
        descending(root.right)
        print(f"{root.city} : {root.population}")
        descending(root.left)


def search(root, city):
    comparisons = 0
    while root:
        comparisons += 1
        if city == root.city:
            print(f"City found! Population: {root.population}")
            print(f"Comparisons made: {comparisons}")
            return
        elif city < root.city:
            root = root.left
        else:
            root = root.right
    print("City not found!")
    print(f"Comparisons made: {comparisons}")


def max_comparisons(n):
    print(f"Maximum comparisons (worst case) = {n}")

#MAIN PROGRAM
root = None

while True:
    print("\n--- CITY DATABASE (BST) ---")
    print("1. Add new city")
    print("2. Delete city")
    print("3. Update population")
    print("4. Display ascending order")
    print("5. Display descending order")
    print("6. Search city")
    print("7. Maximum comparisons (worst case)")
    print("8. Exit")
    ch = input("Enter choice: ")

    if ch == '1':
        city = input("Enter city name: ")
        pop = int(input("Enter population: "))
        root = insert(root, city, pop)
    elif ch == '2':
        city = input("Enter city name to delete: ")
        root = delete(root, city)
    elif ch == '3':
        city = input("Enter city name to update: ")
        pop = int(input("Enter new population: "))
        update(root, city, pop)
    elif ch == '4':
        print("\nCities in Ascending Order:")
        inorder(root)
    elif ch == '5':
        print("\nCities in Descending Order:")
        descending(root)
    elif ch == '6':
        city = input("Enter city name to search: ")
        search(root, city)
    elif ch == '7':
        n = int(input("Enter total number of cities: "))
        max_comparisons(n)
    elif ch == '8':
        print("Exiting program...")
        break
    else:

        print("Invalid choice!")
