import tkinter as tk
from tkinter import scrolledtext


# FAQ questions and answers
faqs = {
    "what is python":
        "Python is a high-level, easy-to-learn programming language.",

    "what is ai":
        "AI stands for Artificial Intelligence. It enables machines to perform tasks that normally require human intelligence.",

    "what is artificial intelligence":
        "Artificial Intelligence is the ability of computers or machines to perform tasks that normally require human intelligence.",

    "what is machine learning":
        "Machine Learning is a branch of AI that allows computers to learn from data.",

    "what is your name":
        "I am your FAQ Chatbot.",

    "how are you":
        "I am doing great! How can I help you?",

    "what can you do":
        "I can answer frequently asked questions.",

    "thank you":
        "You're welcome!",

    "thanks":
        "You're welcome!",

    "bye":
        "Goodbye! Have a nice day."
}


def get_response():
    question = user_input.get().strip().lower()

    if not question:
        status_label.config(text="Please enter a question.")
        return

    # Display user's question
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "You: " + question + "\n", "user")

    # Find answer
    response = faqs.get(
        question,
        "Sorry, I don't know the answer to that question."
    )

    # Display chatbot answer
    chat_area.insert(tk.END, "Bot: " + response + "\n\n", "bot")
    chat_area.config(state=tk.DISABLED)

    # Clear input box
    user_input.delete(0, tk.END)

    status_label.config(text="Ready")


def clear_chat():
    chat_area.config(state=tk.NORMAL)
    chat_area.delete("1.0", tk.END)

    chat_area.insert(
        tk.END,
        "Bot: Hello! 👋 I am your FAQ Chatbot.\n"
        "Bot: Ask me a question!\n\n",
        "bot"
    )

    chat_area.config(state=tk.DISABLED)
    user_input.delete(0, tk.END)
    status_label.config(text="Ready")


# -----------------------------------
# Main Window
# -----------------------------------

root = tk.Tk()
root.title("FAQ Chatbot")
root.geometry("700x700")
root.configure(bg="#EAF4FF")
root.resizable(False, False)


# -----------------------------------
# Header
# -----------------------------------

header = tk.Frame(
    root,
    bg="#1565C0",
    height=80
)
header.pack(fill="x")

title_label = tk.Label(
    header,
    text="🤖 FAQ Chatbot",
    font=("Arial", 24, "bold"),
    bg="#1565C0",
    fg="white"
)
title_label.pack(pady=20)


# -----------------------------------
# Description
# -----------------------------------

description = tk.Label(
    root,
    text="Ask questions and get instant answers",
    font=("Arial", 12),
    bg="#EAF4FF",
    fg="#333333"
)
description.pack(pady=12)


# -----------------------------------
# Chat Area
# -----------------------------------

chat_area = scrolledtext.ScrolledText(
    root,
    width=75,
    height=22,
    font=("Arial", 11),
    wrap=tk.WORD,
    bg="white",
    fg="#222222",
    relief="solid",
    borderwidth=1
)

chat_area.pack(
    padx=20,
    pady=10
)

# Text styles
chat_area.tag_config(
    "user",
    foreground="#1565C0",
    font=("Arial", 11, "bold")
)

chat_area.tag_config(
    "bot",
    foreground="#2E7D32",
    font=("Arial", 11, "bold")
)

# Welcome message
chat_area.insert(
    tk.END,
    "Bot: Hello! 👋 I am your FAQ Chatbot.\n"
    "Bot: Ask me a question!\n\n",
    "bot"
)

chat_area.config(state=tk.DISABLED)


# -----------------------------------
# Input Section
# -----------------------------------

input_label = tk.Label(
    root,
    text="Ask your question:",
    font=("Arial", 12, "bold"),
    bg="#EAF4FF",
    fg="#1565C0"
)
input_label.pack(pady=(5, 5))


user_input = tk.Entry(
    root,
    font=("Arial", 12),
    width=55,
    relief="solid",
    borderwidth=1
)
user_input.pack(pady=5)


# -----------------------------------
# Buttons
# -----------------------------------

button_frame = tk.Frame(
    root,
    bg="#EAF4FF"
)
button_frame.pack(pady=12)


ask_button = tk.Button(
    button_frame,
    text="💬 Ask",
    command=get_response,
    font=("Arial", 11, "bold"),
    bg="#2E7D32",
    fg="white",
    activebackground="#1B5E20",
    activeforeground="white",
    width=15,
    pady=8,
    cursor="hand2"
)
ask_button.grid(
    row=0,
    column=0,
    padx=10
)


clear_button = tk.Button(
    button_frame,
    text="🗑 Clear",
    command=clear_chat,
    font=("Arial", 11, "bold"),
    bg="#D32F2F",
    fg="white",
    activebackground="#B71C1C",
    activeforeground="white",
    width=15,
    pady=8,
    cursor="hand2"
)
clear_button.grid(
    row=0,
    column=1,
    padx=10
)


# -----------------------------------
# Status
# -----------------------------------

status_label = tk.Label(
    root,
    text="Ready",
    font=("Arial", 10, "italic"),
    bg="#EAF4FF",
    fg="#555555"
)
status_label.pack(pady=5)


# Press Enter to ask
root.bind("<Return>", lambda event: get_response())


# Start application
root.mainloop()