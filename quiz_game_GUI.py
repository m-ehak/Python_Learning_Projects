import tkinter as tk
import json

# Sample questions as a dictionary
questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Rome", "Berlin"], "answer": "Paris"},
    {"question": "Which is the largest planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Jupiter"},
    # Add more questions as needed
]

current_question = 0
score = 0

def check_answer(selected_option):
    global current_question, score
    if selected_option == questions[current_question]['answer']:
        score += 1
    current_question += 1
    if current_question < len(questions):
        load_question()
    else:
        display_score()

def load_question():
    question_label.config(text=questions[current_question]['question'])
    for i, option in enumerate(option_buttons):
        option.config(text=questions[current_question]['options'][i], command=lambda opt=questions[current_question]['options'][i]: check_answer(opt))

def display_score():
    question_label.config(text=f"Your score is {score} out of {len(questions)}")
    for button in option_buttons:
        button.config(state='disabled')

# Set up the main window
root = tk.Tk()
root.title("Quiz Game")

question_label = tk.Label(root, text="")
question_label.pack()

option_buttons = [tk.Button(root, text="", width=20) for _ in range(4)]
for button in option_buttons:
    button.pack(pady=5)

# Load the first question
load_question()

# Start the main event loop
root.mainloop()
