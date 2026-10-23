# Technical Assessment 1: Random Walk Simulation Using AgentPy

**Programmer:** Arianne Beverly Marquez

**Course:** CS0065 (Intelligent Systems) 

## 📌 About This Project

This project explores agent-based modeling by simulating a "Random Walk" on a grid using Python. It visualizes how autonomous agents move, interact, and disperse in an environment over a set number of steps. 

The modified simulation includes:
* **Path Tracking:** Draws trail lines to show the exact path each agent took during the simulation.
* **Scenario Comparison:** Runs a side-by-side animated comparison between a standard "Random Walk" and a "Biased Walk" (where agents prefer certain directions).
* **Final Position Analysis:** Generates a 2D heatmap (histogram) to analyze where agents ultimately clustered at the end of the simulation.

## 📂 Files Included

* `MARQUEZ_Technical1.py`: The Python script containing the AgentPy model, custom walker logic, and Matplotlib interactive animations.
* `TA1_Marquez.pdf`: The complete project documentation, including code structure, program screenshots, and analytical answers regarding agent behavior.

## 🛠️ How to Run

1. Make sure you have Python installed on your computer.
2. You will need the `agentpy` and `matplotlib` libraries. You can install them via terminal:
   ```
   pip install agentpy matplotlib
   ```
3. Download or clone this repository.
4. Open your terminal or command prompt in the folder containing the files.
5. Run the following command:
   ```
   python MARQUEZ_Technical1.py
   ```
6. Enter the requested parameters in the terminal (number of agents, grid size, and steps). A window will pop up showing the live animation, followed by a final distribution analysis window once closed.
