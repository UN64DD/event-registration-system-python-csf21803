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
            "registered": 0
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

