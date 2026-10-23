# Technical Assessment 4: Knowledge Representation, RBR, and CBR

**Programmers:** Arianne Beverly Marquez & Lester Anthony Respicio

**Course:** CS0065 (Intelligent Systems) - FEU Institute of Technology

## 📌 About This Project

This project is a **Medical AI Diagnostic System** focused on evaluating heart attack symptoms. It demonstrates and compares two different artificial intelligence reasoning methods:

1. **Rule-Based Reasoning (RBR):** Uses predefined IF-THEN rules to instantly recommend medical actions based on specific symptom thresholds (e.g., blood pressure, chest pain severity).
2. **Case-Based Reasoning (CBR):** Compares a new patient's symptoms to a database of past medical cases to find the closest match, suggest a treatment solution, and allow the user to revise and retain the new case for future learning.

## 📂 Files Included

* `TA4_Marquez_Respicio.py`: The main Python program featuring the Knowledge Base, RBR Inference Engine, CBR logic, and a custom graphical user interface (GUI) built with Tkinter.
* `TA4_Marquez_Respicio.pdf`: The complete project documentation, including code structure, program screenshots, and a comparative reflection on RBR vs. CBR.

## 🛠️ How to Run

1. Make sure you have Python installed on your computer.
2. Download or clone this repository.
3. Open your terminal or command prompt in the folder containing the files.
4. Run the following command:

   ```
   python TA4_Marquez_Respicio.py
   ```

5. A "New Patient Entry" window will appear where you can input symptoms to see how both the RBR and CBR systems diagnose the case.