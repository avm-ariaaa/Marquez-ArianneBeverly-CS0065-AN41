# Task 3

print('\nProgrammed by: Arianne Beverly V. Marquez\n')

# TASK 1: THE ENVIRONMENT

class VacuumEnvironment:
    def __init__(self):
        # Initialize two rooms using a Python dictionary.
        # By default, both are clean, but user input will overwrite this.
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



# TASK 2: THE RULE-BASED AGENT

class VacuumAgent:
    def __init__(self, environment):
        # Pass the environment to the agent so it can interact with the rooms
        self.env = environment
        # The agent defaults to starting in room A.
        self.current_room = 'A'

    def move(self):
        # Implement a move method to switch rooms.
        self.current_room = 'B' if self.current_room == 'A' else 'A'
        # Print the action taken for Task 3 output
        print(f"Action taken: Moved to room {self.current_room}")

    def perceive_and_act(self):
        # Implement the perceive-and-act method.
        # Rule 1: If the current room is dirty, clean it.
        if self.env.is_dirty(self.current_room):
            self.env.clean_room(self.current_room)
            # Print the action taken for Task 3 output
            print("Action taken: Cleaned the room.")
        # Rule 2: If the current room is clean, move to the other room.
        else:
            self.move()



# TASK 3: RUN THE SIMULATION

if __name__ == "__main__":
    while True:
        # Create a fresh environment and agent for each run
        env = VacuumEnvironment()
        agent = VacuumAgent(env)
        
        # Prompt user for initial room states
        env.set_initial_states()
        print() 
        
        # Ask the user how many steps the simulation should run.
        try:
            steps = int(input("How many steps should the agent run? "))
        except ValueError:
            print("Invalid input. Defaulting to 5 steps.")
            steps = 5

        # Run the agent in a loop for the specified steps.
        for step in range(1, steps + 1):
            print(f"\n--- Step {step} ---")
            
            # 1. Print the agent's current location
            print(f"Agent's current location: Room {agent.current_room}")
            
            # 2. Print the action taken (handled inside perceive_and_act and move methods)
            agent.perceive_and_act()
            
            # 3. Print the current state of the environment
            print(f"Current state of the environment: {env.rooms}")

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