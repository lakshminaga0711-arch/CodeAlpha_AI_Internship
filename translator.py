import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import threading


def translate_text():
    text = input_text.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Warning", "Please enter some text.")
        return

    source = source_language.get()
    target = target_language.get()

    # Disable button while translating
    translate_button.config(state="disabled")
    status_label.config(text="Translating... Please wait")

    # Run translation in background
    thread = threading.Thread(
        target=do_translation,
        args=(text, source, target),
        daemon=True
    )
    thread.start()


def do_translation(text, source, target):
    try:
        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        root.after(
            0,
            lambda: show_result(translated)
        )

    except Exception as error:
        root.after(
            0,
            lambda: show_error(error)
        )


def show_result(translated):
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, translated)

    translate_button.config(state="normal")
    status_label.config(text="Translation completed ✓")


def show_error(error):
    translate_button.config(state="normal")
    status_label.config(text="Translation failed")

    messagebox.showerror(
        "Translation Error",
        "Unable to translate.\n\nPlease check your internet connection."
    )


def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)
    status_label.config(text="Ready")


# -----------------------------
# Main Window
# -----------------------------

root = tk.Tk()
root.title("AI Language Translator")
root.geometry("700x650")
root.configure(bg="#EAF4FF")

# -----------------------------
# Title
# -----------------------------

title_label = tk.Label(
    root,
    text="🌐 AI Language Translator",
    font=("Arial", 24, "bold"),
    bg="#1565C0",
    fg="white",
    pady=15
)
title_label.pack(fill="x")


subtitle_label = tk.Label(
    root,
    text="Translate text quickly between different languages",
    font=("Arial", 11),
    bg="#EAF4FF",
    fg="#333333"
)
subtitle_label.pack(pady=10)


# -----------------------------
# Language Selection
# -----------------------------

language_frame = tk.Frame(
    root,
    bg="#EAF4FF"
)
language_frame.pack(pady=5)


tk.Label(
    language_frame,
    text="Source Language",
    font=("Arial", 11, "bold"),
    bg="#EAF4FF",
    fg="#1565C0"
).grid(row=0, column=0, padx=20)


tk.Label(
    language_frame,
    text="Target Language",
    font=("Arial", 11, "bold"),
    bg="#EAF4FF",
    fg="#1565C0"
).grid(row=0, column=1, padx=20)


languages = [
    "auto",
    "en",
    "te",
    "hi",
    "ta",
    "kn",
    "ml"
]


source_language = ttk.Combobox(
    language_frame,
    values=languages,
    state="readonly",
    width=15
)
source_language.set("auto")
source_language.grid(row=1, column=0, padx=20, pady=5)


target_language = ttk.Combobox(
    language_frame,
    values=languages,
    state="readonly",
    width=15
)
target_language.set("te")
target_language.grid(row=1, column=1, padx=20, pady=5)


# -----------------------------
# Input Text
# -----------------------------

tk.Label(
    root,
    text="Enter Text",
    font=("Arial", 12, "bold"),
    bg="#EAF4FF",
    fg="#1565C0"
).pack(pady=(15, 5))


input_text = tk.Text(
    root,
    height=7,
    width=65,
    font=("Arial", 12),
    bg="white",
    fg="#222222",
    insertbackground="black",
    relief="solid",
    borderwidth=1
)
input_text.pack()


# -----------------------------
# Buttons
# -----------------------------

button_frame = tk.Frame(
    root,
    bg="#EAF4FF"
)
button_frame.pack(pady=15)


translate_button = tk.Button(
    button_frame,
    text="🌐 Translate",
    command=translate_text,
    font=("Arial", 12, "bold"),
    bg="#2E7D32",
    fg="white",
    activebackground="#1B5E20",
    activeforeground="white",
    width=15,
    padx=10,
    pady=7,
    cursor="hand2"
)
translate_button.grid(row=0, column=0, padx=10)


clear_button = tk.Button(
    button_frame,
    text="🗑 Clear",
    command=clear_text,
    font=("Arial", 12, "bold"),
    bg="#D32F2F",
    fg="white",
    activebackground="#B71C1C",
    activeforeground="white",
    width=12,
    padx=10,
    pady=7,
    cursor="hand2"
)
clear_button.grid(row=0, column=1, padx=10)


# -----------------------------
# Output
# -----------------------------

tk.Label(
    root,
    text="Translated Text",
    font=("Arial", 12, "bold"),
    bg="#EAF4FF",
    fg="#1565C0"
).pack(pady=(5, 5))


output_text = tk.Text(
    root,
    height=7,
    width=65,
    font=("Arial", 12),
    bg="#F5FFF5",
    fg="#1B5E20",
    relief="solid",
    borderwidth=1
)
output_text.pack()


# -----------------------------
# Status
# -----------------------------

status_label = tk.Label(
    root,
    text="Ready",
    font=("Arial", 10, "italic"),
    bg="#EAF4FF",
    fg="#555555"
)
status_label.pack(pady=10)


# Start application
root.mainloop()