def create_node(roll, name, marks):  
    return {"roll": roll, "name": name, "marks": marks, "next": None}
def add_student(head):  
    roll = int(input("Enter Roll No: "))   # Input roll number
    name = input("Enter Name: ")           # Input student name
    marks = float(input("Enter Marks: "))  # Input marks (float allows decimals)

    
    new_node = create_node(roll, name, marks)

    # If the list is empty, the new node becomes the first node (head)
    if head is None:
        head = new_node
    else:
        # Otherwise, traverse till the last node
        temp = head
        while temp["next"] is not None:  # Move until we find last node
            temp = temp["next"]
        temp["next"] = new_node  # Link new node at the end

    print("Student added successfully!")
    return head  # Return updated head of the linked list


# Function to delete a student record using roll number
def delete_student(head):
    if head is None:  # If no data in list
        print("No records found.")
        return head

    roll = int(input("Enter Roll No to delete: "))

    # Case 1: If first node (head) is to be deleted
    if head["roll"] == roll:
        head = head["next"]  # Move head to next node
        print("Record deleted successfully!")
        return head

    # Case 2: Deleting any middle or last node
    prev = None
    temp = head
    while temp and temp["roll"] != roll:
        prev = temp
        temp = temp["next"]

    if temp is None:  # If record not found
        print("Record not found!")
    else:
        prev["next"] = temp["next"]  # Bypass (unlink) the node to delete it
        print("Record deleted successfully!")

    return head  # Return updated linked list


# Function to update an existing student record
def update_student(head):
    if head is None:
        print("No records found.")
        return

    roll = int(input("Enter Roll No to update: "))  # Roll number to find
    temp = head  # Start from first node
    while temp:
        if temp["roll"] == roll:  # If roll matches
            print("Record found.")
            # Take new data
            name = input("Enter new name: ")
            marks = float(input("Enter new marks: "))
            # Update dictionary values
            temp["name"] = name
            temp["marks"] = marks
            print("Record updated successfully!")
            return  # Exit after updating
        temp = temp["next"]  # Move to next node if not found yet

    print("Record not found!")  # If roll not found


# Function to search for a student using roll number
def search_student(head):
    if head is None:
        print("No records found.")
        return

    roll = int(input("Enter Roll No to search: "))
    temp = head
    while temp:
        if temp["roll"] == roll:  # Match found
            print(f"Record Found → Roll: {temp['roll']}, Name: {temp['name']}, Marks: {temp['marks']}")
            return
        temp = temp["next"]  # Move to next node
    print("Record not found!")  # If end reached without finding


# Function to display all student records
def display_students(head):
    if head is None:
        print("No records to display.")
        return

    print("\nROLL NO\tNAME\tMARKS")  # Table header
    temp = head
    while temp:  # Traverse until end
        print(f"{temp['roll']}\t{temp['name']}\t{temp['marks']}")  
        temp = temp["next"]  # Move to next node


# Function to sort student records
def sort_students(head):
    # If 0 or 1 record → no need to sort
    if head is None or head["next"] is None:
        print("Not enough records to sort.")
        return head

    print("1. Sort by Roll Number")
    print("2. Sort by Marks")
    choice = input("Enter choice: ")  # Choose sorting field
    order = input("Ascending (A) or Descending (D): ").upper()

    swapped = True  # Flag for checking if swapping happened
    # Using Bubble Sort on linked list
    while swapped:
        swapped = False
        temp = head
        while temp["next"]:  # Traverse nodes
            swap = False
            # Sorting condition based on user choice and order
            if choice == "1":  # Sort by Roll No
                if (order == "A" and temp["roll"] > temp["next"]["roll"]) or \
                   (order == "D" and temp["roll"] < temp["next"]["roll"]):
                    swap = True
            elif choice == "2":  # Sort by Marks
                if (order == "A" and temp["marks"] > temp["next"]["marks"]) or \
                   (order == "D" and temp["marks"] < temp["next"]["marks"]):
                    swap = True

            # If swapping needed, exchange values between two nodes
            if swap:
                temp["roll"], temp["next"]["roll"] = temp["next"]["roll"], temp["roll"]
                temp["name"], temp["next"]["name"] = temp["next"]["name"], temp["name"]
                temp["marks"], temp["next"]["marks"] = temp["next"]["marks"], temp["marks"]
                swapped = True  # Set flag true → another pass required

            temp = temp["next"]

    print("Records sorted successfully!")
    return head


# ---------------- MAIN PROGRAM ----------------
head = None  # Initially, linked list is empty

# Infinite loop for menu-driven program
while True:
    # Menu display
    print("\n--- STUDENT RECORD MANAGEMENT (LINKED LIST) ---")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Display All Students")
    print("6. Sort Students")
    print("7. Exit")

    ch = input("Enter your choice: ")

    # Match choice and call respective function
    if ch == '1':
        head = add_student(head)       # Add new record
    elif ch == '2':
        head = delete_student(head)    # Delete record
    elif ch == '3':
        update_student(head)           # Update record
    elif ch == '4':
        search_student(head)           # Search record
    elif ch == '5':
        display_students(head)         # Display all
    elif ch == '6':
        head = sort_students(head)     # Sort list
    elif ch == '7':
        print("Exiting program...")
        break                          # Exit loop and program
    else:
        print("Invalid choice!")       # Wrong input handling
