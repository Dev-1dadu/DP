

# Initialize empty event queue (FIFO)
event_queue = []

# Function to add event
def add_event():
    event = input("Enter event name: ")
    event_queue.append(event)  # Add event to end of queue
    print(f"Event '{event}' added successfully!")

# Function to process next event (dequeue)
def process_event():
    if not event_queue:  # Queue empty check
        print("No events to process!")
    else:
        event = event_queue.pop(0)  # Remove first (oldest) event
        print(f"Processing event: {event}")

# Function to display all pending events
def display_events():
    if not event_queue:
        print("No pending events.")
    else:
        print("\nPending Events:")
        for i, e in enumerate(event_queue, start=1):
            print(f"{i}. {e}")

# Function to cancel a pending event
def cancel_event():
    if not event_queue:
        print("No events to cancel.")
        return
    event = input("Enter event name to cancel: ")
    if event in event_queue:
        event_queue.remove(event)  # Remove that event from queue
        print(f"Event '{event}' canceled successfully!")
    else:
        print("Event not found in queue!")

# ---------------- MAIN MENU ----------------
while True:
    print("\n--- REAL-TIME EVENT PROCESSING SYSTEM ---")
    print("1. Add Event")
    print("2. Process Next Event")
    print("3. Display Pending Events")
    print("4. Cancel an Event")
    print("5. Exit")

    ch = input("Enter your choice: ")

    if ch == '1':
        add_event()
    elif ch == '2':
        process_event()
    elif ch == '3':
        display_events()
    elif ch == '4':
        cancel_event()
    elif ch == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")
