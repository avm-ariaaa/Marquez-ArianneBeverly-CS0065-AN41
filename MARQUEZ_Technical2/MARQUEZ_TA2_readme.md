# Technical Assessment 2: Rule-Based Agent

**Programmer:** Arianne Beverly Marquez  
**Course:** CS0065 (Intelligent Systems)   

## 📌 About This Project
This project implements a **Rule-Based Agent** (a vacuum cleaner robot) that operates in a multi-room environment. The agent perceives its current surroundings and makes decisions based on predefined rules:
1. **If the current room is dirty**, clean it.
2. **If the current room is clean**, move to another room.

The project is divided into the standard 2-room environment (Rooms A and B) and an expanded **Bonus Task** featuring a 3-room environment (Rooms A, B, and C). The bonus implementation includes randomized movement logic for finding dirty rooms and a dynamic, text-based grid visualization (e.g., `[A-Agent] [B-Dirty] [C-Clean]`).

## 📂 Files Included
* `TA2_OPT_TASK_MARQUEZ.py` (or your equivalent Python file name): The main Python script containing the environment setup, rule-based agent logic, and terminal visualization.
* `TA2_Marquez.pdf`: The complete documentation containing the step-by-step laboratory output, program screenshots, and analysis question answers.

## 🛠️ How to Run
1. Make sure you have Python 3.x installed on your computer.
2. Open your terminal or command prompt in the folder containing the script.
3. Run the following command:
   ```bash
   python TA2_OPT_TASK_MARQUEZ.py
   ```
4. When prompted, enter the initial states of the rooms (type `Dirty` or `Clean`) and the number of steps you want the agent to run. 
5. Watch the agent evaluate, clean, and navigate the environment in the terminal!
