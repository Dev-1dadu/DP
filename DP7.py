# Hash Table using Linear Probing (Non-OOP)
def hash_function(key, size):
    return key % size   

def insert(table, key, size):
    index = hash_function(key, size)
    start_index = index

    while table[index] is not None and table[index] != "DELETED":
        if table[index] == key:
            print(f"Key {key} already exists.")
            return
        index = (index + 1) % size
        if index == start_index:
            print("Hash table is full!")
            return

    table[index] = key
    print(f"Inserted key {key} at index {index}")


def search(table, key, size):
    index = hash_function(key, size)
    start_index = index

    while table[index] is not None:
        if table[index] == key:
            print(f"Key {key} found at index {index}")
            return
        index = (index + 1) % size
        if index == start_index:
            break

    print(f"Key {key} not found.")


def delete(table, key, size):
    index = hash_function(key, size)
    start_index = index

    while table[index] is not None:
        if table[index] == key:
            table[index] = "DELETED"
            print(f"Key {key} deleted from index {index}")
            return
        index = (index + 1) % size
        if index == start_index:
            break

    print(f"Key {key} not found, cannot delete.")


def display(table):
    print("\nHash Table Contents:")
    for i in range(len(table)):
        print(f"Index {i}: {table[i]}")
    print()


# ---------- Main Program ----------
size = int(input("Enter size of hash table: "))
hash_table = [None] * size

while True:
    print("\nMenu:")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter key to insert: "))
        insert(hash_table, key, size)
    elif choice == 2:
        key = int(input("Enter key to search: "))
        search(hash_table, key, size)
    elif choice == 3:
        key = int(input("Enter key to delete: "))
        delete(hash_table, key, size)
    elif choice == 4:
        display(hash_table)
    elif choice == 5:
        print("Exiting program.")
        break
    else:
        print("Invalid choice, try again.")