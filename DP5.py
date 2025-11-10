def create_node(roll, name, marks):  
    return {"roll": roll, "name": name, "marks": marks, "next": None}
def add_student(head):  
    roll = int(input("Enter Roll No: "))   
    name = input("Enter Name: ")          
    marks = float(input("Enter Marks: ")) 

    
    new_node = create_node(roll, name, marks)

    
    if head is None:
        head = new_node
    else:
        
        temp = head
        while temp["next"] is not None:  
            temp = temp["next"]
        temp["next"] = new_node 

    print("Student added successfully!")
    return head  
    
def delete_student(head):
    if head is None:  
        print("No records found.")
        return head

    roll = int(input("Enter Roll No to delete: "))


    if head["roll"] == roll:
        head = head["next"] 
        print("Record deleted successfully!")
        return head

    # Case 2: Deleting any middle or last node
    prev = None
    temp = head
    while temp and temp["roll"] != roll:
        prev = temp
        temp = temp["next"]

    if temp is None:  
        print("Record not found!")
    else:
        prev["next"] = temp["next"]  
        print("Record deleted successfully!")

    return head  



def update_student(head):
    if head is None:
        print("No records found.")
        return

    roll = int(input("Enter Roll No to update: "))  
    temp = head  
    while temp:
        if temp["roll"] == roll:  
            print("Record found.")
            
            name = input("Enter new name: ")
            marks = float(input("Enter new marks: "))
            
            temp["name"] = name
            temp["marks"] = marks
            print("Record updated successfully!")
            return  
        temp = temp["next"]  

    print("Record not found!")  



def search_student(head):
    if head is None:
        print("No records found.")
        return

    roll = int(input("Enter Roll No to search: "))
    temp = head
    while temp:
        if temp["roll"] == roll:  
            print(f"Record Found → Roll: {temp['roll']}, Name: {temp['name']}, Marks: {temp['marks']}")
            return
        temp = temp["next"]
    print("Record not found!")  



def display_students(head):
    if head is None:
        print("No records to display.")
        return

    print("\nROLL NO\tNAME\tMARKS")  
    temp = head
    while temp:  
        print(f"{temp['roll']}\t{temp['name']}\t{temp['marks']}")  
        temp = temp["next"]  



def sort_students(head):
    
    if head is None or head["next"] is None:
        print("Not enough records to sort.")
        return head

    print("1. Sort by Roll Number")
    print("2. Sort by Marks")
    choice = input("Enter choice: ")  
    order = input("Ascending (A) or Descending (D): ").upper()

    swapped = True  
    
    while swapped:
        swapped = False
        temp = head
        while temp["next"]: 
            swap = False
            
            if choice == "1":  
                if (order == "A" and temp["roll"] > temp["next"]["roll"]) or \
                   (order == "D" and temp["roll"] < temp["next"]["roll"]):
                    swap = True
            elif choice == "2":  
                if (order == "A" and temp["marks"] > temp["next"]["marks"]) or \
                   (order == "D" and temp["marks"] < temp["next"]["marks"]):
                    swap = True

            
            if swap:
                temp["roll"], temp["next"]["roll"] = temp["next"]["roll"], temp["roll"]
                temp["name"], temp["next"]["name"] = temp["next"]["name"], temp["name"]
                temp["marks"], temp["next"]["marks"] = temp["next"]["marks"], temp["marks"]
                swapped = True  

            temp = temp["next"]

    print("Records sorted successfully!")
    return head


# ---------------- MAIN
head = None  


while True:
    
    print("\n--- STUDENT RECORD MANAGEMENT (LINKED LIST) ---")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Display All Students")
    print("6. Sort Students")
    print("7. Exit")

    ch = input("Enter your choice: ")

    
    if ch == '1':
        head = add_student(head)       
    elif ch == '2':
        head = delete_student(head)   
    elif ch == '3':
        update_student(head)           
    elif ch == '4':
        search_student(head)           
    elif ch == '5':
        display_students(head)         
    elif ch == '6':
        head = sort_students(head)     
    elif ch == '7':
        print("Exiting program...")
        break                          
    else:
        print("Invalid choice!")      


