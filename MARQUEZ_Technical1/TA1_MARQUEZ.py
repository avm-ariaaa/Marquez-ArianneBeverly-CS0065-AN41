import agentpy as ap
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

print('\nProgrammed by: Arianne Beverly V. Marquez\n')

class CustomWalker(ap.Agent):
    def setup(self):
        # 1. Track agent paths: Initialize a list to store coordinates
        self.path = []
        
    def step(self):
        # 2. Change movement rules: Introduce a biased behavior preference
        if self.model.p.behavior == 'biased':
            choices = [(1,0), (1,0), (0,1), (0,1), (-1,0), (0,-1)]
        else:
            choices = [(1,0), (-1,0), (0,1), (0,-1)]
            
        direction = random.choice(choices)
        x, y = self.position
        
        x = max(0, min(self.model.p.grid_size[0]-1, x + direction[0]))
        y = max(0, min(self.model.p.grid_size[1]-1, y + direction[1]))
        self.position = (x, y)
        
        # Append current position after moving
        self.path.append(self.position)

class WalkModel(ap.Model):
    def setup(self):
        self.agents = ap.AgentList(self, self.p.agents, CustomWalker)
        for agent in self.agents:
            agent.position = (random.randint(0, self.p.grid_size[0]-1),
                              random.randint(0, self.p.grid_size[1]-1))
            agent.path.append(agent.position) # Store starting point
            
    def step(self):
        self.agents.step()

num_agents = int(input('Enter number of agents: '))
grid_size = int(input('Enter grid size (e.g., 10 for 10x10): '))
num_steps = int(input('Enter number of steps: '))

# 4. Compare scenarios: Define parameters
model1 = WalkModel({'agents': num_agents, 'grid_size': (grid_size, grid_size), 'behavior': 'random'})
model2 = WalkModel({'agents': num_agents, 'grid_size': (grid_size, grid_size), 'behavior': 'biased'})
model1.setup()
model2.setup()

# --- INTERACTIVE ANIMATION ---
fig_anim, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
fig_anim.suptitle('Agent Movement Comparison (Close window when done to see analysis)')

ax1.set_title('Scenario 1: Random Walk')
ax2.set_title('Scenario 2: Biased Walk')

for ax in [ax1, ax2]:
    ax.set_xlim(0, grid_size)
    ax.set_ylim(0, grid_size)
    ax.grid(True)

scat1 = ax1.scatter([], [], s=100, c='blue', zorder=2)
scat2 = ax2.scatter([], [], s=100, c='red', zorder=2)

# Create line objects for the path trails
lines1 = [ax1.plot([], [], alpha=0.3, c='blue', zorder=1)[0] for _ in range(num_agents)]
lines2 = [ax2.plot([], [], alpha=0.3, c='red', zorder=1)[0] for _ in range(num_agents)]

def update(frame):
    model1.step()
    model2.step()
    
    x1 = [a.position[0] for a in model1.agents]
    y1 = [a.position[1] for a in model1.agents]
    scat1.set_offsets(list(zip(x1, y1)))
    
    x2 = [a.position[0] for a in model2.agents]
    y2 = [a.position[1] for a in model2.agents]
    scat2.set_offsets(list(zip(x2, y2)))
    
    # Update trail lines
    for i, agent in enumerate(model1.agents):
        lines1[i].set_data([p[0] for p in agent.path], [p[1] for p in agent.path])
        
    for i, agent in enumerate(model2.agents):
        lines2[i].set_data([p[0] for p in agent.path], [p[1] for p in agent.path])
        
    return [scat1, scat2] + lines1 + lines2

ani = animation.FuncAnimation(fig_anim, update, frames=num_steps, blit=True, repeat=False)
plt.show() 

# --- 3. FINAL POSITION ANALYSIS ---
# This window will pop up automatically after you close the animation window
fig_hist, (ax3, ax4) = plt.subplots(1, 2, figsize=(12, 5))
fig_hist.suptitle('Final Position Analysis')

final_x1 = [a.position[0] for a in model1.agents]
final_y1 = [a.position[1] for a in model1.agents]
ax3.hist2d(final_x1, final_y1, bins=[range(grid_size + 1), range(grid_size + 1)], cmap='Blues')
ax3.set_title('Scenario 1 Final Distribution')

final_x2 = [a.position[0] for a in model2.agents]
final_y2 = [a.position[1] for a in model2.agents]
ax4.hist2d(final_x2, final_y2, bins=[range(grid_size + 1), range(grid_size + 1)], cmap='Reds')
ax4.set_title('Scenario 2 Final Distribution')

plt.show()