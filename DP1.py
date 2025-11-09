


def linear_search(ids, key):
    for i in range(len(ids)):
        if ids[i] == key:
            return  i
    return -1  



def binary_search(ids, key):
    low = 0
    high = len(ids) - 1

    while low <= high:
        mid = (low + high) // 2

        if ids[mid] == key:
            return mid
        elif ids[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1




n = int(input("Enter number of customer accounts: "))
ids = []

for i in range(n):
    acc = int(input(f"Enter Account ID {i + 1}: "))
    ids.append(acc)

print("\nCustomer Account IDs:", ids)

key = int(input("\nEnter Account ID to search: "))


pos = linear_search(ids, key)
if pos != -1:
    print(f"\n(Linear Search) Account ID {key} found at position {pos + 1}.")
else:
    print(f"\n(Linear Search) Account ID {key} not found.")
    

ids.sort()
print("\nSorted Account IDs for Binary Search:", ids)

pos = binary_search(ids, key)
if pos != -1:
    print(f"(Binary Search) Account ID {key} found at position {pos + 1}.")
else:
    print(f"(Binary Search) Account ID {key} not found.")

