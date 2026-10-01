# Optional Task

import random

print('\nProgrammed by: Arianne Beverly V. Marquez\n')

# TASK 1: THE ENVIRONMENT (Updated for Room C)

class VacuumEnvironment:
    def __init__(self):
        # Initialize three rooms using a Python dictionary.
        self.rooms = {'A': 'Clean', 'B': 'Clean', 'C': 'Clean'}

    def set_initial_states(self):
        # Allow the user to set the initial state of each room.
        # Adjusted input prompt to match the inline format of the new screenshot.
        self.rooms['A'] = input("\nIs room A Dirty or Clean? ").strip().capitalize()
        self.rooms['B'] = input("\nIs room B Dirty or Clean? ").strip().capitalize()
        self.rooms['C'] = input("\nIs room C Dirty or Clean? ").strip().capitalize()

    def is_dirty(self, room):
        # Function to check if a room is dirty.
        return self.rooms[room] == 'Dirty'

    def clean_room(self, room):
        # Function to clean a room.
        self.rooms[room] = 'Clean'
        print(f"Room {room} has been cleaned.")



# BONUS TASK: VISUALIZATION HELPER

def display_grid(rooms_dict, current_room):
    # Generates the [A-State] [B-State] [C-State] grid output
    grid = []
    for room in ['A', 'B', 'C']:
        if room == current_room:
            grid.append(f"[{room}-Agent]")
        else:
            grid.append(f"[{room}-{rooms_dict[room]}]")
    print("  ".join(grid))



# TASK 2: THE RULE-BASED AGENT (Updated Logic)

class VacuumAgent:
    def __init__(self, environment):
        self.env = environment
        self.current_room = 'A'

    def perceive_and_act(self):
        # Rule 1: If the current room is dirty, clean it.
        if self.env.is_dirty(self.current_room):
            self.env.clean_room(self.current_room)
        
        # Rule 2: If the current room is clean, find dirty rooms.
        else:
            # Create a list of all rooms that are currently dirty
            dirty_rooms = [room for room, state in self.env.rooms.items() if state == 'Dirty']
            
            if dirty_rooms:
                # Randomly pick a dirty room from the list to move to next
                self.current_room = random.choice(dirty_rooms)
                print(f"Moving to room {self.current_room}")
            else:
                # If the list is empty, all rooms are clean
                print("All rooms are clean. Agent is idle.")



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
            print(f"\nStep {step}:")
            
            # Print the text-based grid before the agent takes action
            display_grid(env.rooms, agent.current_room)
            
            # Agent perceives the room and acts
            agent.perceive_and_act()
            
            # Print the text-based grid after the agent takes action
            display_grid(env.rooms, agent.current_room)

        print()
        input("Press any key to continue . . . ")
        
        # Ask the user if they want to run it again
        print()
        retry = input("Would you like to run the simulation again? (Type 'yes' to restart, or any other key to exit): ").strip().lower()
        
        if retry not in ['yes', 'y']:
                    print("Exiting program. Goodbye!")
                    break