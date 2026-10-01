# Task 2


print('\nProgrammed by: Arianne Beverly V. Marquez\n')

class VacuumEnvironment:
    def __init__(self):
        # Initialize two rooms using a Python dictionary.
        self.rooms = {'A': 'Clean', 'B': 'Clean'}

    def set_initial_states(self):
        # Allow the user to set the initial state of each room (dirty or clean).
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
        # We now create the Agent from Task 2 here to run the loop
        agent = VacuumAgent(self)
        
        # Loop (for loop) to simulate the agent running
        for step in range(1, steps + 1):
            print(f"\nStep {step}: Agent is in room {agent.current_room}")

            # The agent perceives its environment and acts based on its rules
            agent.perceive_and_act()

            # Display the exact environment state after the action is taken
            print(f"Environment state: {self.rooms}")


# ADDED FOR TASK 2: The Agent Class

class VacuumAgent:
    def __init__(self, environment):
        self.env = environment
        self.current_room = 'A'

    def move(self):
        # Implement a move method to switch rooms.
        self.current_room = 'B' if self.current_room == 'A' else 'A'
        print(f"Moving to room {self.current_room}")

    def perceive_and_act(self):
        # Implement the perceive-and-act method.
        # Rule 1: If the current room is dirty, clean it.
        if self.env.is_dirty(self.current_room):
            self.env.clean_room(self.current_room)
        # Rule 2: If the current room is clean, move to the other room.
        else:
            self.move()


# Main program execution (Kept exactly as your Task 1!)
if __name__ == "__main__":
    while True:
        # Create a fresh environment for each run
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