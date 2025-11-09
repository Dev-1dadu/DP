


undo_stack = []
redo_stack = []


def make_change():
    change = input("Enter your text change: ")
    undo_stack.append(change)   
    redo_stack.clear()          
    print(f"Change '{change}' added successfully!")


def undo_action():
    if not undo_stack:
        print("Nothing to undo!")
    else:
        last_change = undo_stack.pop()  
        redo_stack.append(last_change)  
        print(f"Undo: '{last_change}' reverted.")


def redo_action():
    if not redo_stack:
        print("Nothing to redo!")
    else:
        change = redo_stack.pop()       
        undo_stack.append(change)       
        print(f"Redo: '{change}' re-applied.")


def display_document():
    if not undo_stack:
        print("Document is empty.")
    else:
        print("\nCurrent Document State:")
        for i, change in enumerate(undo_stack, start=1):
            print(f"{i}. {change}")


while True:
    print("\n--- REAL-TIME UNDO/REDO SYSTEM (STACK) ---")
    print("1. Make a Change")
    print("2. Undo Action")
    print("3. Redo Action")
    print("4. Display Document State")
    print("5. Exit")

    ch = input("Enter your choice: ")

    if ch == '1':
        make_change()
    elif ch == '2':
        undo_action()
    elif ch == '3':
        redo_action()
    elif ch == '4':
        display_document()
    elif ch == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")

