import tkinter as tk
from tkinter import ttk

# TECHNICAL ASSESSMENT 3: CASE-BASED REASONING (CBR) SYSTEM
# Case Study 2: AI-Based Legal Decision Support System

def display_header():
    print(str('\nAI-BASED LEGAL DECISION SUPPORT SYSTEM (CYBERCRIME & E-THEFT)\n'))
    print(str('\nProgrammed by: Arianne Beverly V. Marquez & Lester Anthony G. Respicio\n'))

#STEP 3: Defining case base
case_base = [
    {
        'case_id': 'CR-2021-089',
        'title': 'People v. Arnaldo (Unauthorized ACH Transfer)',
        'problem': {
            'offense_type': 'Unauthorized Bank Transfer',
            'transfer_medium': 'Web Banking Portal',
            'evidence_available': 'Server Access Logs',
            'disputed_amount': 150000.0,
            'primary_defense': 'Lack of Direct Attribution / Shared Terminal'
        },
        'solution': {
            'precedent_title': 'G.R. No. 201142 - Doctrine of Digital Chain of Custody',
            'applicable_law': 'Cybercrime Prevention Act & E-Commerce Act (Sec. 33)',
            'core_argument': 'IP address mapping alone does not establish physical identity beyond reasonable doubt without session token correlation.',
            'recommended_motion': 'Motion to Suppress IP Telemetry pending ISP subscriber identity verification.'
        }
    },
    {
        'case_id': 'CR-2022-144',
        'title': 'State v. Macatangay (Mobile Wallet Phishing)',
        'problem': {
            'offense_type': 'Digital Fraud & Identity Theft',
            'transfer_medium': 'Mobile Banking App',
            'evidence_available': 'SMS OTP Delivery Logs',
            'disputed_amount': 45000.0,
            'primary_defense': 'Compromised Credentials via SIM Swap'
        },
        'solution': {
            'precedent_title': 'Crim. Case 4491 - Third-Party Interception Standard',
            'applicable_law': 'Access Devices Regulation Act (R.A. 8484)',
            'core_argument': 'Defendants credentials were hijacked via fraudulent SIM duplication, negating criminal intent.',
            'recommended_motion': 'Motion for Forensic Examination of Telco SIM re-issuance audit trails.'
        }
    },
    {
        'case_id': 'CR-2023-305',
        'title': 'People v. Tan (API Scripted Transfer)',
        'problem': {
            'offense_type': 'Electronic Theft',
            'transfer_medium': 'Automated Clearing House API',
            'evidence_available': 'API Gateway Transaction Payload',
            'disputed_amount': 520000.0,
            'primary_defense': 'Software Glitch / Involuntary Beneficiary'
        },
        'solution': {
            'precedent_title': 'G.R. No. 198774 - Absence of Animus Lucrandi',
            'applicable_law': 'Revised Penal Code Art. 308 in rel. to R.A. 10175',
            'core_argument': 'Automated system race condition caused erroneous double deposit without affirmative defendant exfiltration.',
            'recommended_motion': 'Motion for Independent Source-Code and Database Audit by court-appointed forensic expert.'
        }
    }
]

#STEP 4: Implementing similarity assessment

# Weighted scoring
FEATURE_WEIGHTS = {
    'offense_type': 0.30,
    'transfer_medium': 0.25,
    'evidence_available': 0.20,
    'primary_defense': 0.15,
    'amount_similarity': 0.10
}

# Simple Rule-Based Comparison
def calculate_amount_similarity(amt1, amt2):
    max_val = max(amt1, amt2)
    if max_val == 0:
        return 1.0
    return max(0.0, 1.0 - (abs(amt1 - amt2) / max_val))

# Attribute matching
def compute_case_similarity(new_case, past_case):
    p_new = new_case['problem']
    p_past = past_case['problem']

    score_offense = 1.0 if p_new['offense_type'].lower() == p_past['offense_type'].lower() else 0.0
    score_medium = 1.0 if p_new['transfer_medium'].lower() == p_past['transfer_medium'].lower() else 0.0
    score_evidence = 1.0 if p_new['evidence_available'].lower() == p_past['evidence_available'].lower() else 0.3
    score_defense = 1.0 if p_new['primary_defense'].lower() == p_past['primary_defense'].lower() else 0.2
    score_amount = calculate_amount_similarity(p_new['disputed_amount'], p_past['disputed_amount'])

    global_similarity = (
        (score_offense * FEATURE_WEIGHTS['offense_type']) +
        (score_medium * FEATURE_WEIGHTS['transfer_medium']) +
        (score_evidence * FEATURE_WEIGHTS['evidence_available']) +
        (score_defense * FEATURE_WEIGHTS['primary_defense']) +
        (score_amount * FEATURE_WEIGHTS['amount_similarity'])
    )
    return round(global_similarity, 4)

def retrieve_best_precedent(new_case, case_library):
    scored_cases = []
    for past_case in case_library:
        sim = compute_case_similarity(new_case, past_case)
        scored_cases.append((sim, past_case))
    
    scored_cases.sort(key=lambda item: item[0], reverse=True)
    return scored_cases[0], scored_cases

#STEP 5: Adapting retrieved solutions
def adapt_solution(retrieved_case, new_case):
    old_sol = retrieved_case['solution']
    new_prob = new_case['problem']
    
    adapted_argument = (
        f"{old_sol['core_argument']}In the current case, because the transaction was executed via "
        f"{new_prob['transfer_medium']}, the defense asserts that {new_prob['evidence_available']} "
        f"fails to conclusively prove intentional execution by the client regarding the PHP {new_prob['disputed_amount']:,.2f} transfer."
    )
    
    adapted_motion = (
        f"Urgent Motion to present forensic counter-evidence addressing {new_prob['evidence_available']} "
        f"and subpoena authentication records for {new_prob['transfer_medium']} transactions pursuant to {old_sol['applicable_law']}."
    )
    
    final_solution = {
        'applied_precedent': old_sol['precedent_title'],
        'applicable_law': old_sol['applicable_law'],
        'adapted_defense_argument': adapted_argument,
        'adapted_procedural_motion': adapted_motion
    }
    return final_solution

#STEP 6: Demonstrating learning (retain stage)
def retain_case(new_case, final_solution, case_library):
    retained_record = {
        'case_id': new_case['case_id'],
        'title': new_case.get('title', 'Adjudicated New Incident'),
        'problem': new_case['problem'],
        'solution': final_solution
    }
    case_library.append(retained_record)
    return retained_record

# MAIN WORKFLOW (GUI Implementation)
def main():
    # Print the header to the terminal first
    display_header()

    root = tk.Tk()
    root.title('AI-Based Legal Decision Support System')
    root.geometry('900x750')
    root.configure(bg='#f0f0f0')

    # Ensure main container expands
    main_frame = tk.Frame(root, bg='#f0f0f0')
    main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    # Centered Header (GUI)
    lbl_title = tk.Label(main_frame, text='AI-BASED LEGAL DECISION SUPPORT SYSTEM', font=('Helvetica', 16, 'bold'), bg='#f0f0f0')
    lbl_title.pack(pady=(0, 20))

    new_incident = {
        'case_id': 'CR-2026-901',
        'title': 'State v. S. Alvarez (E-Wallet Unauthorized Transfer)',
        'problem': {
            'offense_type': 'Electronic Theft',
            'transfer_medium': 'Mobile Banking App',
            'evidence_available': 'SMS OTP Delivery Logs',
            'disputed_amount': 92000.0,
            'primary_defense': 'Compromised Credentials via SIM Swap'
        }
    }

    # Left-aligned Table Title
    lbl_input = tk.Label(main_frame, text='[INPUT: INCOMING CLIENT LEGAL ISSUE]', font=('Helvetica', 11, 'bold'), bg='#f0f0f0')
    lbl_input.pack(anchor='w')

    # Treeview (Table)
    tree_frame = tk.Frame(main_frame)
    tree_frame.pack(fill=tk.X, pady=(5, 20))
    
    columns = ('Attribute', 'Details')
    tree = ttk.Treeview(tree_frame, columns=columns, show='headings', height=6)
    tree.heading('Attribute', text='Case Attribute')
    tree.heading('Details', text='Client Details')
    
    # stretch=True allows the table to adapt when resizing window
    tree.column('Attribute', width=200, anchor='w', stretch=False)
    tree.column('Details', width=600, anchor='w', stretch=True) 
    tree.pack(fill=tk.X, expand=True)

    tree.insert('', tk.END, values=('Case Reference', new_incident['case_id']))
    tree.insert('', tk.END, values=('Allegation', new_incident['problem']['offense_type']))
    tree.insert('', tk.END, values=('Transfer Medium', new_incident['problem']['transfer_medium']))
    tree.insert('', tk.END, values=('Available Evidence', new_incident['problem']['evidence_available']))
    tree.insert('', tk.END, values=('Disputed Amount', f"PHP {new_incident['problem']['disputed_amount']:,.2f}"))
    tree.insert('', tk.END, values=('Proposed Defense', new_incident['problem']['primary_defense']))

    # Scrollable Text Box for Logic Execution
    text_frame = tk.Frame(main_frame)
    text_frame.pack(fill=tk.BOTH, expand=True)
    
    scrollbar = tk.Scrollbar(text_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    text_output = tk.Text(text_frame, font=('Consolas', 10), bg='#f8f9fa', wrap=tk.WORD, yscrollcommand=scrollbar.set)
    text_output.pack(fill=tk.BOTH, expand=True)
    scrollbar.config(command=text_output.yview)

    def print_to_gui(msg):
        text_output.insert(tk.END, str(msg) + '\n')

    # Integrating your exact string modifications with GUI dashed lines
    print_to_gui('\nEXECUTING SIMILARITY ASSESSMENT (RETRIEVAL)\n')

    
    (best_score, best_case), all_scores = retrieve_best_precedent(new_incident, case_base)
    for score, item in all_scores:
        print_to_gui(f"-> Precedent [{item['case_id']}] Similarity: {score * 100:.2f}%")

    print_to_gui(f"\n !!! Best Match Found: [{best_case['case_id']}] {best_case['title']} !!! \n")

    print_to_gui('\nEXECUTING ADAPTING RETRIEVED SOLUTION\n')
    
    adapted_strategy = adapt_solution(best_case, new_incident)
    print_to_gui(f"Applicable Precedent : {adapted_strategy['applied_precedent']}")
    print_to_gui(f"\nAdapted Legal Argument:\n  {adapted_strategy['adapted_defense_argument']}")
    print_to_gui(f"\nRecommended Actionable Motion:\n  {adapted_strategy['adapted_procedural_motion']}\n")

    print_to_gui('\nEXECUTING RETAIN STAGE (LEARNING)\n')
    
    initial_count = len(case_base)
    new_record = retain_case(new_incident, adapted_strategy, case_base)
    
    print_to_gui(f"Initial Case Base Count : {initial_count}")
    print_to_gui(f"Added Case ID           : {new_record['case_id']}")
    print_to_gui(f"Updated Case Base Count : {len(case_base)}")

    text_output.config(state=tk.DISABLED)
    root.mainloop()

if __name__ == '__main__':
    main()
