#!/usr/bin/env python3
# Day 02

def main():
    # List of all USA states
    usa_states = [
        "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
        "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky",
        "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
        "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",
        "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
        "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
        "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
    ]

    visited_states = []

    # Ask user for each state
    for state in usa_states:
        while True:
            user_input = input(f"Have you visited {state}? (y/n): ").strip().lower()
            if user_input in ('y', 'n'):
                if user_input == 'y':
                    visited_states.append(state)
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    # Calculate total number of states visited
    total_states_visited = len(visited_states)
    total_states = len(usa_states)

    # Calculate percentage of states visited
    percentage_visited = (total_states_visited / total_states) * 100

    print(f"\nTotal states visited: {total_states_visited}/{total_states}")
    print(f"Percentage of states visited: {percentage_visited:.2f}%")

if __name__ == "__main__":
    main()

