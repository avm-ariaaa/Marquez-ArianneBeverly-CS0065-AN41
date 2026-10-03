import tkinter as tk
import os


# PART 1: Knowledge Representation (KR) Setup

# Task 1A: Create a Knowledge Base
facts = {
    "chest_pain_severity": 8,       
    "shortness_of_breath": True,    
    "dizziness": True,              
    "left_arm_numbness": True,      
    "systolic_bp": 165              
}


# PART 2: Implement Rule-Based Reasoning (RBR)

# Task 2A: Create at least 3 IF THEN rules
def rule_severe_pain(f):
    if f.get("chest_pain_severity", 0) >= 7 and f.get("left_arm_numbness") == True:
        return "Administer aspirin and call emergency services immediately."
    return None

def rule_high_bp(f):
    if f.get("systolic_bp", 0) > 140 and f.get("dizziness") == True:
        return "Monitor blood pressure closely and keep the patient seated."
    return None

def rule_breathing(f):
    if f.get("shortness_of_breath") == True:
        return "Provide supplemental oxygen."
    return None

# Task 2B: Implement an Inference Engine
def inference_engine(current_facts, rule_set):
    inferred_actions = []
    for rule in rule_set:
        action = rule(current_facts)
        if action:  
            inferred_actions.append(action)
    return inferred_actions


# PART 3: Implement Case-Based Reasoning (CBR)

# Task 3A: Build a Case Base
case_base = [
    {
        "problem": {"chest_pain_severity": 2, "shortness_of_breath": False, "left_arm_numbness": False},
        "solution": "Recommend rest and antacids. Monitor for 30 minutes."
    },
    {
        "problem": {"chest_pain_severity": 9, "shortness_of_breath": True, "left_arm_numbness": True},
        "solution": "Code Red: Suspected Myocardial Infarction. Dispatch ambulance immediately."
    },
    {
        "problem": {"chest_pain_severity": 0, "shortness_of_breath": False, "left_arm_numbness": True},
        "solution": "Assess for pinched nerve or localized musculoskeletal strain."
    }
]

def get_similarity(past_problem, new_problem):
    matches = 0
    for key in new_problem:
        if new_problem.get(key) == past_problem.get(key):
            matches += 1
    return matches


# CUSTOM MEDICAL GUI INTERFACE

class MedicalExpertSystemUI:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()

    def abort_program(self):
        """Kills the entire program instantly if the 'X' button is clicked."""
        print("System terminated by user.")
        os._exit(0) # Forces an immediate operating system level exit

    def input_new_case(self):
        win = tk.Toplevel(self.root)
        win.title("⚕️ New Patient Entry")
        win.geometry("450x350")
        win.configure(bg="#FFFFFF")
        
        win.protocol("WM_DELETE_WINDOW", self.abort_program)
        
        tk.Label(win, text="Input Patient Symptoms 🩺", font=("Helvetica", 16, "bold"), fg="#D32F2F", bg="#FFFFFF").pack(pady=15)
        
        tk.Label(win, text="Chest Pain Severity (0-10):", font=("Helvetica", 10, "bold"), fg="#1976D2", bg="#FFFFFF").pack(pady=(10, 0))
        pain_var = tk.IntVar(value=0)
        tk.Scale(win, from_=0, to=10, orient="horizontal", variable=pain_var, bg="#FFFFFF", highlightthickness=0, length=200).pack()
        
        breath_var = tk.BooleanVar()
        tk.Checkbutton(win, text="Patient has Shortness of Breath", variable=breath_var, font=("Helvetica", 10), bg="#FFFFFF", fg="#333333", selectcolor="#FFFFFF").pack(pady=5)
        
        numb_var = tk.BooleanVar()
        tk.Checkbutton(win, text="Patient has Left Arm Numbness", variable=numb_var, font=("Helvetica", 10), bg="#FFFFFF", fg="#333333", selectcolor="#FFFFFF").pack(pady=5)
        
        self.new_case_data = None
        
        def submit_case():
            self.new_case_data = {
                "chest_pain_severity": pain_var.get(),
                "shortness_of_breath": breath_var.get(),
                "left_arm_numbness": numb_var.get()
            }
            win.destroy() 
            
        tk.Button(win, text="Analyze Case", bg="#D32F2F", fg="white", font=("Helvetica", 10, "bold"), command=submit_case).pack(pady=20)
        
        self.root.wait_window(win)
        return self.new_case_data
        
    def show_results(self, rbr_text, cbr_text):
        win = tk.Toplevel(self.root)
        win.title("⚕️ Medical AI Diagnostics") 
        win.geometry("550x450")
        win.configure(bg="#FFFFFF") 
        
        win.protocol("WM_DELETE_WINDOW", self.abort_program)
        
        tk.Label(win, text="AI Diagnostic Results 🩺", font=("Helvetica", 18, "bold"), fg="#D32F2F", bg="#FFFFFF").pack(pady=15)
        
        tk.Label(win, text="Rule-Based Reasoning (RBR):", font=("Helvetica", 11, "bold"), fg="#1976D2", bg="#FFFFFF").pack(anchor="w", padx=20)
        rbr_box = tk.Text(win, font=("Helvetica", 10), fg="#333333", bg="#FFFFFF", wrap="word", height=4, bd=0, highlightthickness=0)
        rbr_box.insert("1.0", rbr_text)
        rbr_box.config(state="disabled")
        rbr_box.pack(fill="x", padx=30, pady=5)
        
        tk.Label(win, text="Case-Based Reasoning (CBR):", font=("Helvetica", 11, "bold"), fg="#1976D2", bg="#FFFFFF").pack(anchor="w", padx=20, pady=(15, 0))
        cbr_box = tk.Text(win, font=("Helvetica", 10), fg="#333333", bg="#FFFFFF", wrap="word", height=4, bd=0, highlightthickness=0)
        cbr_box.insert("1.0", cbr_text)
        cbr_box.config(state="disabled")
        cbr_box.pack(fill="x", padx=30, pady=5)
        
        btn = tk.Button(win, text="Acknowledge & Continue", bg="#1976D2", fg="white", font=("Helvetica", 10, "bold"), command=win.destroy)
        btn.pack(pady=25)
        
        self.root.wait_window(win)
        
    def ask_revision(self, suggested_solution):
        win = tk.Toplevel(self.root)
        win.title("⚕️ Revise Solution Step") 
        win.geometry("550x250")
        win.configure(bg="#FFFFFF")
        
        win.protocol("WM_DELETE_WINDOW", self.abort_program)
        
        self.revised_solution = None
        
        tk.Label(win, text="Revise CBR Solution? 🩺", font=("Helvetica", 14, "bold"), fg="#D32F2F", bg="#FFFFFF").pack(pady=15)
        
        entry = tk.Entry(win, width=70, font=("Helvetica", 10))
        entry.insert(0, suggested_solution)
        entry.pack(pady=15, padx=20)
        
        def save():
            self.revised_solution = entry.get()
            win.destroy()
            
        def keep():
            self.revised_solution = suggested_solution
            win.destroy()
            
        tk.Button(win, text="Save Revision", bg="#D32F2F", fg="white", font=("Helvetica", 10, "bold"), command=save).pack(side="left", padx=60, pady=20)
        tk.Button(win, text="Keep Original", bg="#1976D2", fg="white", font=("Helvetica", 10, "bold"), command=keep).pack(side="right", padx=60, pady=20)
        
        self.root.wait_window(win)
        return self.revised_solution
        
    def show_retained(self, count):
        win = tk.Toplevel(self.root)
        win.title("⚕️ Case Base Updated")
        win.geometry("350x180")
        win.configure(bg="#FFFFFF")
        
        win.protocol("WM_DELETE_WINDOW", self.abort_program)
        
        tk.Label(win, text="✅ Case Retained Successfully", font=("Helvetica", 12, "bold"), fg="#1976D2", bg="#FFFFFF").pack(pady=20)
        tk.Label(win, text=f"Total cases in Case Base now: {count}", font=("Helvetica", 11), fg="#D32F2F", bg="#FFFFFF").pack()
        
        tk.Button(win, text="View Reports", bg="#1976D2", fg="white", font=("Helvetica", 10, "bold"), command=win.destroy).pack(pady=20)
        self.root.wait_window(win)

    def show_reports(self, cases):
        win = tk.Toplevel(self.root)
        win.title("⚕️ System Reports")
        win.geometry("600x400")
        win.configure(bg="#FFFFFF")
        
        win.protocol("WM_DELETE_WINDOW", win.destroy)
        
        tk.Label(win, text="Case Base Reports 🩺", font=("Helvetica", 16, "bold"), fg="#D32F2F", bg="#FFFFFF").pack(pady=15)
        
        tk.Button(win, text="Close System", bg="#D32F2F", fg="white", font=("Helvetica", 10, "bold"), command=win.destroy).pack(side="bottom", pady=15)
        
        frame = tk.Frame(win, bg="#FFFFFF")
        frame.pack(fill="both", expand=True, padx=20, pady=(0, 10))
        
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")
        
        text_area = tk.Text(frame, font=("Helvetica", 10), bg="#F9F9F9", fg="#333333", wrap="word", yscrollcommand=scrollbar.set, padx=15, pady=10)
        
        report_content = ""
        for i, case in enumerate(cases):
            report_content += f"CASE {i+1}:\n"
            report_content += f"Problem Variables: {case['problem']}\n"
            report_content += f"\nAssigned Solution: {case['solution']}\n"
            report_content += "-"*60 + "\n\n"
            
        text_area.insert("1.0", report_content)
        text_area.config(state="disabled")
        text_area.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=text_area.yview)
        
        self.root.wait_window(win)


def run_expert_system():
    root = tk.Tk()
    ui = MedicalExpertSystemUI(root)
    
    rules_list = [rule_severe_pain, rule_high_bp, rule_breathing]
    actions_to_take = inference_engine(facts, rules_list)
    rbr_output = "\n".join([f"• {action}" for action in actions_to_take])

    new_patient_problem = ui.input_new_case()
    
    # Extra safety check
    if not new_patient_problem:
        os._exit(0)
    
    best_match = None
    highest_score = -1
    for case in case_base:
        score = get_similarity(case["problem"], new_patient_problem)
        if score > highest_score:
            highest_score = score
            best_match = case
            
    suggested_solution = best_match["solution"]
    cbr_output = f"Most similar case found (Match Score: {highest_score}).\nSuggested Solution: {suggested_solution}"
    
    ui.show_results(rbr_output, cbr_output)
    final_solution = ui.ask_revision(suggested_solution)
    
    new_case = {"problem": new_patient_problem, "solution": final_solution}
    case_base.append(new_case)
    
    ui.show_retained(len(case_base))
    ui.show_reports(case_base)
    
    root.destroy()

if __name__ == "__main__":
    print("\nProgrammed by: Arianne Beverly Marquez & Lester Anthony Respicio\n")
run_expert_system()