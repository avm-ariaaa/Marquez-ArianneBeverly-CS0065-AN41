import tkinter as tk
from tkinter import messagebox
from textblob import TextBlob

# Global counters for the summary
pos_count = 0
neg_count = 0
neu_count = 0

def add_new_sentence():
    global pos_count, neg_count, neu_count
    
    # Get the sentence from the single-line entry
    sentence = entry.get().strip()
    
    if not sentence:
        messagebox.showwarning("Input Error", "Please enter a sentence.")
        return
        
    # TextBlob sentiment analysis
    s = TextBlob(sentence)
    p = s.polarity
    
    # Make a decision based on the polarity
    if p < 0:
        sentiment = "Negative"
        neg_count += 1
    elif p == 0:
        sentiment = "Neutral"
        neu_count += 1
    elif p > 0 and p <= 1:
        sentiment = "Positive"
        pos_count += 1
        
    # Append the result to the history text area
    history_text.config(state=tk.NORMAL) # Enable editing momentarily
    history_text.insert(tk.END, f"Sentence: {sentence}\nSentiment: {sentiment}\n")
    history_text.insert(tk.END, "-"*40 + "\n")
    history_text.see(tk.END) # Auto-scroll to the bottom
    history_text.config(state=tk.DISABLED) # Disable editing 
    
    # Update the summary labels and clear the entry box for the next input
    update_summary()
    entry.delete(0, tk.END)

def enter_new_sentences():
    """Clears the history and resets counters to start a new batch of sentences."""
    global pos_count, neg_count, neu_count
    
    # Reset counters
    pos_count = neg_count = neu_count = 0
    
    # Clear history text area
    history_text.config(state=tk.NORMAL)
    history_text.delete("1.0", tk.END)
    history_text.config(state=tk.DISABLED)
    
    # Reset summary and entry box
    update_summary()
    entry.delete(0, tk.END)

def update_summary():
    """Updates the summary tally at the bottom."""
    summary_label.config(text=f"Total Positive: {pos_count}   |   Total Negative: {neg_count}   |   Total Neutral: {neu_count}")
    total_label.config(text=f"Total number of sentences entered: {pos_count + neg_count + neu_count}")

# Main GUI Setup 
root = tk.Tk()
root.title("Technical 5 -- Sentiment Analysis Log")
root.geometry("600x550")
root.minsize(550, 450) # Prevents the window from being squeezed too small

# Header 
tk.Label(root, text="Sentiment Analysis", font=("Arial", 15, "bold", "underline")).pack(pady=5)
tk.Label(root, text="Programmed by: Arianne Beverly Marquez", font=("Arial", 9, "italic")).pack(pady=5)

# Bottom Frame (Input, Summary, and Buttons) 
bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=10)

# Summary Labels (Inside bottom frame)
summary_label = tk.Label(bottom_frame, text="Total Positive: 0   |   Total Negative: 0   |   Total Neutral: 0", font=("Arial", 10, "bold"))
summary_label.pack(pady=5)

total_label = tk.Label(bottom_frame, text="Total number of sentences entered: 0", font=("Arial", 10, "bold"))
total_label.pack(pady=2)

# Input Field and Instructions (Inside bottom frame)
tk.Label(bottom_frame, text="Type a sentence below:").pack(pady=(10, 0))
tk.Label(bottom_frame, text="(You may press Enter button on your keyboard or click the 'Enter Sentence' button below)", font=("Arial", 8, "italic"), fg="#555555").pack()

entry = tk.Entry(bottom_frame)
entry.pack(fill=tk.X, pady=5) # makes the entry box stretch horizontally with the window

# Buttons Frame (Inside bottom frame)
btn_frame = tk.Frame(bottom_frame)
btn_frame.pack(pady=5)

add_btn = tk.Button(btn_frame, text="Add New Sentence", bg="lightblue", width=18, command=add_new_sentence)
add_btn.grid(row=0, column=0, padx=5)

enter_btn = tk.Button(btn_frame, text="Enter Sentence", bg="lightgreen", width=18, command=add_new_sentence)
enter_btn.grid(row=0, column=1, padx=5)

clear_btn = tk.Button(btn_frame, text="Enter New Sentence/s (Reset)", bg="#ffb3b3", width=24, command=enter_new_sentences)
clear_btn.grid(row=0, column=2, padx=5)

#  Middle Frame (History Text Area) 
history_text = tk.Text(root, state=tk.DISABLED, bg="#f0f0f0")
history_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

# Bind the Enter key
root.bind('<Return>', lambda event: add_new_sentence())

root.mainloop()