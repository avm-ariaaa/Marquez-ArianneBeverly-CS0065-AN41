import tkinter as tk
from tkinter import messagebox

# Datasets
happy_dataset = ["happy", "joy", "cheerful", "good", "great", "excellent", "love", "smile", "fantastic", "wonderful", "delight"]
sad_dataset = ["sad", "sorrow", "depressed", "bad", "terrible", "awful", "hate", "cry", "miserable", "tragic", "grief", "disappointed"]

def number_happy(sentence):
    """Returns the number of words in a given string that are in the happy dataset."""
    count = 0
    for word in sentence.lower().split():
        clean_word = word.strip(".,!?\"'") # Strip punctuation for accurate matching
        if clean_word in happy_dataset:
            count += 1
    return count

def number_sad(sentence):
    """Returns the number of words in a given string that are in the sad dataset."""
    count = 0
    for word in sentence.lower().split():
        clean_word = word.strip(".,!?\"'") 
        if clean_word in sad_dataset:
            count += 1
    return count

def evaluate_challenge():
    sentence = entry.get()
    
    if not sentence.strip():
        messagebox.showwarning("Input Error", "Please enter a sentence to analyze.")
        return
        
    happy_count = number_happy(sentence)
    sad_count = number_sad(sentence)
    
    # Find the tone of the sentence based on the higher level
    if happy_count > sad_count:
        analysis = "Positive (Happy)"
    elif sad_count > happy_count:
        analysis = "Negative (Sad)"
    else:
        analysis = "Neutral"
        
    # Format and display 
    result = f"Number of happy words: {happy_count}\n"
    result += f"Number of sad words: {sad_count}\n\n"
    result += f"Analysis: {analysis}"
    
    messagebox.showinfo("Challenge Output", result)

def reset_entry():
    """Clears the entry box for a new sentence."""
    entry.delete(0, tk.END)

# Main GUI Setup 
root = tk.Tk()
root.title("Technical 5 -- Sentiment Challenge")
root.geometry("450x250")
root.minsize(400, 250) # Prevents the window from becoming too small

# Header Labels 
tk.Label(root, text="Sentiment Calculator", font=("Arial", 15, "bold", "underline")).pack(pady=5)
tk.Label(root, text="Programmed by: Arianne Beverly & Lester Anthony Respicio", font=("Arial", 9, "italic")).pack(pady=5)

# Content Frame 
content_frame = tk.Frame(root)
content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

tk.Label(content_frame, text="Enter a single sentence to evaluate its tone:", font=("Arial", 10, "bold")).pack(pady=(10, 5))

# Input Field 
entry = tk.Entry(content_frame)
entry.pack(fill=tk.X, pady=5) # allows it to stretch horizontally with the window)

# Buttons Frame to keep them side-by-side
btn_frame = tk.Frame(content_frame)
btn_frame.pack(pady=15)

# Evaluate Button
btn = tk.Button(btn_frame, text="Analyze Tone", bg="lightgreen", width=15, command=evaluate_challenge)
btn.grid(row=0, column=0, padx=5)

# Reset Button
reset_btn = tk.Button(btn_frame, text="Enter New Sentence", bg="#ffb3b3", width=20, command=reset_entry)
reset_btn.grid(row=0, column=1, padx=5)

# Bind the Enter key to automatically trigger the analysis
root.bind('<Return>', lambda event: evaluate_challenge())

root.mainloop()