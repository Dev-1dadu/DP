SIZE = 10
hash_table = [[] for _ in range(SIZE)]  
def hash_function(key):
    return key % SIZE
def insert(key, value):
    index = hash_function(key)
    
    for pair in hash_table[index]:
        if pair[0] == key:
            pair[1] = value
            print("Key already exists. Value updated.")
            return
    
    hash_table[index].append([key, value])
    print("Inserted successfully.")

def search(key):
    index = hash_function(key)
    for pair in hash_table[index]:
        if pair[0] == key:
            print(f"Key found! Value = {pair[1]}")
            return
    print("Key not found!")


def delete(key):
    index = hash_function(key)
    for pair in hash_table[index]:
        if pair[0] == key:
            hash_table[index].remove(pair)
            print("Key deleted successfully.")
            return
    print("Key not found!")

# Display hash table
def display():
    print("\nHash Table:")
    for i in range(SIZE):
        print(f"Index {i}: {hash_table[i]}")

# ---------------- MAIN PROGRAM ----------------
while True:
    print("\n--- HASH TABLE MENU ---")
    print("1. Insert key-value pair")
    print("2. Search key")
    print("3. Delete key")
    print("4. Display hash table")
    print("5. Exit")
    ch = input("Enter choice: ")

    if ch == '1':
        key = int(input("Enter key (integer): "))
        value = input("Enter value: ")
        insert(key, value)
    elif ch == '2':
        key = int(input("Enter key to search: "))
        search(key)
    elif ch == '3':
        key = int(input("Enter key to delete: "))
        delete(key)
    elif ch == '4':
        display()
    elif ch == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")