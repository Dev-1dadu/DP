


event_queue = []


def add_event():
    event = input("Enter event name: ")
    event_queue.append(event)  
    print(f"Event '{event}' added successfully!")


def process_event():
    if not event_queue:  
        print("No events to process!")
    else:
        event = event_queue.pop(0)  
        print(f"Processing event: {event}")


def display_events():
    if not event_queue:
        print("No pending events.")
    else:
        print("\nPending Events:")
        for i, e in enumerate(event_queue, start=1):
            print(f"{i}. {e}")


def cancel_event():
    if not event_queue:
        print("No events to cancel.")
        return
    event = input("Enter event name to cancel: ")
    if event in event_queue:
        event_queue.remove(event)  
        print(f"Event '{event}' canceled successfully!")
    else:
        print("Event not found in queue!")


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

