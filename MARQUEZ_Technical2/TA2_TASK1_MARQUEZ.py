print('\nProgrammed by: Arianne Beverly V. Marquez\n')

class VacuumEnvironment:
    def __init__(self):
        # Initialize two rooms using a Python dictionary.
        # By default, both are clean, but user input will overwrite this.
        self.rooms = {'A': 'Clean', 'B': 'Clean'}
        
        # The agent defaults to starting in room A.
        self.current_room = 'A'

    def set_initial_states(self):
        # Allow the user to set the initial state of each room (dirty or clean).
        # .capitalize() ensures the formatting matches the dictionary output (e.g., 'Dirty', 'Clean')
        state_a = input("\nIs room A Dirty or Clean? \n").strip().capitalize()
        state_b = input("\nIs room B Dirty or Clean? \n").strip().capitalize()
        self.rooms['A'] = state_a
        self.rooms['B'] = state_b

    def is_dirty(self, room):
        # Function to check if a room is dirty.
        return self.rooms[room] == 'Dirty'

    def clean_room(self, room):
        # Function to clean a room.
        self.rooms[room] = 'Clean'
        print(f"Room {room} has been cleaned.")

    def run_agent(self, steps):
        # Loop (for loop) to simulate the agent running for the specified number of steps.
        for step in range(1, steps + 1):
            print(f"\nStep {step}: Agent is in room {self.current_room}")

            # If-Else statements to determine the agent's action
            if self.is_dirty(self.current_room):
                self.clean_room(self.current_room)
            else:
                # If the room is already clean, move to the other room
                next_room = 'B' if self.current_room == 'A' else 'A'
                print(f"Moving to room {next_room}")
                self.current_room = next_room

            # Display the exact environment state after the action is taken
            print(f"Environment state: {self.rooms}")

# Main program execution
if __name__ == "__main__":
    while True:
        # Create a fresh environment for each run so the agent resets to Room A
        env = VacuumEnvironment()
        
        # Prompt user for initial room states
        env.set_initial_states()
        print() 
        
        # Ask the user for the number of steps
        try:
            steps = int(input("How many steps should the agent run? "))
        except ValueError:
            print("Invalid input. Defaulting to 5 steps.")
            steps = 5

        # Run the agent through the environment
        env.run_agent(steps)

        print()
        input("Press any key to continue . . . ")
        
        # Ask the user if they want to run it again
        print()
        retry = input("Would you like to run the simulation again? (Type 'yes' to restart, or any other key to exit): ").strip().lower()
        
        if retry not in ['yes', 'y']:
            print("Exiting program. Goodbye!")
            break
        
        # Print a visual separator for the next run
        print("\n" + "="*41 + "\n")