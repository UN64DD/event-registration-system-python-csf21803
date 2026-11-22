"""
Event Registration System (CLI)
Course: CSF21803 - Software Development Fundamental
"""

events = [
    {
            "id": "EVT001",
            "title": "Python & Git Workshop",
            "date": "2026-12-10",
            "capacity": 50,
            "registered": 0,
            "fee": 100.00,
    },
    {
            "id": "EVT002",
            "title": "Data Science Seminar",
            "date": "2026-12-15",
            "capacity": 100,
            "registered": 0,
            "fee": 150.00,
    },
]

registrations = []
next_registration_num = 1

def get_non_empty_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        else:
            print("Input cannot be empty. Please try again.")

def get_positive_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_positive_int(prompt, min_value=1):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_non_negative_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def find_event_by_id(event_id):
    for event in events:
        if event["id"] == event_id:
            return event
    return None

def find_registration_by_number(registration_num):
    for registration in registrations:
        if registration["registration_num"] == registration_num:
            return registration
    return None

def create_event():
    event_id = get_non_empty_input("Enter Event ID: ")
    if find_event_by_id(event_id):
        print("Event ID already exists. Please try again.")
        return

    title = get_non_empty_input("Enter Event Title: ")
    date = get_non_empty_input("Enter Event Date (YYYY-MM-DD): ")
    capacity = get_positive_integer_input("Enter Event Capacity: ")
    fee = get_non_negative_float("Enter Event Fee: ")

    new_event = {
        "id": event_id,
        "title": title,
        "date": date,
        "capacity": capacity,
        "registered": 0,
        "fee": fee,
    }
    events.append(new_event)
    print(f"Event '{title}' created successfully.")

def view_events():
    if not events:
        print("No events available.")
        return

    print("\nAvailable Events:")
    for event in events:
        print(f"ID: {event['id']}, Title: {event['title']}, Date: {event['date']}, "
              f"Capacity: {event['capacity']}, Registered: {event['registered']}, Fee: ${event['fee']:.2f}")

def register_attendee():
    global next_registration_num

    if not events:
        print("No events available for registration.")
        return

    view_events()
    event_id = get_non_empty_input("Enter Event ID to register: ")
    event = find_event_by_id(event_id)

    if not event:
        print("Event not found. Please try again.")
        return

    if event["registered"] >= event["capacity"]:
        print("Event is full. Cannot register more attendees.")
        return

    attendee_name = get_non_empty_input("Enter Attendee Name: ")
    attendee_email = get_non_empty_input("Enter Attendee Email: ")

    registration = {
        "registration_num": next_registration_num,
        "event_id": event_id,
        "attendee_name": attendee_name,
        "attendee_email": attendee_email,
    }
    registrations.append(registration)
    event["registered"] += 1
    print(f"Registration successful! Registration Number: {next_registration_num}")
    next_registration_num += 1

def view_registrations():
    if not registrations:
        print("No registrations found.")
        return

    print("\nRegistrations:")
    for registration in registrations:
        event = find_event_by_id(registration["event_id"])
        print(f"Registration Number: {registration['registration_num']}, "
              f"Event: {event['title']}, Attendee: {registration['attendee_name']}, "
              f"Email: {registration['attendee_email']}")

def cancel_registration():
    if not registrations:
        print("No registrations found.")
        return

    registration_num = get_positive_integer_input("Enter Registration Number to cancel: ")
    registration = find_registration_by_number(registration_num)

    if not registration:
        print("Registration not found. Please try again.")
        return

    event = find_event_by_id(registration["event_id"])
    event["registered"] -= 1
    registrations.remove(registration)
    print(f"Registration Number {registration_num} has been canceled successfully.")

def view_summary_report():
    print("\nSummary Report:")
    for event in events:
        print(f"Event ID: {event['id']}, Title: {event['title']}, Date: {event['date']}, "
              f"Capacity: {event['capacity']}, Registered: {event['registered']}, "
              f"Available Slots: {event['capacity'] - event['registered']}, Fee: ${event['fee']:.2f}")

def main_menu():
    while True:
        print("\nEvent Registration System")
        print("1. Create Event")
        print("2. View Events")
        print("3. Register Attendee")
        print("4. View Registrations")
        print("5. Cancel Registration")
        print("6. View Summary Report")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            create_event()
        elif choice == '2':
            view_events()
        elif choice == '3':
            register_attendee()
        elif choice == '4':
            view_registrations()
        elif choice == '5':
            cancel_registration()
        elif choice == '6':
            view_summary_report()
        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    print("Welcome to the Event Registration System!")
    main_menu()

if __name__ == "__main__":
    main()