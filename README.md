# Event Registration System (CLI)

**Course:** CSF21803 – Software Development Fundamental  
**Semester:** I Session 2026/2027  
**Deliverable:** Item #11 – Python CLI Event Registration System

---

## 1. Project Overview & Purpose

A small, menu-driven command-line application for managing event registrations. It allows a user to create events, register attendees, cancel registrations, and view event/registration reports. The entire application is contained in a single Python file and stores all data in memory for the length of one run.

---

## 2. Features Implemented

The CLI menu (`main_menu`) exposes seven options:

| Option | Function | Behavior |
| --- | --- | --- |
| `1. Create Event` | `create_event()` | Prompts for Event ID (non-empty, must be unique), Event Title, Event Date (`YYYY-MM-DD`), Event Capacity (positive integer), and Event Fee (non-negative float). New events start with `registered = 0` and are appended to `events`. |
| `2. View Events` | `view_events()` | Lists every event's ID, title, date, capacity, registered count, and fee. Prints `No events available.` when the list is empty. |
| `3. Register Attendee` | `register_attendee()` | Displays events, asks for an Event ID, rejects unknown IDs and full events, then asks for a non-empty attendee name and email. Creates a registration with a sequential number and increments the event's registered count. |
| `4. View Registrations` | `view_registrations()` | Lists registration number, event title (looked up by event ID), attendee name, and email. Prints `No registrations found.` when empty. |
| `5. Cancel Registration` | `cancel_registration()` | Asks for a positive registration number, removes the matching registration, and decrements that event's registered count. |
| `6. View Summary Report` | `view_summary_report()` | Lists each event with ID, title, date, capacity, registered count, available slots (`capacity - registered`), and fee. |
| `7. Exit` | — | Prints `Exiting the system. Goodbye!` and ends the loop. |

Supporting functions:

- `get_non_empty_input()` – re-prompts until input is not blank.
- `get_positive_integer_input()` – re-prompts until input is an integer greater than zero.
- `get_non_negative_float()` – re-prompts until input is a number greater than or equal to zero.
- `find_event_by_id()` / `find_registration_by_number()` – linear lookups used by the above features.
- `get_positive_int()` – defined but **not used** by any menu option.

Two events are seeded at startup: `EVT001` (Python & Git Workshop, 2026-12-10, capacity 50, fee 100.00) and `EVT002` (Data Science Seminar, 2026-12-15, capacity 100, fee 150.00).

---

## 3. Project Structure

```
.
├── README.md              # This file
└── event_registration.py  # Entire CLI application
```

`event_registration.py` defines three module-level variables: `events` (list of event dictionaries), `registrations` (list of registration dictionaries), and `next_registration_num` (starting at 1). Execution begins at `main()` via the `if __name__ == "__main__"` guard.

---

## 4. Prerequisites & How to Run

**Prerequisites:** Python 3. No third-party packages, requirements file, or setup script are present; only the standard library is needed.

From the repository root:

```bash
python3 event_registration.py
```

Interactive flow:

1. `Welcome to the Event Registration System!` is printed.
2. The seven-option menu is shown.
3. Enter a choice from `1` to `7` at `Enter your choice (1-7):`; anything else prints `Invalid choice. Please try again.`
4. Follow the prompts for the chosen option. Input validation loops until a valid value is entered.
5. The menu returns after each option. Choose `7` to exit.

---

## 5. Testing & Sample Usage

There is no automated test suite, test directory, or test framework configuration in this repository. Verification is manual through the interactive CLI.

Sample session:

```text
Welcome to the Event Registration System!

Event Registration System
1. Create Event
2. View Events
3. Register Attendee
4. View Registrations
5. Cancel Registration
6. View Summary Report
7. Exit
Enter your choice (1-7): 2

Available Events:
ID: EVT001, Title: Python & Git Workshop, Date: 2026-12-10, Capacity: 50, Registered: 0, Fee: $100.00
ID: EVT002, Title: Data Science Seminar, Date: 2026-12-15, Capacity: 100, Registered: 0, Fee: $150.00

Event Registration System
...
Enter your choice (1-7): 3

Available Events:
ID: EVT001, Title: Python & Git Workshop, Date: 2026-12-10, Capacity: 50, Registered: 0, Fee: $100.00
ID: EVT002, Title: Data Science Seminar, Date: 2026-12-15, Capacity: 100, Registered: 0, Fee: $150.00
Enter Event ID to register: EVT001
Enter Attendee Name: Alice Tan
Enter Attendee Email: alice@example.com
Registration successful! Registration Number: 1

Event Registration System
...
Enter your choice (1-7): 6

Summary Report:
Event ID: EVT001, Title: Python & Git Workshop, Date: 2026-12-10, Capacity: 50, Registered: 1, Available Slots: 49, Fee: $100.00
Event ID: EVT002, Title: Data Science Seminar, Date: 2026-12-15, Capacity: 100, Registered: 0, Available Slots: 100, Fee: $150.00

Event Registration System
...
Enter your choice (1-7): 5
Enter Registration Number to cancel: 1
Registration Number 1 has been canceled successfully.

Event Registration System
...
Enter your choice (1-7): 7
Exiting the system. Goodbye!
```

Creating an event uses this prompt sequence:

```text
Enter Event ID: EVT003
Enter Event Title: Git Basics
Enter Event Date (YYYY-MM-DD): 2026-12-20
Enter Event Capacity: 30
Enter Event Fee: 0
Event 'Git Basics' created successfully.
```

---

## 6. Limitations & Course Context

**Current limitations:**

- Data is stored only in Python lists; nothing is written to disk, so all events and registrations are lost when the program exits.
- No persistence layer, database, user accounts, or access control.
- The date is only prompted in `YYYY-MM-DD` format; it is not validated. Email is only checked for being non-empty, not for format.
- The fee field is stored and displayed but there is no payment processing.
- No edit/update operations for events or attendees, no search or filtering, and no command-line arguments.
- No automated tests.
- `get_positive_int()` is dead code, and its `min_value` parameter is ignored.

**Course context:** This repository is the group project deliverable for Item #11 in CSF21803 (Software Development Fundamental), Semester I Session 2026/2027. The repository currently contains only the single CLI source file and this README; no separate design document, report, or test suite is included.
